import os
from pathlib import Path

from dotenv import load_dotenv
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')


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
    
    'django.contrib.sites', 
# Sinekys Apps
    'accounts',
    'core', 
    'ejercicios',

# AllAuth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # Providers
    'allauth.socialaccount.providers.google', 
    # 'allauth.socialaccount.providers.linkedin', 
    
]
SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = 'sinekys.urls'



TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'sinekys.wsgi.application'

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',
    # pairs
    # username + password
    # email + password
]
# AllAuth settings | Pendiente | Pending


# SOCIALACCOUNT_PROVIDERS = {
#     'google': {
#         'SCOPE': [
#             'profile',
#             'email',
#         ],
#         'AUTH_PARAMS': {
#             'access_type': 'online',
#         },
#         'OAUTH_PKCE_ENABLED' : True, # Check whats the purpose of this
        
#         'APP': {
#             'client_id': '123',
#             'secret': '456',
#             'key': ''
#         }
#     }
# }



# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('PORT'),
    }
}



# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'
# The directory where static files are collected
# This is used when running the collectstatic command
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# ALLAUTH_SETTINGS
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# EmailSenderConfig
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('G_EMAIL')
EMAIL_HOST_PASSWORD = os.getenv('G_PASSWORD') 

LOGIN_REDIRECT_URL = '/'

# ACCOUNT_AUTHENTICATION_METHOD = 'email' #'username_email' # It says its deprecated...
ACCOUNT_LOGIN_METHODS = {'email'}  # 'username_email' or 'email'
# ACCOUNT_EMAIL_REQUIRED = True # Its says its deprecated...
ACCOUNT_SIGNUP_FIELDS = ['email*','password1','password2']  
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'  # 'mandatory' or 'optional'
ACCOUNT_MAX_EMAIL_ADDRESSES = 3
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True #2FA email

ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1
ACCOUNT_EMAIL_MAX_LENGTH = 254
ACCOUNT_USERNAME_MIN_LENGTH = 4

ACCOUNT_USERNAME_BLACKLIST = [
    'admin',
    'administrator',
    'root',
]

AUTH_USER_MODEL = 'accounts.CustomUser'
AUTH_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_SIGNUP_FORM_CLASS = 'accounts.forms.CustomSignupForm'
