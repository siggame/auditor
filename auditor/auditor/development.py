from auditor.auditor.settings import *


##########################################################################
#
# Debug settings
#
##########################################################################
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = DEBUG


##########################################################################
#
# Server settings
#
##########################################################################
ALLOWED_HOSTS = ["localhost"]

WSGI_APPLICATION = 'auditor.auditor.wsgi_development.application'


##########################################################################
#
# Database settings
#
##########################################################################
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(VAR_DIR, 'db', 'dev_db.sqlite3'),
    }
}
