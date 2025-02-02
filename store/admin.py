"""
********************************************************************************
 * 🌐 Dokoon Project
 * 👤 Author: idarbandi
 * 📁 GitHub: https://github.com/idarbandi/Dokoon-NextJS-GraphQL
 * ✉️ Email: darbandidr99@gmail.com
 * 💼 LinkedIn: https://www.linkedin.com/in/amir-darbandi-72526b25b/
 *
 * This project was developed by idarbandi.
 * We hope you find it useful! Contributions and feedback are welcome.
 ********************************************************************************
"""

# این فایل تنظیمات مربوط به بخش ادمین اپلیکیشن فروشگاه دکون رو مدیریت می‌کنه

from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import (
    DokoonCategory,
    DokoonProduct,
    DokoonProductImage,
    DokoonProductSpecification,
    DokoonProductSpecificationValue,
    DokoonProductType,
)


# ثبت مدل DokoonCategory در بخش ادمین با استفاده از MPTTModelAdmin
@admin.register(DokoonCategory)
class DokoonCategoryAdmin(MPTTModelAdmin):
    # فیلدهایی که در لیست دسته‌بندی‌ها نمایش داده می‌شن
    list_display = ('name', 'parent', 'is_active')
    # افزودن فیلتر برای فعال یا غیرفعال بودن دسته‌بندی
    list_filter = ('is_active',)
    # امکان جستجو بر اساس نام دسته‌بندی
    search_fields = ('name',)
    # ساخت خودکار فیلد slug بر اساس نام
    prepopulated_fields = {'slug': ('name',)}

# تعریف Inline برای مشخصات محصول


class DokoonProductSpecificationInline(admin.TabularInline):
    model = DokoonProductSpecification
    # اجازه افزودن مشخصات جدید در پنل ادمین
    extra = 1

# ثبت مدل DokoonProductType در بخش ادمین


@admin.register(DokoonProductType)
class DokoonProductTypeAdmin(admin.ModelAdmin):
    # اضافه کردن مشخصات محصول به صورت Inline
    inlines = [DokoonProductSpecificationInline]
    # فیلدهایی که در لیست نوع محصولات نمایش داده می‌شن
    list_display = ('name', 'is_active')
    # افزودن فیلتر برای فعال یا غیرفعال بودن نوع محصول
    list_filter = ('is_active',)
    # امکان جستجو بر اساس نام نوع محصول
    search_fields = ('name',)

# تعریف Inline برای تصاویر محصول


class DokoonProductImageInline(admin.TabularInline):
    model = DokoonProductImage
    # اجازه افزودن تصاویر جدید در پنل ادمین
    extra = 1

# تعریف Inline برای مقادیر مشخصات محصول


class DokoonProductSpecificationValueInline(admin.StackedInline):
    model = DokoonProductSpecificationValue
    # اجازه افزودن مقادیر جدید برای مشخصات محصول
    extra = 1

# ثبت مدل DokoonProduct در بخش ادمین


@admin.register(DokoonProduct)
class DokoonProductAdmin(admin.ModelAdmin):
    # اضافه کردن Inline‌های مربوط به تصاویر و مشخصات محصول
    inlines = [
        DokoonProductSpecificationValueInline,
        DokoonProductImageInline,
    ]
    # فیلدهایی که در لیست محصولات نمایش داده می‌شن
    list_display = ('title', 'category', 'regular_price', 'is_active')
    # افزودن فیلتر برای دسته‌بندی، وضعیت فعال بودن و نوع محصول
    list_filter = ('category', 'is_active', 'product_type')
    # امکان جستجو بر اساس عنوان و توضیحات محصول
    search_fields = ('title', 'description')
    # ساخت خودکار فیلد slug بر اساس عنوان
    prepopulated_fields = {'slug': ('title',)}
