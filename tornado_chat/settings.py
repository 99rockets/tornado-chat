import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = 'r(73!vpm36^a8*ryfw*jyklvc8mjt_+xc0ny29oj3yb_8ti#)v'

DEBUG = True

TEMPLATE_DEBUG = DEBUG

SESSION_ENGINE = 'redis_sessions.session'

API_KEY = '$0m3-U/\/1qu3-K3Y'

SEND_MESSAGE_API_URL = 'http://127.0.0.1:8000/messages/send_message_api'

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'chat',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'tornado_chat.urls'

WSGI_APPLICATION = 'tornado_chat.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "_static"),
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "templates"),
)

try:
    from local_settings import *
except ImportError:
    pass
