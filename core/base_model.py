from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.db import models, transaction

from core.utils import generate_pk


class BaseModel(models.Model):
    id = models.CharField(primary_key=True, max_length=255, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    operation_user = models.CharField(max_length=300, null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            id_prefix = getattr(self, "id_prefix")
            if id_prefix is not None:
                setattr(self, 'id', generate_pk(self.id_prefix))
        super(BaseModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class UserManager(BaseUserManager):

    def _create_user(self, email, password, **extra_fields):
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
