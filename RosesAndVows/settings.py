"""
Django settings for RosesAndVows project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

SITE_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/RosesAndVows'
BASE_DIR = os.path.dirname(SITE_ROOT)
print(BASE_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5t%$^br^0$+ns4wi%x$-3iq3m_7^jr0-rw^p6kx2jjk^g2ir*c'
# SECRET_KEY = ' '
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = ['192.168.12.39', '127.0.0.1', ]
ALLOWED_HOSTS = ['192.168.12.39', 'localhost', '127.0.0.1', ]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    # 'django.contrib.pillow',

    'Coordinator',
    'Client',
    'Profile',
    'Post',

    'account',
    'pinax_theme_bootstrap',
    'bootstrapform',
    'django_inlinecss',
#     'bootstrap3',
    # 'social_django',

    # 'south',
    'django_private_chat',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'account.middleware.LocaleMiddleware',
    'account.middleware.TimezoneMiddleware',
    'account.middleware.ExpiredPasswordMiddleware',
    # 'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'RosesAndVows.urls'

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

                'account.context_processors.account',
                'pinax_theme_bootstrap.context_processors.theme',

                # 'social_django.context_processors.backends',  # <--
                # 'social_django.context_processors.login_redirect', # <--
            ],
        },
    },
]

WSGI_APPLICATION = 'RosesAndVows.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, "db.sqlite3"),
    #     # 'USER': '',
    #     # 'HOST': '',
    #     # 'PASSWORD': '',
    # }
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'rav',
        'USER': 'root',
        'HOST': 'localhost',
        'PASSWORD': '',
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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

AUTHENTICATION_BACKENDS = (
    # 'social_core.backends.twitter.TwitterOAuth',
    # 'social_core.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
    'account.auth_backends.EmailAuthenticationBackend',

)
# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
#
# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

SITE_ID = 1
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

ACCOUNT_HOOKSET = 'RosesAndVows.hooks.AccountDefaultHookSet'

ACCOUNT_EMAIL_UNIQUE = True
ACCOUNT_EMAIL_CONFIRMATION_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_USER_DISPLAY = lambda user: user.email
ACCOUNT_USE_AUTHENTICATE = True

# ACCOUNT_SIGNUP_REDIRECT_URL = 'welcome'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'madaddadam24@gmail.com'
EMAIL_HOST_PASSWORD = '24madaddadam'
EMAIL_USE_TLS = True
# EMAIL_USE_SSL = False
# EMAIL_TIMEOUT = None
# EMAIL_SSL_KEYFILE = None
# EMAIL_SSL_CERTFILE = None

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

THEME_CONTACT_EMAIL = 'inquiries@rosesandvows.com'

# print(ALLOWED_HOSTS)
# LOGIN_URL = 'account/login/'
# LOGOUT_URL = 'account_logout'
# LOGIN_REDIRECT_URL = 'account/login/'
# AUTH_USER_MODEL = 'Coordinator.MyUser'

DATETIME_FORMAT = "d.m.Y H:i:s"
CHAT_WS_SERVER_HOST = 'localhost'
CHAT_WS_SERVER_PORT = 5002
CHAT_WS_SERVER_PROTOCOL = 'ws'

