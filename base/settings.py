"""********************************************************************************
 * Dokoon Project
 * Author: Idarbandi
 * GitHub: https://github.com/idarbandi/Dokoon-NextDRF
 * Email: darbandidr99@gmail.com
 *
 * This project was developed by Idarbandi.
 * We hope you find it useful! Contributions and feedback are welcome.
 *********************************************************************************

"""

# این فایل تنظیمات اصلی پروژه دکوون را تعریف می‌کند.
# (This file defines the base settings for the Dokoon project.)

from pathlib import Path

# مسیرهای ساخت پروژه به این صورت ساخته می‌شوند: BASE_DIR / 'subdir'.
# (Build paths inside the project like this: BASE_DIR / 'subdir'.)
BASE_DIR = Path(__file__).resolve().parent.parent

# کلید مخفی برای مدیریت نشست‌ها و سایر موارد امنیتی. این را مخفی نگه دارید!
# (Secret key for session management and other security purposes. Keep this secret!)
SECRET_KEY = 'django-insecure-@$xjnk6_9@=rz517qu4s)$hy2nhs0hh%qxqeb8kgyavb5lpp-w'

# هشدار امنیتی: حالت اشکال‌زدایی را در محیط تولید فعال نکنید!
# (SECURITY WARNING: Don't enable debug mode in production!)
DEBUG = True

# هاست‌های مجاز برای محیط توسعه
# (Allowed hosts for the development environment)
ALLOWED_HOSTS = []

# برنامه‌های نصب شده
# (Applications to install)
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Third Party Apps
    "corsheaders",
    'mptt',
    "rest_framework",
    "graphene_django",
    # Internal Apps
    'store',
    'account',
]


# میان‌افزار برای مدیریت درخواست‌ها و پاسخ‌ها
# (Middleware for handling requests and responses)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# تنظیمات CORS برای اشتراک منابع بین دامنه‌ای
# (CORS settings for cross-origin resource sharing)
CORS_EXPOSE_HEADERS = [
    'Content-Type', 'X-CSRFToken'
]
CORS_ALLOW_CREDENTIALS = True
CSRF_COOKIE_SAMESITE = 'Lax'
SESSION_COOKIE_SAMESITE = 'Lax'
# settings.py
CSRF_USE_SESSIONS = True
CSRF_COOKIE_HTTPONLY = True
CSRF_COOKIE_SECURE = False  # Set to True if you're using HTTPS

CORS_ALLOW_HEADERS = [
    'content-type',
    'X-CSRFToken',
    'X-Requested-With',
]

SESSION_COOKIE_HTTPONLY = True

CORS_ORIGIN_WHITELIST = (
    'http://localhost:3000',  # برای لوکال هاست (پیش‌فرض React)
    'http://127.0.0.1:3000',  # برای شبکه
    'http://localhost:8080',  # برای لوکال هاست (توسعه)
    'http://192.168.0.50:8080',  # برای شبکه (توسعه)
)

CSRF_TRUSTED_ORIGINS = [
    'http://localhost:3000',  # برای لوکال هاست (پیش‌فرض React)
    'http://192.168.0.50:3000',  # برای شبکه
    'http://localhost:8080',  # برای لوکال هاست (توسعه)
    'http://192.168.0.50:8080',  # برای شبکه (توسعه)
]

# تنظیمات URL ریشه برای مسیریابی درخواست‌ها
# (Root URLconf for routing requests)
ROOT_URLCONF = 'base.urls'

# قالب‌ها برای رندر کردن صفحات HTML
# (Templates for rendering HTML pages)
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
            ],
        },
    },
]

# برنامه WSGI برای مدیریت درخواست‌های سرور وب
# (WSGI application for handling web server requests)
WSGI_APPLICATION = 'base.wsgi.application'

# تنظیمات پایگاه داده (در حال حاضر از SQLite برای توسعه استفاده می‌شود)
# (Database configuration (currently using SQLite for development))
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

if not DEBUG:
    # تنظیمات پایگاه داده برای محیط تولید (PostgreSQL)
    # (Database settings for production environment (PostgreSQL))
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_postgres_db_name',
        'USER': 'your_postgres_user',
        'PASSWORD': 'your_postgres_password',
        'HOST': 'your_postgres_host',
        'PORT': 'your_postgres_port',
    }

# اعتبارسنجی رمز عبور
# (Password validation)
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

# تنظیمات بین‌المللی‌سازی
# (Internationalization settings)
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True
USE_TZ = True

# فایل‌های استاتیک (CSS، جاوااسکریپت، تصاویر)
# (Static files (CSS, JavaScript, Images))
STATIC_URL = "/static/"
STATIC_ROOT = "static/"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media/"

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# تنظیمات Rest Framework
# (Rest Framework settings)
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly"
    ]
}

GRAPHENE = {
    'SCHEMA': 'base.schema.schema',
    "MIDDLEWARE": [
        "graphql_jwt.middleware.JSONWebTokenMiddleware",
    ],
}


AUTHENTICATION_BACKENDS = [
    "graphql_jwt.backends.JSONWebTokenBackend",
    "django.contrib.auth.backends.ModelBackend",
]
