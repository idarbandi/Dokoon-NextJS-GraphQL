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

# برای تعریف الگوهای آدرس‌ها (URL patterns)، تابع 'path' از بستهٔ 'django.urls' رو وارد می‌کنیم.
from django.urls import path

# برای دسترسی به viewها، از فایل 'views.py' در همین پوشه، import انجام می‌دیم.
from . import views

# نام فضای نام برای URLهای این برنامه رو 'account' قرار می‌دیم.
app_name = 'account'

# الگوهای آدرس‌های مربوط به برنامهٔ 'account'
urlpatterns = [
    # آدرس مربوط به دریافت توکن CSRF
    path("csrf/", views.get_csrf, name="api_csrf"),
    # آدرس مربوط به صفحهٔ ورود
    path("login/", views.Login_view, name="api_login"),
    # آدرس مربوط به نمایش اطلاعات کاربر فعلی (whoami) که توسط یک کلاس view مدیریت می‌شه.
    path("whoami/", views.who_am_i_view.as_view(), name="whoami")
]
