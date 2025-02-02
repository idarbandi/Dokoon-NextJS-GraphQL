"""
********************************************************************************
 * 🌐 Dokoon-NextJS-GraphQL
 * 👤 Author: idarbandi
 * 📁 GitHub: https://github.com/idarbandi/Dokoon-NextJS-GraphQL
 * ✉️ Email: darbandidr99@gmail.com
 * 💼 LinkedIn: https://www.linkedin.com/in/amir-darbandi-72526b25b/
 *
 * This project was developed by idarbandi.
 * We hope you find it useful! Contributions and feedback are welcome.
 ********************************************************************************
"""

# این فایل تنظیمات اصلی پروژه دکون رو تعریف می‌کنه

from pathlib import Path

# بیاید مسیر پایه پروژه رو مشخص کنیم
BASE_DIR = Path(__file__).resolve().parent.parent

# کلید مخفی پروژه (SECRET_KEY) که باید محرمانه بمونه
SECRET_KEY = 'your-secret-key'  # کلید مخفی شما اینجا قرار می‌گیرد

# حالت دیباگ برای توسعه فعال است؛ در محیط واقعی حتماً غیرفعال کنید
DEBUG = True

# هاست‌های مجاز برای دسترسی به پروژه
ALLOWED_HOSTS = []

# اپلیکیشن‌های نصب شده در پروژه
INSTALLED_APPS = [
    # اپ‌های پیش‌فرض جنگو
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # اپ‌های شخص ثالث
    "corsheaders",
    'mptt',
    "graphene_django",
    # اپ‌های داخلی پروژه
    'store',
    'account',
]

# میان‌افزارهای پروژه که درخواست‌ها رو پردازش می‌کنن
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # مدیریت درخواست‌های CORS
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',  # حفاظت CSRF
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# تنظیمات CORS برای اجازه دسترسی از دامنه‌های دیگر
CORS_EXPOSE_HEADERS = [
    'Content-Type', 'X-CSRFToken'
]
CORS_ALLOW_CREDENTIALS = True
CSRF_COOKIE_SAMESITE = 'Lax'
SESSION_COOKIE_SAMESITE = 'Lax'
CSRF_USE_SESSIONS = True
CSRF_COOKIE_HTTPONLY = True
CSRF_COOKIE_SECURE = False  # اگر از HTTPS استفاده می‌کنید، True کنید

CORS_ALLOW_HEADERS = [
    'content-type',
    'X-CSRFToken',
    'X-Requested-With',
]

SESSION_COOKIE_HTTPONLY = True

# لیست دامنه‌های مجاز برای ارسال درخواست به سرور
CORS_ORIGIN_WHITELIST = (
    'http://localhost:3000',      # برای توسعه محلی با React
    'http://127.0.0.1:3000',      # برای دسترسی از طریق شبکه محلی
    'http://localhost:8080',      # پورت دیگر برای توسعه
    'http://192.168.0.50:8080',   # آی‌پی شبکه محلی برای توسعه
)

# دامنه‌های مورد اعتماد برای CSRF
CSRF_TRUSTED_ORIGINS = [
    'http://localhost:3000',
    'http://192.168.0.50:3000',
    'http://localhost:8080',
    'http://192.168.0.50:8080',
]

# تنظیمات مسیرهای اصلی پروژه
ROOT_URLCONF = 'base.urls'

# تنظیمات قالب‌ها (Templates)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # می‌تونید مسیر قالب‌های خودتون رو اینجا اضافه کنید
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

# برنامه WSGI برای اجرای پروژه
WSGI_APPLICATION = 'base.wsgi.application'

# تنظیمات پایگاه داده؛ در حالت توسعه از SQLite استفاده می‌کنیم
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# اگر حالت دیباگ غیرفعال بود، از PostgreSQL استفاده می‌کنیم
if not DEBUG:
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_postgres_db_name',
        'USER': 'your_postgres_user',
        'PASSWORD': 'your_postgres_password',
        'HOST': 'your_postgres_host',
        'PORT': 'your_postgres_port',
    }

# اعتبارسنجی رمز عبور کاربران
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
LANGUAGE_CODE = 'en-us'  # می‌تونید به 'fa' تغییر بدید اگر می‌خواهید
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# تنظیمات فایل‌های استاتیک
STATIC_URL = "/static/"
STATIC_ROOT = "static/"

# تنظیمات فایل‌های رسانه‌ای
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media/"

# تنظیمات پیش‌فرض برای فیلدهای خودکار
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# تنظیمات Graphene برای GraphQL
GRAPHENE = {
    'SCHEMA': 'base.schema.schema',
    "MIDDLEWARE": [
        "graphql_jwt.middleware.JSONWebTokenMiddleware",
    ],
}

# بک‌اندهای احراز هویت
AUTHENTICATION_BACKENDS = [
    "graphql_jwt.backends.JSONWebTokenBackend",
    "django.contrib.auth.backends.ModelBackend",
]
