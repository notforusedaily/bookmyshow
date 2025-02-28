"""
Django settings for bookmyseat project.

Generated by 'django-admin startproject' using Django 5.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os
import dj_database_url
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-c8aetlj(=vp90n@#yoc^&d(_6ivp(d!bv-4-f!r$lawptjzrwu'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#ALLOWED_HOSTS = []
ALLOWED_HOSTS = [".vercel.app"]


# Application definition ->".vercel.app

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
    'movies',
    'channels',
    'whitenoise.runserver_nostatic',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', 
      
]

AUTH_USER_MODEL='auth.User'
EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


ROOT_URLCONF = 'bookmyseat.urls'
LOGIN_URL='/login/'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'bookmyseat.wsgi.application'
ASGI_APPLICATION = 'bookmyseat.asgi.application'

# CHANNEL_LAYERS = {
#     'default': {
#         'BACKEND': 'channels_redis.core.RedisChannelLayer',
#         'CONFIG': {
#             "hosts": f"redis-15594.c267.us-east-1-4.ec2.redns.redis-cloud.com:15594"
# #[('127.0.0.1', 6379)],
#             # Redis default host and port
#         },
#     },
# }

# CHANNEL_LAYERS = {
#     'default': {
#         'BACKEND': 'channels_redis.core.RedisChannelLayer',
#         'CONFIG': {
#             "hosts": [(os.getenv('REDIS_URL'), 15594)],
#             "password": os.getenv('REDIS_PASSWORD')
#         },
#     },
# }
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [
                {
                    "host": "redis-11548.crce179.ap-south-1-1.ec2.redns.redis-cloud.com",
                    "port": 11548,
                    "username": "default",  # Optional, depending on Redis setup
                    "password": "bsI5Pzt7UPsVAZbRjxNclmOkSz2KGB4t",
                }
            ],
        },
    },
}

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
DATABASES['default'] = dj_database_url.parse('postgresql://nullclassintern_etg2_user:Or8UYPGzEzHMOqJj46zVtt2FTD9RMctb@dpg-cv0ugu2n91rc73anm83g-a.oregon-postgres.render.com/nullclassintern_etg2')
# postgresql://django_bookmyshow_nqpy_user:tFMIlzSh323Jsrz5J7POb5QPqeHnlHd1@dpg-ctdh71d2ng1s73d6j13g-a.oregon-postgres.render.com/django_bookmyshow_nqpy

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'kalihacker20042003@gmail.com'
EMAIL_HOST_PASSWORD ='zotf vskk lhqn keqb'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


# Static files settings
STATIC_URL = '/static/'

# Directory where collectstatic command collects static files
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Additional directories where Django will look for static files
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]


DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
