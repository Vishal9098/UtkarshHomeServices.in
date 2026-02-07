"""
Django settings for shop project.
"""

from pathlib import Path

# ----------------------
# Base Directory
# ----------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# ----------------------
# Security
# ----------------------
SECRET_KEY = 'django-insecure-&(+lm&$%l7cp@v%z(^n^ozcaz8u%@gy02npi7jmuxi=xg)kcbe'
DEBUG = True  # Production me False karna
ALLOWED_HOSTS = ['*']

# ----------------------
# Installed Apps
# ----------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'shop', 
    'app.apps.AppConfig',
]

# ----------------------
# Middleware
# ----------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Static files ke liye
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ----------------------
# URLs & Templates
# ----------------------
ROOT_URLCONF = 'shop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'app.context_processors.cart_count',
                 'app.context_processors.all_services',   # 🔥 YE LINE MISS THI
            ],
        },
    },
]

WSGI_APPLICATION = 'shop.wsgi.application'

# ----------------------
# Database
# ----------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ----------------------
# Password Validators
# ----------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# ----------------------
# Internationalization
# ----------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ----------------------
# Static & Media
# ----------------------
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "shop" / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
LOGIN_REDIRECT_URL = '/profile/'
# ----------------------
# Login & Sessions
# ----------------------

SESSION_ENGINE = "django.contrib.sessions.backends.db"




# ----------------------
# Default primary key field type
# ----------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# -------------------------------
# WhatsApp Cloud API Configuration
# -------------------------------

WHATSAPP_TOKEN = "EAAQ608ROhyoBQi0qT4EsBoEJi9LyG0rIwg8W8olLqmgj7ZBiq84W5CKA5a9ZA4Qo5kbbPaG6vwnCjfp7bFTrqnLDxMtsDSTL1AGQtLtyIvlZAiUFPhGsz4GO51vTlOZA30zlJeZCm9cmx5osaEf1Fvak0OV0riz6yQ7xKgrBaJPL2Y7e2ZBvPcLiV2iZCL5pAZDZD"
WHATSAPP_PHONE_NUMBER_ID = "964093766788925"












