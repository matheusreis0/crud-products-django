import json
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from products.models import Product

# Create your tests here.
class ProductTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.client = APIClient(content_type='application/json')
        cls.url = "/api/product/"

        number_of_products = 5

        for product_id in range(number_of_products):
            Product.objects.create(
                name=f"Product #{product_id}",
                price=product_id
            )

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
    
    def test_return_id_after_post_product(self):
        """
            Test to check if response returns the id of the new product
        """
        product_create_json = {
            "name": "Product Test",
            "price": 123.0
        }
        response = self.client.post(self.url, data=product_create_json, 
            content_type='application/json')
        content = response.data
        product = Product.objects.latest('id')

        self.assertEqual(content["id"], product.id)

    def test_missing_name_post_product(self):
        """
            Test to check if returns an error for POST of product without name
        """
        product_create_json = {
            "price": 123.0
        }
        response = self.client.post(self.url, data=product_create_json, 
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_missing_price_post_product(self):
        """
            Test to check if returns an error for POST of product without price
        """
        product_create_json = {
            "name": "Product"
        }
        response = self.client.post(self.url, data=product_create_json, 
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_missing_data_post_product(self):
        """
            Test to check if returns an error for POST of product without data
        """
        product_create_json = {}
        response = self.client.post(self.url, data=product_create_json, 
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_one_product(self):
        """
            Test PUT method to one product
        """
        product_id = '1'
        product_update_json = {
            "name": "Product Test",
            "price": 123.0
        }
        response = self.client.put(f"{self.url}{product_id}/", 
            data=product_update_json, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_missing_data_put_product(self):
        """
            Test to check if returns an error for PUT request without data
        """
        product_id = '1'
        product_update_json = {}
        response = self.client.put(f"{self.url}{product_id}/", 
            data=product_update_json, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_missing_name_put_product(self):
        """
            Test to check if returns an error for PUT method without name
        """
        product_id = '1'
        product_update_json = {
            "price": 123.0
        }
        response = self.client.put(f"{self.url}{product_id}/", 
            data=product_update_json, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_missing_price_post_product(self):
        """
            Test to check if returns an error for PUT method without price
        """
        product_id = '1'
        product_update_json = {
            "name": "Product"
        }
        response = self.client.put(f"{self.url}{product_id}/", 
            data=product_update_json, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_patch_method_one_product(self):
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
