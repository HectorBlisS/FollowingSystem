from .base import *

DEBUG = False

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

ADMINS = (
		('bliss', 'contacto@fixter.org'),
	)

ALLOWED_HOSTS = ["*"]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['DBNAME'],
        'USER': os.environ['DBUSER'],
        'PASSWORD': os.environ['DBPASS']
    }
}

