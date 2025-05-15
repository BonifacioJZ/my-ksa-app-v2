from django.urls import reverse
from rest_framework import status
from tests.test_setup import TestSetUp
from ..factories.product_manager.product_factory import ProductFactory

class ProductTestCase(TestSetUp):
    def test_find_product(self):
        """
        Prueba el endpoint para encontrar un producto.
        """
        product = ProductFactory().build_product()
        response = self.client.get(
            reverse("product-detail", kwargs={"slug": product.slug}),
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        self.assertEqual(response.data['id'], str(product.id))
        self.assertEqual(response.data['name'], product.name)
        self.assertEqual(response.data['slug'], product.slug)
        
    def test_find_product_not_found(self):
        """
        Prueba el endpoint para encontrar un producto que no existe.
        """
        response = self.client.get(
            reverse("product-detail", kwargs={"slug": "non-existent-product"}),
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_create_product(self):
        """
        Prueba el endpoint para crear un producto.
        """
        product_data = ProductFactory().build_product_JSON()
        response = self.client.post(
            reverse("product-create-list"),
            data=product_data,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], product_data['name'])
        self.assertEqual(response.data['description'], product_data['description'])
        self.assertEqual(response.data['category'], product_data['category'])
        self.assertEqual(response.data['brand'], product_data['brand'])
    
    def test_create_product_invalid(self):
        """
        Prueba el endpoint para crear un producto con datos inválidos.
        """
        product_data = ProductFactory().build_product_invalid()
        response = self.client.post(
            reverse("product-create-list"),
            data=product_data,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('name', response.data)
        
        
    def test_create_product_invalid_category(self):
        """
        Prueba el endpoint para crear un producto con categoría inválida.
        """
        product_data = ProductFactory().build_product_invalid_category()
        response = self.client.post(
            reverse("product-create-list"),
            data=product_data,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('category', response.data)
    
    def test_create_product_invalid_brand(self):
        """
        Prueba el endpoint para crear un producto con marca inválida.
        """
        product_data = ProductFactory().build_product_invalid_brand()
        response = self.client.post(
            reverse("product-create-list"),
            data=product_data,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('brand', response.data)
    
    
    def test_update_product(self):
        """
        Prueba el endpoint para actualizar un producto.
        """
        product = ProductFactory().build_product()
        updated_data = {
            "name": "Updated Product Name",
            "description": "Updated Product Description",
            "category": product.category.id,
            "brand": product.brand.id,
        }
        response = self.client.put(
            reverse("product-update", kwargs={"slug": product.slug}),
            data=updated_data,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], updated_data['name'])
        self.assertEqual(response.data['description'], updated_data['description'])
        self.assertEqual(response.data['category'], updated_data['category'])
        self.assertEqual(response.data['brand'], updated_data['brand'])
    
    def test_update_product_not_found(self):
        """
        Prueba el endpoint para actualizar un producto que no existe.
        """
        updated_data = {
            "name": "Updated Product Name",
            "description": "Updated Product Description",
            "category": "invalid-category",
            "brand": "invalid-brand",
        }
        response = self.client.put(
            reverse("product-update", kwargs={"slug": "non-existent-product"}),
            data=updated_data,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_delete_product(self):
        """
        Prueba el endpoint para eliminar un producto.
        """
        product = ProductFactory().build_product()
        response = self.client.delete(
            reverse("product-delete", kwargs={"pk": product.pk}),
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(product._state.db == None)
        with self.assertRaises(product.DoesNotExist):
            product.refresh_from_db()
            
    def test_delete_product_not_found(self):
        """
        Prueba el endpoint para eliminar un producto que no existe.
        """
        response = self.client.delete(
            reverse("product-delete", kwargs={"pk": 999}),
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        