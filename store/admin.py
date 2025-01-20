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

from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import DokoonCategory  # Corrected model name
from .models import DokoonProduct  # Corrected model name
from .models import DokoonProductImage  # Corrected model name
from .models import DokoonProductSpecification  # Corrected model name
from .models import DokoonProductSpecificationValue  # Corrected model name
from .models import DokoonProductType  # Corrected model name


# Register DokoonCategory with MPTTModelAdmin
@admin.register(DokoonCategory)  # Corrected model name
class DokoonCategoryAdmin(MPTTModelAdmin):  # Created a custom admin class
    list_display = ('name', 'parent', 'is_active')  # Display relevant fields
    list_filter = ('is_active',)  # Add filters for easier management
    search_fields = ('name',)  # Add search field
    prepopulated_fields = {'slug': ('name',)}  # Automatically fill slug field


# Inline admin for Product Specifications
class DokoonProductSpecificationInline(admin.TabularInline):
    model = DokoonProductSpecification
    extra = 1  # allows adding new specifications directly in the admin panel


@admin.register(DokoonProductType)
class DokoonProductTypeAdmin(admin.ModelAdmin):
    inlines = [DokoonProductSpecificationInline]
    list_display = ('name', 'is_active')  # Display relevant fields
    list_filter = ('is_active',)  # Add filters for easier management
    search_fields = ('name',)  # Add search field

# Inline admin for Product Images


class DokoonProductImageInline(admin.TabularInline):
    model = DokoonProductImage
    extra = 1  # allows adding new images directly in the admin panel


# Inline admin for Product Specification Values
class DokoonProductSpecificationValueInline(admin.StackedInline):
    model = DokoonProductSpecificationValue
    extra = 1  # allows adding new specification values directly in the admin panel


@admin.register(DokoonProduct)
class DokoonProductAdmin(admin.ModelAdmin):
    inlines = [
        DokoonProductSpecificationValueInline,
        DokoonProductImageInline,
    ]
    list_display = ('title', 'category', 'regular_price',
                    'is_active')  # More fields for overview
    # Filters for easier management
    list_filter = ('category', 'is_active', 'product_type')
    search_fields = ('title', 'description')  # Add search fields
    prepopulated_fields = {'slug': ('title',)}  # Automatically fill slug field
