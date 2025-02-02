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

# این فایل اسکیمای GraphQL برای اپلیکیشن فروشگاه دکون رو تعریف می‌کنه

import graphene
from graphene_django import DjangoObjectType

# ایمپورت مدل‌های مورد نیاز از فایل models.py
from .models import DokoonCategory, DokoonProduct, DokoonProductImage


# تعریف نوع GraphQL برای تصاویر محصولات دکون
class DokoonProductImageType(DjangoObjectType):
    class Meta:
        model = DokoonProductImage
        fields = ('id', 'image', 'alt_text')

    def resolve_image(self, info):
        # این متد آدرس کامل تصویر رو برمی‌گردونه
        if self.image:
            self.image = info.context.build_absolute_uri(self.image.url)
        return self.image

# تعریف نوع GraphQL برای محصولات دکون


class DokoonProductType(DjangoObjectType):
    class Meta:
        model = DokoonProduct
        fields = (
            'id',
            'title',
            'description',
            'regular_price',
            'slug',
            'product_image',
            'product_category',
        )

# تعریف نوع GraphQL برای دسته‌بندی‌های دکون


class DokoonCategoryType(DjangoObjectType):
    class Meta:
        model = DokoonCategory
        fields = ('id', 'name', 'product_category', 'level')

# تعریف کوئری‌های GraphQL برای دکون


class DokoonQuery(graphene.ObjectType):
    # لیست همه محصولات
    dokoon_main_index = graphene.List(DokoonProductType)
    # لیست دسته‌بندی‌ها
    dokoon_category_index = graphene.List(DokoonCategoryType)
    # دریافت دسته‌بندی بر اساس نام
    dokoon_category_by_name = graphene.Field(
        DokoonCategoryType, name=graphene.String(required=True)
    )
    # دریافت محصول بر اساس اسلاگ
    dokoon_product_by_slug = graphene.Field(
        DokoonProductType, slug=graphene.String(required=True)
    )
    # دریافت تمام اسلاگ‌های محصولات
    dokoon_all_slugs = graphene.List(graphene.String)

    def resolve_dokoon_main_index(self, info):
        # این متد تمام محصولات رو برمی‌گردونه
        return DokoonProduct.objects.all()

    def resolve_dokoon_category_index(self, info):
        # این متد دسته‌بندی‌های سطح ۱ رو برمی‌گردونه
        return DokoonCategory.objects.filter(level=1)

    def resolve_dokoon_category_by_name(self, info, name):
        # این متد یک دسته‌بندی رو بر اساس نام برمی‌گردونه
        try:
            return DokoonCategory.objects.get(name=name)
        except DokoonCategory.DoesNotExist:
            return None

    def resolve_dokoon_product_by_slug(self, info, slug):
        # این متد یک محصول رو بر اساس اسلاگ برمی‌گردونه
        try:
            return DokoonProduct.objects.get(slug=slug)
        except DokoonProduct.DoesNotExist:
            return None

    def resolve_dokoon_all_slugs(self, info):
        # این متد تمام اسلاگ‌های محصولات رو برمی‌گردونه
        return DokoonProduct.objects.values_list('slug', flat=True)
