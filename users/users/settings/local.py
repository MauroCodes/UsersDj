from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbuser',
        'USER': 'sidis',
        'PASSWORD': 'sidis',
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