from django.urls import reverse
from rest_framework import status
from tests.test_setup import TestSetUp
from ..factories.presentation_manager.presentation_manager import PresentationFactory

class PresentationTestCase(TestSetUp):
    def test_find_presentation(self):
        """
        Prueba el endpoint para encontrar una presentación.
        """
        presentation = PresentationFactory().build_presentation()
        response = self.client.get(
            reverse("presentation-detail", kwargs={"slug": presentation.slug}),
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        self.assertEqual(response.data['id'], str(presentation.id))
        self.assertEqual(response.data['name'], presentation.name)
        self.assertEqual(response.data['product'], presentation.product.id)
        self.assertEqual(response.data['stock'], presentation.stock)
        self.assertEqual(response.data['sku'], presentation.sku)
        self.assertEqual(response.data['bar_code'], presentation.bar_code)
        self.assertEqual(response.data['abbreviation'], presentation.abbreviation)
    
    def test_create_presentation(self):
        """
        Prueba el endpoint para crear una presentación.
        """
        presentation_data = PresentationFactory().build_presentation_JSON()
        response = self.client.post(
            reverse("presentation-list-create"),
            data=presentation_data,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        self.assertEqual(response.data['name'], presentation_data['name'])
        self.assertEqual(response.data['product'], presentation_data['product'])
        self.assertEqual(response.data['stock'], presentation_data['stock'])
        self.assertEqual(response.data['sku'], presentation_data['sku'])
        self.assertEqual(response.data['bar_code'], presentation_data['bar_code'])
        self.assertEqual(response.data['abbreviation'], presentation_data['abbreviation'])
        
    def test_create_presentation_invalid(self):
        """
        Prueba el endpoint para crear una presentación con datos inválidos.
        """
        presentation_data = PresentationFactory().build_presentation_invalid()
        response = self.client.post(
            reverse("presentation-list-create"),
            data=presentation_data,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("name", response.data)
    
    def test_create_presentation_invalid_product(self):
        """
        Prueba el endpoint para crear una presentación con producto inválido.
        """
        presentation_data = PresentationFactory().build_presentation_invalid_product()
        response = self.client.post(
            reverse("presentation-list-create"),
            data=presentation_data,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("product", response.data)
    
    def test_update_presentation(self):
        """
        Prueba el endpoint para actualizar una presentación.
        """
        presentation = PresentationFactory().build_presentation()
        presentation_data = PresentationFactory().build_presentation_JSON()
        response = self.client.put(
            reverse("presentation-update", kwargs={"slug": presentation.slug}),
            data=presentation_data,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data['name'], presentation_data['name'])
        self.assertEqual(response.data['product'], presentation_data['product'])
        self.assertEqual(response.data['stock'], presentation_data['stock'])
        self.assertEqual(response.data['sku'], presentation_data['sku'])
        self.assertEqual(response.data['bar_code'], presentation_data['bar_code'])
        self.assertEqual(response.data['abbreviation'], presentation_data['abbreviation'])
    
    def test_update_presentation_invalid(self):
        """
        Prueba el endpoint para actualizar una presentación con datos inválidos.
        """
        presentation = PresentationFactory().build_presentation()
        presentation_data = PresentationFactory().build_presentation_invalid()
        response = self.client.put(
            reverse("presentation-update", kwargs={"slug": presentation.slug}),
            data=presentation_data,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("name", response.data)

    def test_delete_presentation(self):
        """
        Prueba el endpoint para eliminar una presentación.
        """
        presentation = PresentationFactory().build_presentation()
        response = self.client.delete(
            reverse("presentation-delete", kwargs={"pk": presentation.id}),
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_delete_presentation_invalid(self):
        """
        Prueba el endpoint para eliminar una presentación con datos inválidos.
        """
        presentation = PresentationFactory().build_presentation()
        response = self.client.delete(
            reverse("presentation-delete", kwargs={"pk": 999}),
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    