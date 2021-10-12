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
SECRET_KEY = "&1#@dafxuuykfjwb-#h3l*in85)fi_1jc9talkve7p)yvahc@r"

# We'll set DEBUG = True below when we're in the dev environment.
DEBUG = False

ALLOWED_HOSTS = []


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
# SESSION_EXPIRE_AT_BROWSER_CLOSE = True


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


LOGIN_URL = "/polls/login"
LOGIN_REDIRECT_URL = "/polls/hostTable"

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
    DEBUG = True
