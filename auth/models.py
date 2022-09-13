from __future__ import unicode_literals

#
from django.contrib.auth.hashers import make_password
from django.utils import timezone
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models, transaction

from bunguo.utils import generate_pk
from bunguo.base_model import BaseModel


class UserManager(BaseUserManager):

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email,and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        try:
            with transaction.atomic():
                user = self.model(email=email, **extra_fields)
                user.password = make_password(password)
                user.save(using=self._db)
                return user
        except:
            raise

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', '1')

        return self._create_user(email, password=password, **extra_fields)


class user_gender(models.IntegerChoices):
    Male = 1
    Female = 2


class marital_status(models.IntegerChoices):
    Married = 1
    Single = 2


class military_status(models.IntegerChoices):
    Done = 1
    Not_done = 2


class education_status(models.IntegerChoices):
    Okul_oncesi = 1
    Ilk_okul = 2
    Orta_okul = 3
    Ilk_ogretim = 4
    Lise = 5
    On_lisans = 6
    Lisans = 7
    Yuksek_lisans = 8
    Doktora = 9
    Bilinmeyen = 10


class customer_type(models.IntegerChoices):
    Tuzel_kisi = 1
    Gercek_kisi = 2


class ParameterGroup(BaseModel):
    name = models.CharField(max_length=500, unique=True)
    display_name = models.CharField(max_length=500, blank=True, null=True)
    display_name_tr = models.CharField(max_length=500, unique=True, blank=True, null=True)
    display_name_en = models.CharField(max_length=500, unique=True, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    id_prefix = "PRG"

    class Meta:
        db_table = "parameter_group"


class Parameter(BaseModel):
    name = models.CharField(max_length=250)
    code = models.IntegerField(blank=True, null=True)
    display_name_tr = models.CharField(max_length=500, blank=True, null=True)
    display_name_en = models.CharField(max_length=500, blank=True, null=True)
    description_tr = models.TextField(blank=True, null=True)
    description_en = models.TextField(blank=True, null=True)
    # text_color = models.CharField(max_length=250, blank=True, null=True)
    # bg_color = models.CharField(max_length=250, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    parameter_group = models.ForeignKey(ParameterGroup, on_delete=models.CASCADE, related_name='parameter')
    id_prefix = "PRM"

    class Meta:
        db_table = 'parameters'
        ordering = ['name']


class Contractor(BaseModel):
    name = models.CharField(max_length=500, unique=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    domain = models.CharField(max_length=200, blank=True, null=True)
    telephone = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    expire_date = models.DateField(blank=False, null=True)
    id_prefix = "PRV"

    @property
    def user_count(self):
        return User.objects.filter(contractor_id=self.id, is_active=True).count()

    class Meta:
        db_table = "contractors"


class Customer(BaseModel):
    name = models.CharField(max_length=250)
    short_name = models.CharField(max_length=250, blank=True, null=True)
    # category = models.ForeignKey(Parameter, on_delete=models.SET_NULL, blank=True, null=True, related_name='parameter')
    contractor = models.ForeignKey(Contractor, on_delete=models.SET_NULL, blank=True, null=True,
                                   related_name='customer')
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=250, blank=True, null=True)
    fax = models.CharField(max_length=250, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    delivery_address = models.TextField(blank=True, null=True)
    vkn_tckn = models.CharField(max_length=250, blank=True, null=True)
    tax_office = models.CharField(max_length=250, blank=True, null=True)
    code = models.CharField(max_length=250, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_tax_free = models.BooleanField(default=False)
    bank_information = models.TextField(blank=True, null=True)
    currency_unit = models.ForeignKey(Parameter, on_delete=models.DO_NOTHING, related_name='currency')
    starting_balance = models.FloatField(blank=True, null=True)
    due_date_day = models.IntegerField(blank=True, null=True)
    discount_percent = models.FloatField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    is_customer = models.BooleanField(default=True)  # tedarikçi yada customer
    # type = models.IntegerField(choices=customer_type.choices, default=1)
    id_prefix = "CUS"

    class Meta:
        db_table = "customers"


def avatar_directory_path(instance, filename):
    return 'avatar_files/{0}/{1}'.format(instance.id, filename)


class User(AbstractBaseUser, PermissionsMixin):
    id = models.CharField(primary_key=True, max_length=255, editable=False)
    email = models.EmailField(max_length=99, unique=True)
    first_name = models.CharField(max_length=99, blank=True)
    last_name = models.CharField(max_length=99, blank=True)
    is_active = models.BooleanField(default=True)
    is_valid = models.BooleanField(default=False)
    user_code = models.CharField(max_length=99, blank=True)
    user_code_time = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_send_crm = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    role = models.IntegerField(default=1)  # 1 Öğrenci
    contractor = models.ForeignKey(Contractor, on_delete=models.SET_NULL, blank=True, null=True,
                                   related_name='user_contractor')
    avatar = models.FileField(upload_to=avatar_directory_path, blank=True, null=True)
    telephone = models.CharField(max_length=50, blank=True, null=True)
    # mfa_hash = models.CharField(max_length=50, null=True)
    operation_user = models.CharField(max_length=300, null=True)

    objects = UserManager()
    id_prefix = "USR"
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    class Meta:
        db_table = "users"
        ordering = ['-id', 'contractor']

    def get_roles(self):
        import math
        result = []
        if self.role is not None:
            arr = bin(self.role)[2:]
            length = len(arr)
            for i, ar in enumerate(arr):
                if ar == '1':
                    result.append(int(math.pow(2, (length - 1 - i))))
        return result

    def generate_token(self):
        link_token, created = Token.objects.get_or_create(user=self)
        return link_token.key

    def save(self, *args, **kwargs):
        if not self.id:
            id_prefix = getattr(self, "id_prefix")
            if id_prefix is not None:
                setattr(self, 'id', generate_pk(self.id_prefix))
            # self.mfa_hash = pyotp.random_base32()
        super(User, self).save(*args, **kwargs)
        return self
