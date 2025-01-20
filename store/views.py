"""********************************************************************************
* Dokoon Project                                                                 *
* Author: Idarbandi                                                              *
* GitHub: https://github.com/idarbandi/Dokoon-NextDRF                             *
* Email: darbandidr99@gmail.com                                                    *
*                                                                                *
* This project was developed by Idarbandi.                                         *
* We hope you find it useful! Contributions and feedback are welcome.             *
********************************************************************************"""

from django.shortcuts import render
from rest_framework import generics

from .models import DokoonCategory, DokoonProduct  # Import renamed models
from .serializers import DokoonCategorySerializer, DokoonProductSerializer


class DokoonProductListView(generics.ListAPIView):
    """
    نمايي براي نمايش ليست تمامي محصولات پروژه Dokoon.

    خروجي اين نمايه، ليستي از محصولات سريال شده با DokoonProductSerializer است.
    """
    queryset = DokoonProduct.objects.all()
    serializer_class = DokoonProductSerializer


class DokoonProductDetailView(generics.RetrieveAPIView):
    """
    نمايي براي نمايش جزئيات يک محصول خاص بر اساس اسلاگ آن.

    اين نمايه يک محصول را بر اساس اسلاگ آن از ديتابيس دريافت کرده و با استفاده از 
    DokoonProductSerializer آن را سريال کرده و برمي‌گرداند.
    """
    lookup_field = "slug"
    queryset = DokoonProduct.objects.all()
    serializer_class = DokoonProductSerializer


class DokoonCategoryProductListView(generics.ListAPIView):
    """
    نمايي براي نمايش ليست محصولات يک دسته بندي خاص و زيرمجموعه‌هاي آن.

    اين نمايه بر اساس اسلاگ دريافتي از URL، ليستي از محصولات آن دسته بندي 
    و تمامي زيرمجموعه‌هاي آن را فيلتر کرده و با استفاده از DokoonProductSerializer 
    آنها را سريال کرده و برمي‌گرداند.
    """
    serializer_class = DokoonProductSerializer

    def get_queryset(self):
        return DokoonProduct.objects.filter(
            category__in=DokoonCategory.objects.get(
                slug=self.kwargs["slug"]).get_descendants(include_self=True)
        )


class DokoonCategoryListView(generics.ListAPIView):
    """
    نمايي براي نمايش ليست تمامي دسته بندي‌هاي سطح يک پروژه Dokoon.

    خروجي اين نمايه، ليستي از دسته بندي‌هاي سطح يک سريال شده با 
    DokoonCategorySerializer است.
    """
    queryset = DokoonCategory.objects.filter(level=1)
    serializer_class = DokoonCategorySerializer
