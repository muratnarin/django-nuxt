from django.contrib.auth.hashers import make_password
from rest_framework.exceptions import APIException
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.db import transaction
# import pyotp
import random
from core import settings, utils
from core.utils import get_tokens_for_user
from core.base_view import BaseViewSet
from core.utils import send_password_reset_email, send_register_email
from user.models import User, Customer, Parameter, ParameterGroup, Contractor
from user.serializers import UserSerializer, CustomerSerializer, ParameterSerializer, ParameterGroupSerializer, \
    ParameterDetailSerializer, CustomerDetailSerializer, MyTokenObtainPairSerializer, ContractorSerializer, \
    UserDetailSerializer
from user.filters import ParameterFilter
from datetime import datetime
from dateutil.relativedelta import relativedelta
from rest_framework.decorators import api_view, permission_classes, throttle_classes
from user.throttles import LoginThrottle, PortalThrottle, SendEmailThrottle
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.throttling import ScopedRateThrottle
from django.db.utils import IntegrityError
import pytz
from django.contrib.auth.hashers import make_password
from project import hubspot
# @api_view(['POST'])
# @permission_classes([AllowAny])
@throttle_classes([LoginThrottle])
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    # filter_backends = [ParameterFilter]


@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def current_user(request, *args, **kwargs):
    user = request.user
    if not user.is_anonymous:
        serializer = UserSerializer(user)
        return Response(serializer.data)
    else:
        raise APIException("User should be authenticated!")


@api_view(['POST'])
@permission_classes([IsAdminUser])
def change_logged_user(request, *args, **kwargs):
    data = request.data
    user_id = data.get('user_id')
    if user_id is None:
        raise APIException('You should pass user id!')

    user = User.objects.filter(id=user_id).first()
    if user is None:
        raise APIException('User not found!')

    tokens = get_tokens_for_user(user)
    return Response(tokens)


@api_view(['POST'])
@permission_classes([AllowAny])
@transaction.atomic()
@throttle_classes([LoginThrottle])
def register(request, *args, **kwargs):
    with transaction.atomic():
        try:
            data = request.data
            if 'name' in data and 'email' in data and 'password' in data and 'repassword' in data and 'lastname' in data:
                email = data.get('email')
                password = data.get('password')
                name = data.get('first_name')
                lastname = data.get('last_name')
                repassword = data.get('repassword')
                result = {'code': 2, 'msg': 'Saved.'}
                if User.objects.filter(email=email).exists():
                    raise APIException("Email already in use.")
                if password != repassword:
                    raise APIException("Password is not valid")
                user_code = random.randint(100000, 999999)
                if utils.send_otp(email, user_code,name,lastname):
                    user = User.objects.create_user(
                        email=email,
                        # password=password,
                        **{'role': 1, 'first_name': name, 'last_name': lastname, 'password': password, 'user_code': user_code}

                    )
                    return Response(result)
                else:
                    raise APIException("An error occurred")

            raise APIException("Please fill all fields")
        except IntegrityError as e:
            raise APIException("Company name already in use.")
        except Exception as e:
            raise APIException(e)


@api_view(['POST'])
@permission_classes([AllowAny])
def get_otp_login_url(request, *args, **kwargs):
    data = request.data
    email = data.get('email')
    password = data.get('password')
    if email is None or password is None:
        raise APIException("Should pass email and password!")

    user = User.objects.filter(email=email).first()
    if user is None or not user.check_password(password):
        raise APIException("Provided credentials are not valid")

    # _uri = pyotp.totp.TOTP(user.mfa_hash).provisioning_uri(name=email, issuer_name='MSSP')
    data = {
        # 'otp_url': settings.OTP_URL_HEAD + _uri
    }
    return Response(data)


@api_view(['POST'])
@permission_classes([AllowAny])
def check_otp(request, *args, **kwargs):
    data = request.data
    otp_code = data.get('otp_code')
    email = data.get('email')
    if otp_code is None or email is None:
        raise APIException("You should pass otp code")
    user = User.objects.filter(email=email).first()
    if user is None:
        raise APIException("User not found.")
    if user.user_code == otp_code and (
            datetime.utcnow().replace(tzinfo=pytz.utc) - user.user_code_time).total_seconds() < settings.USER_OTP_SECONDS:
        user.is_valid = True
        hubspot.create_contact(first_name=user.first_name, last_name=user.last_name, email=email)
        user.is_send_crm = True
        user.save()

        # try:
        #     send_register_email(user)
        #     return Response({'result': "Token created"})
        # except Exception as e:
        #     raise APIException(e)

        return Response({'code': 1, 'msg': 'OTP Code is valid'})
    else:
        raise APIException("OTP Code is not valid!")


@api_view(['POST'])
@permission_classes([AllowAny])
def send_otp(request, *args, **kwargs):
    data = request.data
    email = data.get('email')
    user = User.objects.filter(email=email).first()
    if user is None:
        raise APIException("User not found.")
    user_code = random.randint(100000, 999999)
    if utils.send_otp(email, user_code,user.first_name,user.last_name):
        user.user_code = user_code
        user.user_code_time = datetime.now()
        user.save()
        return Response({'code': 1, 'msg': 'OTP code send'})
    else:
        raise APIException("OTP code not send.")






@api_view(['POST'])
@permission_classes([AllowAny])
@throttle_classes([SendEmailThrottle])
def send_reset_link(request, *args, **kwargs):
    data = request.data
    email = data.get('email')
    if email is None:
        raise APIException('You should pass email for reset password.')

    user = User.objects.filter(email=email).first()
    if user is None:
        raise APIException('Not found user with specified email address.')

    try:
        user_code = random.randint(100000, 999999)
        if utils.send_password_reset_email(email, user_code, user.first_name, user.last_name):
            user.user_code = user_code
            user.user_code_time = datetime.now()
            user.save()
        return Response({'result': "Token created"})
    except Exception as e:
        raise APIException(e)


@api_view(['POST'])
@permission_classes([AllowAny])
@throttle_classes([SendEmailThrottle])
def check_token(request, *args, **kwargs):
    data = request.data
    token = data.get('token')
    if token is None:
        raise APIException("You should pass a token for validation!")

    token = Token.objects.filter(key=token).first()

    if token is None:
        raise APIException("Token is not valid")
    else:
        return Response({'detail': 'Token is valid.'})


@api_view(['POST'])
@permission_classes([AllowAny])
@throttle_classes([SendEmailThrottle])
def set_password_with_token(request, *args, **kwargs):
    data = request.data
    token = data.get('token')
    email = data.get('email')
    password = data.get('password')
    repassword = data.get('passwordConfirm')
    if token is None or password is None or repassword is None:
        raise APIException("You should pass a token and a password for validation!")

    if password != repassword:
        raise APIException("Password is not valid")

    user = User.objects.filter(email=email).first()
    if user is None:
        raise APIException("User not found.")
    if user.user_code == token and (
            datetime.utcnow().replace(tzinfo=pytz.utc) - user.user_code_time).total_seconds() < settings.USER_OTP_SECONDS:
        user.is_valid = True
        user.password=make_password(password)
        user.save()
        return Response({'code': 1, 'msg': 'OTP Code is valid'})
    else:
        raise APIException("OTP Code is not valid!")


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@throttle_classes([PortalThrottle])
def set_password(request, *args, **kwargs):
    data = request.data
    req_user = request.user
    password = data.get('password')
    repassword = data.get('passwordConfirm')
    if password == repassword:
        user = User.objects.filter(id=req_user.id).first()
        user.password = make_password(password)
        user.save()
        return Response({'detail': 'Password Changed'})
    else:
        raise APIException("Password is not correct")


@api_view(['POST'])
@permission_classes([IsAdminUser])
@throttle_classes([PortalThrottle])
def set_user_password(request, *args, **kwargs):
    data = request.data
    req_user = data['user_id']
    password = data.get('password')
    repassword = data.get('passwordConfirm')
    if password == repassword:
        user = User.objects.filter(id=req_user).first()
        user.password = make_password(password)
        user.save()
        return Response({'detail': 'Password Changed'})
    else:
        raise APIException("Password is not correct")


class UserViewSet(BaseViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    read_serializer_class = UserDetailSerializer
    # permission_classes = (IsAdminUser,)
    search_fields = ['first_name', 'last_name', 'email', 'contractor__name', 'telephone']
    ordering_fields = ['first_name', 'last_name', 'email', 'telephone']
    filterset_fields = ['id', 'contractor_id']
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'portal'


class CustomerViewSet(BaseViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    read_serializer_class = CustomerDetailSerializer
    # permission_classes = (IsAdminUser,)
    search_fields = ['name', 'email', 'address', 'phone']
    ordering_fields = ['name', 'email', 'address', 'phone']
    filterset_fields = ['id', 'is_customer']
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'portal'


class ContractorViewSet(BaseViewSet):
    queryset = Contractor.objects.all()
    serializer_class = ContractorSerializer
    # read_serializer_class = CustomerDetailSerializer
    permission_classes = (IsAdminUser,)
    search_fields = ['name', 'email', 'address', 'phone']
    ordering_fields = ['name', 'email', 'address', 'phone']
    filterset_fields = ['id']
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'portal'


class ParameterViewSet(BaseViewSet):
    queryset = Parameter.objects.all()
    serializer_class = ParameterSerializer
    read_serializer_class = ParameterDetailSerializer
    filter_backends = [ParameterFilter]
    ordering_fields = ['name', 'parameter_group__display_name']
    search_fields = ['name', 'parameter_group__display_name']
    filterset_fields = ['parameter_group__name']


class ParameterGroupViewSet(BaseViewSet):
    queryset = ParameterGroup.objects.all().order_by('-display_name')
    serializer_class = ParameterGroupSerializer
