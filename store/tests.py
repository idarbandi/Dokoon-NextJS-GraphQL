from decimal import Decimal

from django.test import TestCase
from django.urls import reverse

from .models import (
    DokoonCategory,
    DokoonProduct,
    DokoonProductImage,
    DokoonProductSpecification,
    DokoonProductSpecificationValue,
    DokoonProductType,
)


def test_product_absolute_url(self):
    # Changed name to product
    url = reverse("store:product", args=[self.product.slug])
    self.assertEqual(self.product.get_absolute_url(), url)


def test_category_absolute_url(self):
    url = reverse("store:categories")  # Changed name to categories
    self.assertEqual(self.category.get_absolute_url(), url)


def test_product_detail_view(self):
    # Changed name to product
    url = reverse('store:product', args=[self.product.slug])
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, self.product.title)


def test_category_list_view(self):
    url = reverse('store:categories')  # Changed name to categories
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, self.category.name)


def test_product_list_view(self):
    url = reverse('store:store_home')  # Name from url
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)
    # Add more assertions to check the content of the response if needed.
