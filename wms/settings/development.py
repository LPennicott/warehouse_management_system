from .base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

DEBUG = True

email_user = os.environ.get('email_user')
email_pass = os.environ.get('email_pass')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
