"""
Django settings for auditor project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

import os


# Determine some important file locations
SETTINGS_DIR = os.path.dirname(__file__)
BASE_DIR = os.path.dirname(SETTINGS_DIR)
BUILDOUT_DIR = os.path.dirname(BASE_DIR)
VAR_DIR = os.path.join(BUILDOUT_DIR, "var")


##########################################################################
#
# Secret settings
#
##########################################################################
# If a secret_settings file isn't defined, open a new one and save a
# SECRET_KEY in it. Then import it. All passwords and other secret
# settings should be stored in secret_settings.py. NOT in settings.py
try:
    from secret_settings import *
except ImportError:
    print "Couldn't find secret_settings file. Creating a new one."
    secret_settings_loc = os.path.join(SETTINGS_DIR, "secret_settings.py")
    with open(secret_settings_loc, 'w') as secret_settings:
        secret_key = ''.join([chr(ord(x) % 90 + 33) for x in os.urandom(40)])
        secret_settings.write("SECRET_KEY = '''%s'''\n" % secret_key)
    from secret_settings import *


##########################################################################
#
# Application Definition
#
##########################################################################
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'auditor.attendance',
    'auditor.audit',
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

ROOT_URLCONF = 'auditor.auditor.urls'


##########################################################################
#
# Database settings
#
##########################################################################

# The database should *not* be set in this file. It should be set in
# development.py or production.py instead.
DATABASES = None


##########################################################################
#
# Internationalization settings
#
##########################################################################
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


##########################################################################
#
# Static files settings
#
##########################################################################
STATIC_URL = '/static/'
