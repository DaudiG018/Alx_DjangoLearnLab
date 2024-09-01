"""
Django settings for LibraryProject project.

Generated by 'django-admin startproject' using Django 5.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-4nd3jthhe3-mun&80qsf*$wo0w92w(z@c_n_q0i7=akn!$pfg&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'csp',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'csp.middleware.CSPMiddleware',
]

ROOT_URLCONF = 'LibraryProject.urls'

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
                'AbstractUser',
                ]
        },
    },
]

WSGI_APPLICATION = 'LibraryProject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'your_app.CustomUser'

DEBUG = False
# Add additional browser-side protections
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'  # Protect against clickjacking
SECURE_CONTENT_TYPE_NOSNIFF = True  # Prevent browsers from MIME-sniffing

# Cookies should only be sent over HTTPS
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

SECURE_SSL_REDIRECT = True

# HSTS setting: instructs browsers to only access your site via HTTPS for the specified time
SECURE_HSTS_SECONDS = 31536000  # 1 year
# Include all subdomains in the HSTS policy
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# Allow your site to be included in the HSTS preload list
SECURE_HSTS_PRELOAD = True

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True


X_FRAME_OPTIONS = 'DENY'

# Ensure that Secure Cookies are only sent over HTTPS connections
CSRF_COOKIE_HTTPONLY = True
SESSION_COOKIE_HTTPONLY = True

SECURE_CONTENT_TYPE_NOSNIFF = True

SECURE_BROWSER_XSS_FILTER = True

# SECURE_SSL_REDIRECT: Redirects all HTTP requests to HTTPS
SECURE_SSL_REDIRECT = True

# SECURE_HSTS_SECONDS: Sets the HSTS policy to 1 year
SECURE_HSTS_SECONDS = 31536000

# SECURE_HSTS_INCLUDE_SUBDOMAINS: Applies HSTS policy to all subdomains
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

# SECURE_HSTS_PRELOAD: Allows inclusion in HSTS preload list
SECURE_HSTS_PRELOAD = True

# SESSION_COOKIE_SECURE: Ensures session cookies are only transmitted over HTTPS
SESSION_COOKIE_SECURE = True

# CSRF_COOKIE_SECURE: Ensures CSRF cookies are only transmitted over HTTPS
CSRF_COOKIE_SECURE = True

# X_FRAME_OPTIONS: Prevents clickjacking by denying framing
X_FRAME_OPTIONS = 'DENY'

# SECURE_CONTENT_TYPE_NOSNIFF: Prevents MIME sniffing
SECURE_CONTENT_TYPE_NOSNIFF = True

# SECURE_BROWSER_XSS_FILTER: Enables browser XSS filtering
SECURE_BROWSER_XSS_FILTER = True
