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

# این فایل مسیرهای اصلی پروژه دکون رو تعریف می‌کنه

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from graphql_jwt.decorators import jwt_cookie

# تعریف الگوی URL‌های اصلی پروژه
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("store.urls", namespace="dokoon_store")),
    path("account/", include("account.urls", namespace="dokoon_account")),
    # مسیر GraphQL با احراز هویت JWT و غیرفعال کردن بررسی CSRF
    path("graphql/", jwt_cookie(csrf_exempt(GraphQLView.as_view(graphiql=True)))),
]

# اگر حالت دیباگ فعال بود، فایل‌های رسانه‌ای رو هم سرو می‌کنیم
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
