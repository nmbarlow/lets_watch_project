"""
Django settings for lets_watch_project project.

Generated by 'django-admin startproject' using Django 1.11.17.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
STATIC_DIR = os.path.join(BASE_DIR, 'static')
MEDIA_DIR = os.path.join(BASE_DIR, 'media')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')ju96h9$p+#f20ts&$2ht&86eccke)t)jciel6xpd1!pjw(0ug'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['http://letuswatch.pythonanywhere.com/', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'letswatch',
    # 'search',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'lets_watch_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR,],
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

WSGI_APPLICATION = 'lets_watch_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
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


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Media files
MEDIA_ROOT = MEDIA_DIR
MEDIA_URL = '/media/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

# # im not sure if this is working yet!
# SOCIAL_AUTH_PIPELINE = (
#     'social_core.pipeline.social_auth.social_details',
#     'social_core.pipeline.social_auth.social_uid',
#     'social_core.pipeline.social_auth.auth_allowed',
#     'social_core.pipeline.social_auth.social_user',
#     'social_core.pipeline.user.get_username',
#     'social_core.pipeline.user.create_user',
#     'lets_watch_project.pipeline.user.create_user',
#     'social_core.pipeline.social_auth.associate_user',
#     'social_core.pipeline.social_auth.load_extra_data',
#     'social_core.pipeline.user.user_details',
# )
#
# SOCIAL_AUTH_TWITTER_KEY = 'utEdYgQ1BshKe73mp82VPmorm'
# SOCIAL_AUTH_TWITTER_SECRET = 'NrcAHdEFg75KlSDoN8dDO4hehk1297Jmkv61K3c2KtVuvyau6q'
#
# AUTHENTICATION_BACKENDS = (
#     'social_core.backends.twitter.TwitterOAuth',
#     'django.contrib.auth.backends.ModelBackend',
# )


# google api key GOOGLE_KEY 'AIzaSyB9Fn6ws_C1eAjmx9Hmxd3RlcobnSHkyr4'

# facebook - not exactly sure what file it will go in to, but its JavaScript
# <script>
#   window.fbAsyncInit = function() {
#     FB.init({
#       appId      : '{your-app-id}',
#       cookie     : true,
#       xfbml      : true,
#       version    : '{api-version}'
#     });
#
#     FB.AppEvents.logPageView();
#
#   };
#
#   (function(d, s, id){
#      var js, fjs = d.getElementsByTagName(s)[0];
#      if (d.getElementById(id)) {return;}
#      js = d.createElement(s); js.id = id;
#      js.src = "https://connect.facebook.net/en_US/sdk.js";
#      fjs.parentNode.insertBefore(js, fjs);
#    }(document, 'script', 'facebook-jssdk'));
# </script>

  # check log in status
    # FB.getLoginStatus(function(response) {
    #     statusChangeCallback(response);
    # });

    # {
    #     status: 'connected',
    #     authResponse: {
    #         accessToken: '...',
    #         expiresIn:'...',
    #         signedRequest:'...',
    #         userID:'...'
    #     }
    # }

    # button
    # function checkLoginState() {
    #   FB.getLoginStatus(function(response) {
    #     statusChangeCallback(response);
    #   });
    # }
