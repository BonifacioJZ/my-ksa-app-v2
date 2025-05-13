from django.urls import reverse
from rest_framework import status
from tests.test_setup import TestSetUp
from ..factories.category_manager.category_factory import CategoryFactory

class CategoryTestCase(TestSetUp):
    def test_find_category(self):
        """
        Test the find category endpoint.
        """
        category = CategoryFactory().build_category()
        response = self.client.get(
            reverse("category-detail", kwargs={"slug": category.slug}),
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        self.assertEqual(response.data['id'], str(category.id))
        self.assertEqual(response.data['name'], category.name)
        self.assertEqual(response.data['slug'], category.slug)
        
    def test_find_category_not_found(self):
        """
        Test the find category endpoint with a non-existent category.
        """
        response = self.client.get(
            reverse("category-detail", kwargs={"slug": "non-existent-category"}),
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_create_category(self):
        """
        Test the create category endpoint.
        """
        category_data = CategoryFactory().build_category_JSON()
        response = self.client.post(
            reverse("category-list-create"),
            data=category_data,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], category_data['name'])
        self.assertEqual(response.data['description'], category_data['description'])
        
    def test_create_category_invalid(self):
        """
        Test the create category endpoint with invalid data.
        """
        category_data = CategoryFactory().build_category_JSON()
        category_data['name'] = ''
        response = self.client.post(
            reverse("category-list-create"),
            data=category_data,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
    def test_update_category(self):
        """
        Test the update category endpoint.
        """
        category = CategoryFactory().build_category()
        updated_data = {
            "name": "Updated Category Name",
            "description": "Updated Category Description",
        }
        response = self.client.put(
            reverse("category-update", kwargs={"slug": category.slug}),
            data=updated_data,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], updated_data['name'])
        self.assertEqual(response.data['description'], updated_data['description'])
    def test_update_category_not_found(self):
        """
        Test the update category endpoint with a non-existent category.
        """
        updated_data = {
            "name": "Updated Category Name",
            "description": "Updated Category Description",
        }
        response = self.client.put(
            reverse("category-update", kwargs={"slug": "non-existent-category"}),
            data=updated_data,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_delete_category(self):
        """
        Test the delete category endpoint.
        """
        category = CategoryFactory().build_category()
        response = self.client.delete(
            reverse("category-delete", kwargs={"pk": category.pk}),
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(category._state.db == None)
        with self.assertRaises(category.DoesNotExist):
            category.refresh_from_db()

    def test_delete_category_not_found(self):
        """
        Test the delete category endpoint with a non-existent category.
        """
        response = self.client.delete(
            reverse("category-delete", kwargs={"pk": 999}),
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)