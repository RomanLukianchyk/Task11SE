import os
from pathlib import Path
import cloudinary


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-_h%e$jhyg0=t&gp39@)d_z#g2cc2g5sxkjs+y*%tu4hk@kh1$v'
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1']

LOGIN_REDIRECT_URL = '/blog/feed/'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

CONFIRMATION_URL = 'localhost/registration/confirm'
SITE_URL = 'localhost'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'accounts',
    'task11SE',
    'registration',
    'cloudinary',
    'cloudinary_storage',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'task11SE.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'task11SE.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'socialeducation',
        'USER': 'admin',
        'PASSWORD': 'arrowqwe26',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

cloudinary.config(
  cloud_name = "dkyeh8rik",
  api_key = "164698517151334",
  api_secret = "j_XYqJ0MrNLmwoxnzlMu1EIlV20"
)

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'


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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
    BASE_DIR / "frontend",
]
STATIC_ROOT = BASE_DIR / 'staticfiles'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = '19arrow19@gmail.com'
EMAIL_HOST_PASSWORD = 'rzbm jxtz rwof cvgb'
DEFAULT_FROM_EMAIL = '19arrow19@gmail.com'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
