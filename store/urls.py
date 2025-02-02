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

# این فایل مسیرهای API برای اپلیکیشن فروشگاه دکون رو تعریف می‌کنه

from django.urls import path

from . import views

# نام اپلیکیشن رو تعریف می‌کنیم
app_name = "store"

# اینجا مسیرهای URL مربوط به اپلیکیشن فروشگاه دکون رو تعریف می‌کنیم
urlpatterns = [
    # مسیر نمایش لیست محصولات (صفحه اصلی فروشگاه)
    path("api/محصولات/", views.DokoonProductListView.as_view(), name="store_home"),
    # مسیر نمایش لیست دسته‌بندی‌ها
    path("api/دسته-بندی‌ها/",
         views.DokoonCategoryListView.as_view(), name="categories"),
    # مسیر نمایش جزئیات یک محصول خاص
    path("api/محصول/<slug:slug>/",
         views.DokoonProductDetailView.as_view(), name="product"),
    # مسیر نمایش محصولات یک دسته‌بندی خاص
    path("api/دسته-بندی/<slug:slug>/محصولات/",
         views.DokoonCategoryProductListView.as_view(), name="category_item"),
]
