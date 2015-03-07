from auditor.auditor.settings import *


##########################################################################
#
# Server settings
#
##########################################################################
ALLOWED_HOSTS = ["localhost"]

WSGI_APPLICATION = 'auditor.auditor.wsgi_production.application'


##########################################################################
#
# Database settings
#
##########################################################################
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(VAR_DIR, 'db', 'production_db.sqlite3'),
    }
}
