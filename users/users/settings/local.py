from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_secret("DB_NAME"),
        'USER': get_secret("USER"),
        'PASSWORD': get_secret("PASSWORD"),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

DEBUG = True

ALLOWED_HOSTS = []

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child("static")]
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child("media")