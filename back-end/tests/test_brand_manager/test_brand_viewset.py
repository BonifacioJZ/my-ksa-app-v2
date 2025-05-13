from django.urls import reverse
from rest_framework import status
from tests.test_setup import TestSetUp
from ..factories.brand_manager.brand_factory import BrandFactory


class BrandTestCase(TestSetUp):
    def test_find_brand(self):
        """
        Test the find brand endpoint.
        """
        brand = BrandFactory().build_brand()
        response = self.client.get(
            reverse("brand-detail",kwargs={"slug": brand.slug}),
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        self.assertEqual(response.data['id'], str(brand.id))
        self.assertEqual(response.data['name'], brand.name)
        self.assertEqual(response.data['slug'], brand.slug)
        
    def test_find_brand_not_found(self):
        """
        Test the find brand endpoint with a non-existent brand.
        """
        response = self.client.get(
            reverse("brand-detail", kwargs={"slug": "non-existent-brand"}),
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_create_brand(self):
        """
        Test the create brand endpoint.
        """
        brand_data = BrandFactory().build_brand_JSON()
        response = self.client.post(
            reverse("brand-list-create"),
            data = brand_data,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], brand_data['name'])
    
    def test_create_brand_invalid(self):
        """
        Test the create brand endpoint with invalid data.
        """
        brand_data = BrandFactory().build_brand_JSON()
        brand_data['name'] = ''
        response = self.client.post(
            reverse("brand-list-create"),
            data = brand_data,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('name', response.data)
        
    def test_update_brand(self):
        """
        Test the update brand endpoint.
        """
        brand = BrandFactory().build_brand()
        updated_data = {
            "name": "Updated Brand Name",
        }
        response = self.client.patch(
            reverse("brand-update", kwargs={"slug": brand.slug}),
            data=updated_data,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], updated_data['name'])
        self.assertEqual(response.data['slug'], brand.slug)
        brand.refresh_from_db()
        self.assertEqual(brand.name, updated_data['name'])
        
    def test_update_brand_not_found(self):
        """
        Test the update brand endpoint with a non-existent brand.
        """
        updated_data = {
            "name": "Updated Brand Name",
        }
        response = self.client.patch(
            reverse("brand-update", kwargs={"slug": "non-existent-brand"}),
            data=updated_data,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    def test_delete_brand(self):
        """
        Test the delete brand endpoint.
        """
        brand = BrandFactory().build_brand()
        response = self.client.delete(
            reverse("brand-delete", kwargs={"pk": brand.pk}),
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(brand._state.db == None)
        with self.assertRaises(brand.DoesNotExist):
            brand.refresh_from_db()
    def test_delete_brand_not_found(self):
        """
        Test the delete brand endpoint with a non-existent brand.
        """
        response = self.client.delete(
            reverse("brand-delete", kwargs={"pk": "non-existent-brand"}),
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)   