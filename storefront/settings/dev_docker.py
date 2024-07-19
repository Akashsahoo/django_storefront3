from  .common  import *

DEBUG = True
if DEBUG:
    MIDDLEWARE += ['silk.middleware.SilkyMiddleware']

SECRET_KEY = 'django-insecure-hs6j037urx6iav+7#10%-vu4l4f5@@-1_zo)oft4g7$vf2$jmp'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'storefront3',
        'HOST': 'mysql',
        'USER': 'root',
        'PASSWORD': 'MYPASSWORD',
        'PORT':'3306',
        'OPTIONS': {  
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"  
        }  
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp4dev'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 2525
DEFAULT_FROM_EMAIL = ''

ADMINS = [
    ('Mosh','admin@moshbuy.com')
]

CELERY_BROKER_URL = 'redis://redis:6379/1'

CELERY_BEAT_SCHEDULE = {
    'notify_customers': {
        'task' : 'playground.tasks.notify_customers',
        'schedule': 5,             #crontab(day_of_week=1,hour=7,minute=30)
        'args' : ['Hello World'],
        
    }
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis:6379/2",
        "TIMEOUT": 10*60 ,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}


DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda request : True
}