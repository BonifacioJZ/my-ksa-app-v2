from faker import Faker
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

faker = Faker()

class TestSetUp(APITestCase):
    """
    Clase base para las pruebas de la API.
    """
    def setUp(self):
        """
        Configuración inicial para las pruebas.
        """
        from src.user.models import UserAccount as User
        self.login_url = reverse('jwt-create')
        self.user = User.objects.create_superuser(
            username=faker.user_name(),
            first_name = 'Developer',
            last_name = 'Test',
            password = 'testpassword',
            email = faker.email(),
        )
        
        response = self.client.post(
            self.login_url,
            {
                'username': self.user.username,
                'password': 'testpassword'
            },
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        return super().setUp()