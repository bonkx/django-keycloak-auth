"""
Django settings for dash project.

Generated by 'django-admin startproject' using Django 3.2.15.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from pathlib import Path

import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(override=True)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'kzr7202=a#4qd$g3z_v0v1$n*#1f5rv@moc%tq@yf+we2t)^#g'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'mozilla_django_oidc',  # Load after auth
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',

    'api',
    'web',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'login_required.middleware.LoginRequiredMiddleware',  # New
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'mozilla_django_oidc.middleware.SessionRefresh',
]

LOGIN_REQUIRED_IGNORE_PATHS = [
    # r'/accounts/logout/$',
    r'/login/$',
    r'/admin(.*)$',
    r'/oidc(.*)$',
    r'/api(.*)$',
]

AUTHENTICATION_BACKENDS = [
    'dash.auth_backends.KeycloakOIDCAuthenticationBackend',
    # 'mozilla_django_oidc.auth.OIDCAuthenticationBackend',
    'django.contrib.auth.backends.ModelBackend',
]

ROOT_URLCONF = 'dash.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'web/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'dash.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
        # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'mozilla_django_oidc.contrib.drf.OIDCAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PAGINATION_CLASS': 'api.paginations.CustomPagination',
    'PAGE_SIZE': 10,
    'MAX_PAGINATE_BY': 100
}


#################### KEYCLOAK CONFIG ####################

"""
manually set the OIDC backend DRF to basic OIDCAuthenticationBackend,
because AUTHENTICATION_BACKENDS using custom KeycloakOIDCAuthenticationBackend
"""
OIDC_DRF_AUTH_BACKEND = 'mozilla_django_oidc.auth.OIDCAuthenticationBackend'


def discover_oidc(discovery_url: str) -> dict:
    """
    Performs OpenID Connect discovery to retrieve the provider configuration.
    """
    response = requests.get(discovery_url)
    # response = requests.get(discovery_url, verify=False)
    if response.status_code != 200:
        raise ValueError("Failed to retrieve provider configuration.")

    provider_config = response.json()

    # Extract endpoint URLs from provider configuration
    return {
        "authorization_endpoint": provider_config["authorization_endpoint"],
        "token_endpoint": provider_config["token_endpoint"],
        "userinfo_endpoint": provider_config["userinfo_endpoint"],
        "end_session_endpoint": provider_config["end_session_endpoint"],
        "jwks_uri": provider_config["jwks_uri"],
    }


# OpenID connect configuration
KC_BASE_URI = os.environ.get('KC_BASE_URI', 'http://localhost:8080')
KC_ADMIN_USER = os.environ.get('KC_ADMIN_USER', 'admin')
KC_ADMIN_PASS = os.environ.get('KC_ADMIN_PASS', 'admin')
KC_REALM = os.environ.get('KC_REALM', 'test')
OIDC_RP_CLIENT_ID = os.environ.get('KC_CLIENT_ID', 'test')
OIDC_RP_CLIENT_SECRET = os.environ.get('KC_CLIENT_SECRET', 'super_scret')

OIDC_OP_BASE_URL = "%s/realms/%s" % (KC_BASE_URI, KC_REALM)

OIDC_OP_DISCOVERY_ENDPOINT = "%s/.well-known/openid-configuration" % (
    OIDC_OP_BASE_URL)

OIDC_RP_SIGN_ALGO = "RS256"
OIDC_RP_SCOPES = os.environ.get(
    "OIDC_RP_SCOPES", "openid email profile")

LOGIN_URL = "oidc_authentication_init"
LOGIN_REDIRECT_URL = os.environ.get(
    'LOGIN_REDIRECT_URL', 'http://localhost:8000/')

# Discover OpenID Connect endpoints
discovery_info = discover_oidc(OIDC_OP_DISCOVERY_ENDPOINT)
# print(discovery_info)
OIDC_OP_AUTHORIZATION_ENDPOINT = discovery_info["authorization_endpoint"]
# print(OIDC_OP_AUTHORIZATION_ENDPOINT)
OIDC_OP_TOKEN_ENDPOINT = discovery_info["token_endpoint"]
# print(OIDC_OP_TOKEN_ENDPOINT)
OIDC_OP_USER_ENDPOINT = discovery_info["userinfo_endpoint"]
# print(OIDC_OP_USER_ENDPOINT)
OIDC_OP_JWKS_ENDPOINT = discovery_info["jwks_uri"]
# print(OIDC_OP_JWKS_ENDPOINT)
OIDC_OP_LOGOUT_ENDPOINT = discovery_info["end_session_endpoint"]
# print(OIDC_OP_LOGOUT_ENDPOINT)

# quay
# LOGOUT_REDIRECT_URL = "%s?client_id=%s&post_logout_redirect_uri=%s" % (
#     OIDC_OP_LOGOUT_ENDPOINT, OIDC_RP_CLIENT_ID, LOGIN_REDIRECT_URL,)

# ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1056)
# OIDC_VERIFY_SSL = False

# OIDC_STORE_ACCESS_TOKEN = True
# OIDC_STORE_ID_TOKEN = True
ALLOW_LOGOUT_GET_METHOD = True
OIDC_OP_LOGOUT_URL_METHOD = 'dash.utils.keycloak.provider_logout'

#################### END KEYCLOAK CONFIG ####################
