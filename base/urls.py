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

# این فایل مسیریابی اصلی برای پروژه دکوون را تعریف می‌کند.
# (This file defines the main URL routing for the Dokoon project.)

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("store.urls", namespace="store")),
    path("account/", include("account.urls", namespace="account")),
]

# مسیریابی برای فایل‌های استاتیک (تنها در حالت توسعه)
# (Routing for static files (only in development mode))
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
