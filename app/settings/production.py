import json
from .base import *
from django.core.exceptions import ImproperlyConfigured

DEBUG = False

secret_file = os.path.join(BASE_DIR, 'secret.json')

with open(secret_file, 'r') as f:
    secret = json.loads(f.read())

def get_secret(setting, secret=secret):
    try:
        return secret[setting]
    except:
        msg = "Set key '{0}' in secret.json".format(setting)
        raise ImproperlyConfigured(error_msg)



#SECRET_KEY = 'lrc-ek4#y0bxge^dj^8vrp0mb6^5m+!2koz$gj1=d#chb#e@52'
SECRET_KEY = get_secret('SECRET_KEY')

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
