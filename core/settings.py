"""
Django settings for bunguo project.

Generated by 'django-admin startproject' using Django 4.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os
import datetime
from decouple import config
import dj_database_url
import whitenoise

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-!6&!!0bcko182ums=vc3_a(@92udn5h%$aw4=7te$f#o(63x3b'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATA_UPLOAD_MAX_MEMORY_SIZE = 524288000

ALLOWED_HOSTS = ['*']
CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]
CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'auto-key',
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'user',
    'project',
    'django_apscheduler',
    'corsheaders',
    'rest_framework.authtoken'
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bunguo.urls'
TEMP_DIR = os.path.join(BASE_DIR, 'templates')
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMP_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
# PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))
# TEMPLATE_DIRS = [
#     os.path.join(PROJECT_PATH, 'templates/'),
# ]

WSGI_APPLICATION = 'bunguo.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.postgresql_psycopg2',
             'NAME': 'bunguo',
             'USER': 'bunguo',
             'PASSWORD': 'Bunguo2022',
             'HOST': "localhost",
             'PORT': '5432',
         },
   # 'default': {
    #    'ENGINE': 'django.db.backends.sqlite3',
     #   'NAME': BASE_DIR / 'db.sqlite3',
    #}
}

# DATABASE_URL = os.environ.get('DATABASE_URL')
# db_from_env = dj_database_url.config(default=DATABASE_URL, conn_max_age=500, ssl_require=True)
# DATABASES['default'].update(db_from_env)


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

# STATICFILES_DIRS = (os.path.join(BASE_DIR, "frontend", "dist", "static"),)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
FIXTURE_DIRS = [os.path.join(BASE_DIR, 'fixtures')]
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        # 'rest_framework.permissions.IsAuthenticated',
        # 'rest_framework.permissions.IsAuthenticatedOrReadOnly',
        'rest_framework.permissions.AllowAny',
        # 'rest_framework.permissions.IsAdminUser',
        'project.permissions.RolePermission'
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),

    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.ScopedRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'login': '10/minute',
        'portal': '150/minute',
        'sendemail': '5/day'
    },
    'PAGE_SIZE': 10
}
PAGE_SIZE = 10
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(hours=8),
}

AUTH_USER_MODEL = "user.User"

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
MAX_ROWS_PER_PAGE = 1000

# Email
# DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL')
# EMAIL_SERVER_NAME = config('EMAIL_SERVER_NAME')
# EMAIL_SERVER_PORT = config('EMAIL_SERVER_PORT')
# EMAIL_HOST = config('EMAIL_HOST')
# EMAIL_PORT = config('EMAIL_PORT')
# EMAIL_HOST_USER = config('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
# # EMAIL_HOST_PASSWORD = '0frDt63Q'
# EMAIL_USE_TLS = config('EMAIL_USE_TLS')


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'welcome@bunguo.com'
EMAIL_HOST_PASSWORD = 'nvlwjkyqsaofzucx'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'Bunguo'

USER_OTP_SECONDS = 240
