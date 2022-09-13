import os
import string
import uuid
from binascii import hexlify
from datetime import timezone
import random
from aead import AEAD
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.mail import send_mail
from bunguo import settings


def utc_to_local(utc_dt):
    try:
        a = utc_dt.replace(tzinfo=timezone.utc).astimezone(tz=None)
    except Exception as e:
        print(e)
        return utc_dt
    return a


def local_to_utc(local_dt):
    return local_dt.astimezone(timezone.utc)


def validate_request(reqiureddict, obj):
    for d in reqiureddict:
        if d not in obj:
            raise Exception('Please set required fields')


def choice_parser(choices):
    return [{"id": choice[0], "value": choice[1]} for choice in choices]


def generate_pk(prefix, upper=False, length=15, separator="-"):
    chars = "%s%s%s%s" % (
        string.ascii_uppercase, string.digits, uuid.uuid1().hex, hexlify(os.urandom(16)).decode("utf-8"))
    pk = prefix.lower() + separator + "".join(random.choice(chars) for _ in range(length)).lower()
    if upper:
        pk = pk.upper()
    return pk


def generate_crypto_key():
    return AEAD.generate_key()


def encrypt_string(val, key):
    try:
        cryptor = AEAD(key)
        ct = cryptor.encrypt(val.encode('utf-8'), settings.SECRET_KEY.encode('utf-8'))
        return ct
    except Exception as e:
        print(e)
        return ''


def decrypt_string(val, key):
    try:
        cryptor = AEAD(key)
        ct = cryptor.decrypt(val, settings.SECRET_KEY.encode('utf-8'))
        return ct.decode('utf-8')

    except Exception as e:
        print(e)
        return ''


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
def get_model_field_names(model):
    if model is not None:
        return [f.name for f in model._meta.fields]

def in_model_fields(model, field_name):
    field_names = get_model_field_names(model)
    return field_name in field_names


def in_model_fields(model, field_name):
    field_names = get_model_field_names(model)
    return field_name in field_names


def send_email(subject, body, to, template_path, context, from_email=settings.DEFAULT_FROM_EMAIL):
    from django.template import loader
    try:
        html_message = loader.render_to_string(template_path, context)
        send_mail(
            subject=subject,
            message=body,
            from_email=from_email,
            recipient_list=to,
            fail_silently=False,
            html_message=html_message
        )
    except Exception as e:
        print(e)


def send_otp(email, user_code,first_name,last_name):
    try:
        email_template_name = 'register.html'
        context = {
            'first_name': first_name,
            'last_name': last_name,
            'code': user_code
        }

        send_email(subject='Yeni Kayıt',
                   body='',
                   to=[email],
                   template_path=email_template_name,
                   context=context
                   )
        return True
    except Exception as e:
        print(e)
        return False


def send_password_reset_email(email, user_code,first_name,last_name):
    try:
        email_template_name = 'password_reset.html'
        context = {
            'first_name': first_name,
            'last_name': last_name,
            'code': user_code
        }

        send_email(subject='Şifre Sıfırlama',
                   body='',
                   to=[email],
                   template_path=email_template_name,
                   context=context
                   )
        return True
    except Exception as e:
        print(e)
        return False


def send_register_email(user):
    try:
        email_template_name = 'register.html'
        use_https = False
        if settings.DEBUG:
            domain = settings.EMAIL_SERVER_NAME + ":8080"
        else:
            domain = settings.EMAIL_SERVER_NAME

        token = user.generate_token()

        context = {
            'user': user,
            'link': 'https' if use_https else 'http' + '://' + domain + '/set-password?token=' + str(token)
        }

        send_email(subject='Yeni Kayıt',
                   body='',
                   to=[user.email],
                   template_path=email_template_name,
                   context=context
                   )
        return True
    except Exception as e:
        print(e)