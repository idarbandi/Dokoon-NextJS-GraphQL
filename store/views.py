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

# این فایل ویوهای مربوط به فروشگاه دکون رو تعریف می‌کنه

from django.shortcuts import render

# ایمپورت مدل‌های مورد نیاز
from .models import DokoonCategory, DokoonProduct


# ویوی نمایش لیست محصولات
def dokoon_product_list_view(request):
    """
    ویویی برای نمایش لیست تمامی محصولات فروشگاه دکون.

    این ویو تمام محصولات را از دیتابیس استخراج و به قالب HTML ارسال می‌کند.
    """
    products = DokoonProduct.objects.all()
    return render(request, "store/product_list.html", {"products": products})

# ویوی نمایش جزئیات محصول


def dokoon_product_detail_view(request, slug):
    """
    ویویی برای نمایش جزئیات یک محصول خاص بر اساس اسلاگ آن.

    این ویو محصولی خاص را از دیتابیس استخراج و به قالب HTML ارسال می‌کند.
    """
    product = DokoonProduct.objects.get(slug=slug)
    return render(request, "store/product_detail.html", {"product": product})

# ویوی نمایش لیست محصولات یک دسته‌بندی خاص


def dokoon_category_product_list_view(request, slug):
    """
    ویویی برای نمایش لیست محصولات یک دسته‌بندی خاص و زیرمجموعه‌های آن.

    این ویو محصولات یک دسته‌بندی خاص را از دیتابیس استخراج و به قالب HTML ارسال می‌کند.
    """
    category = DokoonCategory.objects.get(slug=slug)
    products = DokoonProduct.objects.filter(
        category__in=category.get_descendants(include_self=True)
    )
    return render(request, "store/category_product_list.html", {"category": category, "products": products})

# ویوی نمایش لیست دسته‌بندی‌ها


def dokoon_category_list_view(request):
    """
    ویویی برای نمایش لیست تمامی دسته‌بندی‌های سطح یک فروشگاه دکون.

    این ویو تمام دسته‌بندی‌ها را از دیتابیس استخراج و به قالب HTML ارسال می‌کند.
    """
    categories = DokoonCategory.objects.filter(level=1)
    return render(request, "store/category_list.html", {"categories": categories})
