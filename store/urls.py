"""
آدرس‌های API فروشگاه پروژه Dokoon.
این بخش، مسیرهای دسترسی به نقاط پایانی API فروشگاه را تعریف می‌کند.
"""

from django.urls import path

from . import views

app_name = "store"

urlpatterns = [
    # نمایش لیست محصولات (صفحه اصلی فروشگاه)
    path("api/محصولات/", views.DokoonProductListView.as_view(), name="store_home"),
    # نمایش لیست دسته‌بندی‌ها
    path("api/دسته-بندی‌ها/",
         views.DokoonCategoryListView.as_view(), name="categories"),
    # نمایش جزئیات یک محصول خاص
    path("api/محصول/<slug:slug>/",
         views.DokoonProductDetailView.as_view(), name="product"),
    # نمایش محصولات یک دسته‌بندی خاص
    path("api/دسته-بندی/<slug:slug>/محصولات/",
         views.DokoonCategoryProductListView.as_view(), name="category_item"),
]
