"""
Django settings for samplesite project.

Generated by 'django-admin startproject' using Django 3.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ''

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = 

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'widget_tweaks',
    'crud',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

# STATIC_URL = '/static/'

LOGIN_URL = '/login/'

LOGIN_REDIRECT_URL = 'home'

# STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static", "static")

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'



STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = "/static/"

# ldap authentication
import logging
import ldap
from django_auth_ldap.config import LDAPSearch, LDAPGroupQuery,GroupOfNamesType,PosixGroupType

AUTH_LDAP_SERVER_URI = 'ldap://localhost:10389/' 
print("Hey")
AUTH_LDAP_BIND_DN = 'cn=admin,dc=planetexpress,dc=com'
AUTH_LDAP_BIND_PASSWORD = 'GoodNewsEveryone'
AUTH_LDAP_USER_SEARCH = LDAPSearch('dc=planetexpress,dc=com',ldap.SCOPE_SUBTREE, '(uid=%(user)s)')
AUTH_LDAP_GROUP_SEARCH = LDAPSearch('dc=planetexpress,dc=com',ldap.SCOPE_SUBTREE, '(objectClass=top)')
AUTH_LDAP_GROUP_TYPE = GroupOfNamesType(name_attr="cn")
AUTH_LDAP_MIRROR_GROUPS = True

    # Populate the Django user from the LDAP directory.
AUTH_LDAP_REQUIRE_GROUP = "cn=enabled,ou=groups,dc=planetexpress,dc=com"

AUTH_LDAP_USER_ATTR_MAP = {
        "first_name": "givenName",
        "last_name": "sn",
        "email": "mail",
        "username": "uid",
        "password": "userPassword",
}
AUTH_LDAP_PROFILE_ATTR_MAP = {
        "home_directory": "homeDirectory"
}
AUTH_LDAP_USER_FLAGS_BY_GROUP = {
        "is_active": "cn=active,ou=groups,dc=planetexpress,dc=com",
        "is_staff": "cn=staff,ou=groups,dc=planetexpress,dc=com",
        "is_superuser": "cn=superuser,ou=groups,dc=planetexpress,dc=com",
        "is_admin": "cn=admin,ou=groups,dc=planetexpress,dc=com"
}
    
AUTH_LDAP_ALWAYS_UPDATE_USER = True
AUTH_LDAP_FIND_GROUP_PERMS = True
AUTH_LDAP_CACHE_TIMEOUT = 3600
    
AUTH_LDAP_FIND_GROUP_PERMS = True
    
    # Keep ModelBackend around for per-user permissions and maybe a local
    # superuser.
AUTHENTICATION_BACKENDS = (
        'django_auth_ldap.backend.LDAPBackend',
        'django.contrib.auth.backends.ModelBackend',
)

# - - - - LDAP CONFIGURATION - - - - #
#
# Importing ldap libraries and applications
# import ldap
# import logging
# from django_auth_ldap.config import LDAPSearch, GroupOfNamesType, PosixGroupType

# # ...connecting to ldap server (local environment uses IP)
# AUTH_LDAP_SERVER_URI = 'ldap://172.22.63.55:389' 

# # ...account to enter into ldap server (anonymous is not always allowed)
# AUTH_LDAP_BIND_DN = "cn=admin,dc=xl,dc=com"
# AUTH_LDAP_BIND_PASSWORD = "password"

# # ...path where to start to search groups
# AUTH_LDAP_GROUP_SEARCH = LDAPSearch("ou=groups,dc=xl,dc=com",
#                                     ldap.SCOPE_SUBTREE, # allow searching from current node to all nodes below
#                                     "(objectClass=posixGroup)" # type of object
# )
# AUTH_LDAP_GROUP_TYPE = PosixGroupType() # a posixGroup is identified by the keyword "cn" into ldap server

# # ...associations between ldap and django groups
# AUTH_LDAP_USER_FLAGS_BY_GROUP = {
#     "is_active": "cn=active,ou=groups,dc=xl,dc=com",
#     "is_staff": "cn=staff,ou=groups,dc=xl,dc=com",
#     "is_superuser": "cn=superuser,ou=groups,dc=xl,dc=com"
# }
# AUTH_LDAP_PROFILE_FLAGS_BY_GROUPS = {
#     "is_awesome": ["cn=enabled,ou=groups,dc=xl,dc=com"]
# }


# # ...node where to start to search users
# AUTH_LDAP_USER_SEARCH = LDAPSearch("ou=users,dc=xl,dc=com",
#                                    ldap.SCOPE_SUBTREE, # allow searching from current node to all nodes below
#                                    "(cn=%(user)s)"
#                                    #"(objectClass=posixAccount)"
#                                    #"(objectClass=inetOrgPerson)"
# )
# # Keep ModelBackend around for per-user permissions and maybe a local
# # superuser.
# AUTHENTICATION_BACKENDS = (
#     'django_auth_ldap.backend.LDAPBackend',
#     'django.contrib.auth.backends.ModelBackend',
# )

# # Enable debug for ldap server connection
logger = logging.getLogger('django_auth_ldap')
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)
