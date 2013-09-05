from .base import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

BODY_CLASS = 'staging'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '{{ project_name }}_staging',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
