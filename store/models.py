"""********************************************************************************
 * Dokoon Project
 * Author: Idarbandi
 * GitHub: https://github.com/idarbandi/Dokoon-NextDRF
 * Email: darbandidr99@gmail.com
 *
 * This project was developed by Idarbandi.
 * We hope you find it useful! Contributions and feedback are welcome.
 *********************************************************************************"""

from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey


class DokoonCategory(MPTTModel):
    name = models.CharField(
        verbose_name=_("Category Name"),
        help_text=_("Make Sure To Fill It"),
        max_length=255,
        unique=True,
    )
    slug = models.SlugField(
        verbose_name=_("Category Safe Url"), max_length=255, unique=True
    )
    parent = TreeForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="children"
    )
    is_active = models.BooleanField(default=True)

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def get_absolute_url(self):
        return reverse("store:category_list", args={"pk": self.pk})

    def __str__(self):
        return self.name


class DokoonProductType(models.Model):
    name = models.CharField(
        verbose_name=_("Product Name"), help_text=_("Required"), max_length=255
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("Product Type")
        verbose_name_plural = _("Product Types")

    def __str__(self):
        return self.name


class DokoonProductSpecification(models.Model):
    product_type = models.ForeignKey(
        DokoonProductType, on_delete=models.RESTRICT)
    name = models.CharField(
        verbose_name=_("Name"), help_text=_("Required"), max_length=255
    )

    class Meta:
        verbose_name = _("Product Specification")
        verbose_name_plural = _("Product Specifications")

    def __str__(self):
        return self.name


class DokoonProduct(models.Model):
    product_type = models.ForeignKey(
        DokoonProductType, on_delete=models.RESTRICT)
    category = models.ForeignKey(
        DokoonCategory, on_delete=models.RESTRICT, related_name='product_category')
    title = models.CharField(
        verbose_name=_("Title"), help_text=_("Required"), max_length=255
    )
    description = models.TextField(
        verbose_name=_("Description"), help_text=_("Not Required"), blank=True
    )
    slug = models.SlugField(max_length=255)
    regular_price = models.DecimalField(
        verbose_name=_("Regular Price"),
        help_text=_("Maximum 999.99"),
        error_messages={"name": {"The Price Must Be Between 0 , 999,99"}},
        max_digits=5,
        decimal_places=2,
    )
    discount_price = models.DecimalField(
        verbose_name=_("Discount Price"),
        help_text=_("Maximum 999.99"),
        error_messages={"name": {"The Discount Must Be Between 0 , 999,99"}},
        max_digits=5,
        decimal_places=2,
    )
    is_active = models.BooleanField(
        verbose_name=_("Product Visibility"),
        help_text=_("Change Product Visibility"),
        default=True,
    )
    created_at = models.DateTimeField(
        _("Created at"), auto_now_add=True, editable=False
    )
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def get_absolute_url(self):
        return reverse("store:product_detail", args=[self.slug])

    def __str__(self):
        return self.title


class DokoonProductSpecificationValue(models.Model):
    product = models.ForeignKey(DokoonProduct, on_delete=models.CASCADE)
    specification = models.ForeignKey(
        DokoonProductSpecification, on_delete=models.RESTRICT)
    value = models.CharField(
        verbose_name=_("Value"),
        help_text=_("Product Specification Value (Maximum of 255 Words)"),
        max_length=255,
    )

    class Meta:
        verbose_name = _("Product Specification Value")
        verbose_name_plural = _("Product Specification Values")


class DokoonProductImage(models.Model):
    product = models.ForeignKey(
        DokoonProduct, on_delete=models.CASCADE, related_name="product_image"
    )
    image = models.ImageField(
        verbose_name=_("image"),
        help_text=_("Upload a Products Image"),
        upload_to="images/",
        default="images/default.png",
    )
    alt_text = models.CharField(
        verbose_name=_("Image Alternative Text"),
        help_text=_("Provide descriptive text for the image"),
        max_length=255,
        blank=True,
        null=True,
    )
    is_feature = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Product Image")
        verbose_name_plural = _("Product Images")

    def __str__(self):
        return f"Image for {self.product.title}"
