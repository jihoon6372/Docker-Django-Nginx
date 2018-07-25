from .base import *

DEBUG = True

SECRET_KEY = 'lrc-ek4#y0bxge^dj^8vrp0mb6^5m+!2koz$gj1=d#chb#e@52'

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
