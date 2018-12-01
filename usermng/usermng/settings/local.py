from .base import *

DEBUG = True

if DEBUG:
	import logging
	#logging.basicConfig()

DATABASES = {
	'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'usermng',
        'USER': 'fingeruser',
        'PASSWORD': '',
        'HOST':'va.fyping.cn',
        'PORT': '5444',
		'CONN_MAX_AGE': None,
        'OPTIONS': {
            'client_encoding': 'UTF-8'
        }
    }
}


ALLOWED_HOSTS = ['*']