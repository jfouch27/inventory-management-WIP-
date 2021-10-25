import os
from socket import gethostname
from pathlib import Path

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")

if "upenn-prod-server" in gethostname():
    os.environ["DJENV"] = "prod"
elif "upenn-stage-server" in gethostname():
    os.environ["DJENV"] = "stage"

DJENV = os.environ.get("DJENV", "dev")

# SECURITY WARNING: keep the secret key used in production secret!
with open('/usr/local/upenn/etc/inventory') as f:
    SECRET_KEY = f.read().strip()


# We'll set DEBUG = True below when we're in the dev environment.
DEBUG = False

MAILER_LIST = ['jfouch@isc.upenn.edu']
ADMINS = [('jfouch','jfouch@isc.upenn.edu')]
ALLOWED_HOSTS = ["probe.security.isc.upenn.edu"]
#Logging, mind need more work
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/path/to/django/debug.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
#First draft of logging, seems more comprehensive so might have to be revisited
#LOGGING = {
#    'version': 1,
#    'disable_existing_loggers': False,
#    'formatters': {
#        'verbose': {
#            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
#            'style': '{',
#        },
#        'simple': {
#            'format': '{levelname} {message}',
#            'style': '{',
#        },
#    },
#    'filters': {
#        'special': {
#            '()': 'project.logging.SpecialFilter',
#            'foo': 'bar',
#        },
#        'require_debug_true': {
#            '()': 'django.utils.log.RequireDebugTrue',
#        },
#    },
 #   'handlers': {
 #       'console': {
 #           'level': 'INFO',
#            'filters': ['require_debug_true'],
#            'class': 'logging.StreamHandler',
#            'formatter': 'simple'
#        },
#        'mail_admins': {
#            'level': 'ERROR',
#            'class': 'django.utils.log.AdminEmailHandler',
#            'filters': ['special']
#        }
#    },
#    'loggers': {
##        'django': {
#            'handlers': ['console'],
#            'propagate': True,
#        },
#        'django.request': {
#            'handlers': ['mail_admins'],
#            'level': 'ERROR',
#            'propagate': False,
#        },
#        'myproject.custom': {
#            'handlers': ['console', 'mail_admins'],
#            'level': 'INFO',
#            'filters': ['special']
 #       }
 #   }
#}
# Application definition

CONTRIB_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

PROJECT_APPS = [
    "users.apps.UsersConfig",
    "hosts.apps.HostsConfig",
]

INSTALLED_APPS = CONTRIB_APPS + PROJECT_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

SAML_SESSION_COOKIE_NAME = "saml_session"
SESSION_COOKIE_SECURE = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True
X_FRAME_OPTIONS = 'DENY'
SECURE_HSTS_PRELOAD = True
ROOT_URLCONF = "config.urls"


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"
# LOGIN_URL = '/saml2/login/'
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SECURE_HSTS_SECONDS = 180
SECURE_CONTENT_TYPE_NOSNIFF = True

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}


# User Settings

AUTH_USER_MODEL = "users.User"

AUTHENTICATION_BACKENDS = (("django.contrib.auth.backends.ModelBackend"),)

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/


LOGIN_URL = "/hosts/login"
LOGIN_REDIRECT_URL = "/hosts/hostTable.html"

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

DATETIME_FORMAT = "%y-%m-%d %H:%M:%S"

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = "/static/"

# If we're in development, let's add a few more things and set DEBUG = True
if DJENV == "dev":
    INSTALLED_APPS += [
        "django_extensions",
    ]
    DEBUG = False
