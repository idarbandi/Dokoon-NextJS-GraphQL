"""********************************************************************************
* Dokoon Project                                                                 *
* Author: Idarbandi                                                              *
* GitHub: https://github.com/idarbandi/Dokoon-NextDRF                             *
* Email: darbandidr99@gmail.com                                                    *
*                                                                                *
* This project was developed by Idarbandi.                                         *
* We hope you find it useful! Contributions and feedback are welcome.             *
********************************************************************************"""

from rest_framework import serializers

from .models import (  # Import renamed models
    DokoonCategory,
    DokoonProduct,
    DokoonProductImage,
)


class DokoonImageSerializer(serializers.ModelSerializer):
    """
    سریالایزر برای مدل تصاویر محصول در پروژه Dokoon.

    فیلدها:
        image: تصویر محصول.
        alt_text: متن جایگزین تصویر.
    """
    class Meta:
        model = DokoonProductImage
        fields = ["image", "alt_text"]


class DokoonProductSerializer(serializers.ModelSerializer):
    """
    سریالایزر برای مدل محصول در پروژه Dokoon.

    فیلدها:
        id: شناسه محصول.
        category: دسته بندی محصول.
        title: عنوان محصول.
        description: توضیحات محصول.
        slug: اسلاگ محصول.
        regular_price: قیمت اصلی محصول.
        product_image: تصاویر محصول (سریالایز شده با DokoonImageSerializer).
    """
    product_image = DokoonImageSerializer(many=True, read_only=True)

    class Meta:
        model = DokoonProduct
        fields = ["id", "category", "title", "description",
                  "slug", "regular_price", "product_image"]


class DokoonCategorySerializer(serializers.ModelSerializer):
    """
    سریالایزر برای مدل دسته بندی محصول در پروژه Dokoon.

    فیلدها:
        name: نام دسته بندی.
        slug: اسلاگ دسته بندی.
    """
    class Meta:
        model = DokoonCategory
        fields = ["name", "slug"]
