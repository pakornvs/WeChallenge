from backend.settings.base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "7mbupsea)ell8@vprm)543ofaxa-z&k4tci!jrr^=ybu5p*db9"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgres",
        "USER": "postgres",
        "HOST": "postgres",
        "PASSWORD": "LocalPassword",
    }
}


# Django Q
# https://django-q.readthedocs.io/en/latest/configure.html

Q_CLUSTER = {
    "name": "wechallenge",
    "workers": 4,
    "redis": {"host": "redis"},
}
