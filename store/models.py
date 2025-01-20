"""********************************************************************************
* Dokoon Project                                                                 *
* Author: Idarbandi                                                              *
* GitHub: https://github.com/idarbandi/Dokoon-NextDRF                             *
* Email: darbandidr99@gmail.com                                                    *
*                                                                                *
* This project was developed by Idarbandi.                                         *
* We hope you find it useful! Contributions and feedback are welcome.             *
********************************************************************************"""


from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey


class DokoonCategory(MPTTModel):
    """
    مدل دسته بندی محصولات برای پروژه Dokoon.
    این مدل برای مدیریت دسته بندی محصولات به صورت درختی استفاده می‌شود.

    فیلدها:
        name (str): نام دسته بندی.
        slug (str): اسلاگ دسته بندی.
        parent (DokoonCategory): دسته بندی والد.
        is_active (bool): وضعیت فعال بودن دسته بندی.

    متدها:
        get_absolute_url(): آدرس کامل دسته بندی را برمی‌گرداند.
        __str__(): نام دسته بندی را برمی‌گرداند.
    """

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
    """
    مدل نوع محصول برای پروژه Dokoon.
    این مدل برای تعریف انواع مختلف محصولات استفاده می‌شود.

    فیلدها:
        name (str): نام نوع محصول.
        is_active (bool): وضعیت فعال بودن نوع محصول.

    متدها:
        __str__(): نام نوع محصول را برمی‌گرداند.
    """

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
    """
    مدل مشخصات محصول برای پروژه Dokoon.
    این مدل برای تعریف مشخصات مختلف هر نوع محصول استفاده می‌شود.

    فیلدها:
        product_type (DokoonProductType): نوع محصول مرتبط.
        name (str): نام مشخصه.

    متدها:
        __str__(): نام مشخصه را برمی‌گرداند.
    """

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
    """
    مدل محصول برای پروژه Dokoon.
    این مدل اطلاعات اصلی محصولات را ذخیره می‌کند.

    فیلدها:
        product_type (DokoonProductType): نوع محصول.
        category (DokoonCategory): دسته بندی محصول.
        title (str): عنوان محصول.
        description (str): توضیحات محصول.
        slug (str): اسلاگ محصول.
        regular_price (Decimal): قیمت اصلی محصول.
        discount_price (Decimal): قیمت تخفیف‌خورده محصول.
        is_active (bool): وضعیت فعال بودن محصول.
        created_at (datetime): زمان ایجاد محصول.
        updated_at (datetime): زمان آخرین بروزرسانی محصول.

    متدها:
        get_absolute_url(): آدرس کامل محصول را برمی‌گرداند.
        __str__(): عنوان محصول را برمی‌گرداند.
    """


"""********************************************************************************
* Dokoon Project                                                                 *
* Author: Idarbandi                                                              *
* GitHub: https://github.com/idarbandi/Dokoon-NextDRF                             *
* Email: darbandidr99@gmail.com                                                    *
*                                                                                *
* This project was developed by Idarbandi.                                         *
* We hope you find it useful! Contributions and feedback are welcome.             *
********************************************************************************"""


class DokoonCategory(MPTTModel):
    """
    مدل دسته بندی محصولات برای پروژه Dokoon.
    این مدل برای مدیریت دسته بندی محصولات به صورت درختی استفاده می‌شود.

    فیلدها:
        name (str): نام دسته بندی.
        slug (str): اسلاگ دسته بندی.
        parent (DokoonCategory): دسته بندی والد.
        is_active (bool): وضعیت فعال بودن دسته بندی.

    متدها:
        get_absolute_url(): آدرس کامل دسته بندی را برمی‌گرداند.
        __str__(): نام دسته بندی را برمی‌گرداند.
    """

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
    """
    مدل نوع محصول برای پروژه Dokoon.
    این مدل برای تعریف انواع مختلف محصولات استفاده می‌شود.

    فیلدها:
        name (str): نام نوع محصول.
        is_active (bool): وضعیت فعال بودن نوع محصول.

    متدها:
        __str__(): نام نوع محصول را برمی‌گرداند.
    """

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
    """
    مدل مشخصات محصول برای پروژه Dokoon.
    این مدل برای تعریف مشخصات مختلف هر نوع محصول استفاده می‌شود.

    فیلدها:
        product_type (DokoonProductType): نوع محصول مرتبط.
        name (str): نام مشخصه.

    متدها:
        __str__(): نام مشخصه را برمی‌گرداند.
    """

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
    """
    مدل محصول برای پروژه Dokoon.
    این مدل اطلاعات اصلی محصولات را ذخیره می‌کند.

    فیلدها:
        product_type (DokoonProductType): نوع محصول.
        category (DokoonCategory): دسته بندی محصول.
        title (str): عنوان محصول.
        description (str): توضیحات محصول.
        slug (str): اسلاگ محصول.
        regular_price (Decimal): قیمت اصلی محصول.
        discount_price (Decimal): قیمت تخفیف‌خورده محصول.
        is_active (bool): وضعیت فعال بودن محصول.
        created_at (datetime): زمان ایجاد محصول.
        updated_at (datetime): زمان آخرین بروزرسانی محصول.

    متدها:
        get_absolute_url(): آدرس کامل محصول را برمی‌گرداند.
        __str__(): عنوان محصول را برمی‌گرداند.
    """

    product_type = models.ForeignKey(
        DokoonProductType, on_delete=models.RESTRICT)
    category = models.ForeignKey(DokoonCategory, on_delete=models.RESTRICT)
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
    """
    مدل مقادیر مشخصات محصول برای پروژه Dokoon.
    این مدل مقادیر مربوط به هر مشخصه برای هر محصول را ذخیره می‌کند.

    فیلدها:
        product (DokoonProduct): محصول مرتبط.
        specification (DokoonProductSpecification): مشخصه مرتبط.
        value (str): مقدار مشخصه.
    """

    product = models.ForeignKey(DokoonProduct, on_delete=models.CASCADE)
    specification = models.ForeignKey(
        DokoonProductSpecification, on_delete=models.RESTRICT
    )
    value = models.CharField(
        verbose_name=_("Value"),
        help_text=_("Product Specification Value (Maximum of 255 Words)"),
        max_length=255,
    )

    class Meta:
        verbose_name = _("Product Specification Value")
        verbose_name_plural = _("Product Specification Values")


class DokoonProductImage(models.Model):
    """
    تصاویر محصولات در پروژه Dokoon

    فیلدها:
        product (DokoonProduct): محصول مرتبط
        image (ImageField): تصویر محصول
        alt_text (str): متن جایگزین تصویر (اختیاری)
        is_feature (bool): تصویر اصلی محصول
        created_at (datetime): زمان ایجاد تصویر
        updated_at (datetime): زمان آخرین بروزرسانی تصویر
    """

    product = models.ForeignKey(
        DokoonProduct, on_delete=models.CASCADE, related_name="product_image"
    )  # removed _()
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
        # more informative string representation
        return f"Image for {self.product.title}"

    product_type = models.ForeignKey(
        DokoonProductType, on_delete=models.RESTRICT)
    category = models.ForeignKey(DokoonCategory, on_delete=models.RESTRICT)
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
    """
    مدل مقادیر مشخصات محصول برای پروژه Dokoon.
    این مدل مقادیر مربوط به هر مشخصه برای هر محصول را ذخیره می‌کند.

    فیلدها:
        product (DokoonProduct): محصول مرتبط.
        specification (DokoonProductSpecification): مشخصه مرتبط.
        value (str): مقدار مشخصه.
    """

    product = models.ForeignKey(DokoonProduct, on_delete=models.CASCADE)
    specification = models.ForeignKey(
        DokoonProductSpecification, on_delete=models.RESTRICT
    )
    value = models.CharField(
        verbose_name=_("Value"),
        help_text=_("Product Specification Value (Maximum of 255 Words)"),
        max_length=255,
    )

    class Meta:
        verbose_name = _("Product Specification Value")
        verbose_name_plural = _("Product Specification Values")


class DokoonProductImage(models.Model):
    """
    تصاویر محصولات در پروژه Dokoon

    فیلدها:
        product (DokoonProduct): محصول مرتبط
        image (ImageField): تصویر محصول
        alt_text (str): متن جایگزین تصویر (اختیاری)
        is_feature (bool): تصویر اصلی محصول
        created_at (datetime): زمان ایجاد تصویر
        updated_at (datetime): زمان آخرین بروزرسانی تصویر
    """

    product = models.ForeignKey(
        DokoonProduct, on_delete=models.CASCADE, related_name="product_image"
    )  # removed _()
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
        # more informative string representation
        return f"Image for {self.product.title}"
