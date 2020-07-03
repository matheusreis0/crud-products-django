import json
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from products.models import Product

# Create your tests here.
class ProductTest(TestCase):

    products = [
        {
            "name": "Product 1",
            "price": 100.0
        },
        {
            "name": "Product 2",
            "price": 200.0
        },
    ]

    @classmethod
    def setUpTestData(cls):
        cls.client = APIClient(content_type='application/json')
        cls.url = "/api/product/"
        products = [Product(name=product['name'], price=product['price'])
            for product in cls.products]
        Product.objects.bulk_create(products)

    def setUp(self):
        # setUp run after every single test method
        pass

    def test_get_all_products(self):
        """
            Test GET method to all products in database
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_one_product(self):
        """
            Test GET method to one product
        """
        product_id = '1'
        response = self.client.get(f"{self.url}{product_id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_one_product(self):
        """
            Test POST method for a product
        """
        product_create_json = {
            "name": "Product Test",
            "price": 123.0
        }
        response = self.client.post(self.url, data=product_create_json, 
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_one_product(self):
        """
            Test PUT method to one product
        """
        product_id = '1'
        product_create_json = {
            "name": "Product Test",
            "price": 123.0
        }
        response = self.client.put(f"{self.url}{product_id}/", 
            data=product_create_json, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patch_one_product(self):
        """
            Test PATCH method to one product
        """
        product_id = '1'
        product_json = {
            "name": "Product teste"
        }
        response = self.client.patch(f"{self.url}{product_id}/", 
            data=product_json, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_one_product(self):
        """
            Test DELETE method to one product
        """
        product_id = '1'
        response = self.client.delete(f"{self.url}{product_id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
