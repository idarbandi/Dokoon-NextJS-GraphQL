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

# برای تعریف مسیرهای URL، تابع 'path' از ماژول 'django.urls' رو میاریم
from django.urls import path

# ویوها رو از فایل 'views.py' همین دایرکتوری میاریم
from . import views

# نام اپلیکیشن رو به 'dokoon_account' تغییر می‌دیم
app_name = 'dokoon_account'

# اینجا مسیرهای URL مربوط به اپلیکیشن 'dokoon_account' رو تعریف می‌کنیم
urlpatterns = [
    # مسیر گرفتن توکن CSRF
    path("csrf/", views.dokoon_get_csrf_token, name="dokoon_api_csrf"),
    # مسیر لاگین کاربر
    path("login/", views.dokoon_login_view, name="dokoon_api_login"),
    # مسیر نمایش اطلاعات کاربر فعلی
    path("whoami/", views.dokoon_who_am_i_view.as_view(), name="dokoon_whoami"),
    # مسیر لاگ‌اوت کاربر
    path('logout/', views.dokoon_logout_view, name='dokoon_api_logout'),
]
