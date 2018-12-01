from .base import *

DEBUG = False

if DEBUG:
	import logging
	#logging.basicConfig()

DATABASES = {
	'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'usermng',
        'USER': '',
        'PASSWORD': '',
        'HOST':'va.fyping.cn',
        'PORT': '',
		'CONN_MAX_AGE': None,
        'OPTIONS': {
            'client_encoding': 'UTF-8'
        }
    }
}


ALLOWED_HOSTS = ['*']