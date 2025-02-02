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

# این فایل مدل‌های دیتابیس برای اپلیکیشن فروشگاه دکون رو تعریف می‌کنه

from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey


# مدل دسته‌بندی محصولات دکون
class DokoonCategory(MPTTModel):
    name = models.CharField(
        verbose_name=_("نام دسته‌بندی"),
        help_text=_("نام دسته‌بندی رو اینجا وارد کن"),
        max_length=255,
        unique=True,
    )
    slug = models.SlugField(
        verbose_name=_("آدرس امن دسته‌بندی"), max_length=255, unique=True
    )
    parent = TreeForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="children"
    )
    is_active = models.BooleanField(default=True)

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        verbose_name = _("دسته‌بندی")
        verbose_name_plural = _("دسته‌بندی‌ها")

    def get_absolute_url(self):
        # این متد آدرس مطلق دسته‌بندی رو برمی‌گردونه
        return reverse("store:category_list", args={"pk": self.pk})

    def __str__(self):
        # نمایش نام دسته‌بندی در ادمین
        return self.name

# مدل نوع محصول دکون


class DokoonProductType(models.Model):
    name = models.CharField(
        verbose_name=_("نام نوع محصول"), help_text=_("اسم نوع محصول رو وارد کن"), max_length=255
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("نوع محصول")
        verbose_name_plural = _("انواع محصولات")

    def __str__(self):
        return self.name

# مدل مشخصات محصولات دکون


class DokoonProductSpecification(models.Model):
    product_type = models.ForeignKey(
        DokoonProductType, on_delete=models.RESTRICT
    )
    name = models.CharField(
        verbose_name=_("نام مشخصه"), help_text=_("نام مشخصه رو وارد کن"), max_length=255
    )

    class Meta:
        verbose_name = _("مشخصات محصول")
        verbose_name_plural = _("مشخصات محصولات")

    def __str__(self):
        return self.name

# مدل محصول دکون


class DokoonProduct(models.Model):
    product_type = models.ForeignKey(
        DokoonProductType, on_delete=models.RESTRICT
    )
    category = models.ForeignKey(
        DokoonCategory, on_delete=models.RESTRICT, related_name='product_category'
    )
    title = models.CharField(
        verbose_name=_("عنوان محصول"), help_text=_("عنوان محصول رو وارد کن"), max_length=255
    )
    description = models.TextField(
        verbose_name=_("توضیحات محصول"), help_text=_("توضیحات محصول (اختیاری)"), blank=True
    )
    slug = models.SlugField(max_length=255)
    regular_price = models.DecimalField(
        verbose_name=_("قیمت عادی"),
        help_text=_("قیمت عادی محصول (حداکثر 999.99)"),
        error_messages={"name": {"The price must be between 0 and 999.99"}},
        max_digits=5,
        decimal_places=2,
    )
    discount_price = models.DecimalField(
        verbose_name=_("قیمت تخفیف‌خورده"),
        help_text=_("قیمت با تخفیف محصول (حداکثر 999.99)"),
        error_messages={"name": {"The discount must be between 0 and 999.99"}},
        max_digits=5,
        decimal_places=2,
    )
    is_active = models.BooleanField(
        verbose_name=_("نمایش محصول"),
        help_text=_("آیا محصول فعال باشد یا نه"),
        default=True,
    )
    created_at = models.DateTimeField(
        _("تاریخ ایجاد"), auto_now_add=True, editable=False
    )
    updated_at = models.DateTimeField(_("تاریخ به‌روزرسانی"), auto_now=True)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = _("محصول")
        verbose_name_plural = _("محصولات")

    def get_absolute_url(self):
        # این متد آدرس مطلق محصول رو برمی‌گردونه
        return reverse("store:product_detail", args=[self.slug])

    def __str__(self):
        return self.title

# مدل مقادیر مشخصات محصول دکون


class DokoonProductSpecificationValue(models.Model):
    product = models.ForeignKey(DokoonProduct, on_delete=models.CASCADE)
    specification = models.ForeignKey(
        DokoonProductSpecification, on_delete=models.RESTRICT
    )
    value = models.CharField(
        verbose_name=_("مقدار"),
        help_text=_("مقدار مشخصه محصول (حداکثر 255 کاراکتر)"),
        max_length=255,
    )

    class Meta:
        verbose_name = _("مقدار مشخصات محصول")
        verbose_name_plural = _("مقادیر مشخصات محصولات")

    def __str__(self):
        return f"{self.specification.name}: {self.value}"

# مدل تصاویر محصولات دکون


class DokoonProductImage(models.Model):
    product = models.ForeignKey(
        DokoonProduct, on_delete=models.CASCADE, related_name="product_image"
    )
    image = models.ImageField(
        verbose_name=_("تصویر محصول"),
        help_text=_("یک تصویر برای محصول آپلود کن"),
        upload_to="images/",
        default="images/default.png",
    )
    alt_text = models.CharField(
        verbose_name=_("متن جایگزین"),
        help_text=_("متن جایگزین برای تصویر (برای SEO)"),
        max_length=255,
        blank=True,
        null=True,
    )
    is_feature = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("تصویر محصول")
        verbose_name_plural = _("تصاویر محصولات")

    def __str__(self):
        return f"تصویر مربوط به {self.product.title}"
