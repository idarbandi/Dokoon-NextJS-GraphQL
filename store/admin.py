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
# Djangocontrib از ماژول admin کلاس admin را برای مدیریت مدل‌ها در پنل مدیریت وارد می‌کنیم.
from django.contrib import admin

# برای مدیریت مدل‌هایی که از افزونهٔ mptt استفاده می‌کنند، کلاس MPTTModelAdmin را از این ماژول وارد می‌کنیم.
from mptt.admin import MPTTModelAdmin

# از فایل models.py در همین پوشه، تمام مدل‌های مرتبط با فروشگاه (دسته‌بندی، محصول، تصویر محصول، مشخصات محصول، مقدار مشخصات محصول و نوع محصول) را import می‌کنیم.
from .models import (
    Category,
    Product,
    ProductImage,
    ProductSpecification,
    ProductSpecificationValue,
    ProductType,
)

# ثبت مدل Category در پنل مدیریت با امکان استفاده از قابلیت‌های mptt برای مدیریت سلسله‌مراتبی دسته‌بندی‌ها
admin.site.register(Category, MPTTModelAdmin)


# کلاس DokoonProductSpecificationInline برای نمایش مشخصات محصول به صورت جدولی درون صفحهٔ ویرایش نوع محصول
class DokoonProductSpecificationInline(admin.TabularInline):
    model = ProductSpecification


@admin.register(ProductType)
class DokoonProductTypeAdmin(admin.ModelAdmin):
    # درون این کلاس، مشخص می‌کنیم که در زمان ویرایش نوع محصول، امکان ویرایش مشخصات آن نوع محصول نیز به صورت جدولی (inline) وجود داشته باشد.
    inlines = [
        DokoonProductSpecificationInline,
    ]


# کلاس DokoonProductImageInline برای نمایش تصاویر محصول به صورت جدولی درون صفحهٔ ویرایش محصول
class DokoonProductImageInline(admin.TabularInline):
    model = ProductImage


# کلاس DokoonProductSpecificationValueInline برای نمایش مقادیر مشخصات محصول به صورت چینه‌اي (stacked) درون صفحهٔ ویرایش محصول
class DokoonProductSpecificationValueInline(admin.StackedInline):
    model = ProductSpecificationValue


@admin.register(Product)
class DokoonProductAdmin(admin.ModelAdmin):
    # درون این کلاس، مشخص می‌کنیم که در زمان ویرایش محصول، امکان ویرایش مقادیر مشخصات و تصاویر محصول به صورت جدولی (inline) وجود داشته باشد.
    inlines = [
        DokoonProductSpecificationValueInline,
        DokoonProductImageInline
    ]
