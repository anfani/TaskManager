from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from users.models import User


class AuthenticationTest(TestCase):
    """
    Тесты для проверки аутентификации.
    """
    def setUp(self) -> None:
        self.client = APIClient()
        self.user_data = {
            "email": "authuser@example.com",
            "name": "Auth User",
            "password": "password123"
        }
        self.user = User.objects.create_user(**self.user_data)

    def test_access_protected_route_without_authentication(self) -> None:
        """
        Тест доступа к защищенному маршруту без аутентификации.
        """
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_access_protected_route_with_authentication(self) -> None:
        """
        Тест доступа к защищенному маршруту с аутентификацией.
        """
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_token_authentication(self) -> None:
        """
        Тест получения JWT токена.
        """
        response = self.client.post('/api/token/', {"email": self.user.email, "password": "password123"}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)


class InputValidationTest(TestCase):
    """
    Тесты для проверки валидации ввода.
    """
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create_user(
            email="validationuser@example.com",
            name="Validation User",
            password="password123"
        )

        self.client.force_authenticate(user=self.user)

    def test_create_task_with_missing_fields(self) -> None:
        """
        Тест создания задачи с отсутствующими обязательными полями.
        """
        invalid_data = {
            "description": "Missing title field",
        }
        response = self.client.post('/api/tasks/', data=invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('title', response.data)

    def test_create_user_with_invalid_email(self) -> None:
        """
        Тест создания пользователя с некорректным email.
        """
        invalid_user_data = {
            "email": "not-an-email",
            "name": "Invalid Email User",
            "password": "password123"
        }
        response = self.client.post('/api/users/', data=invalid_user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('email', response.data)


class CoreRoutesTest(TestCase):
    """
    Тесты для проверки основных маршрутов.
    """
    def setUp(self) -> None:
        self.client = APIClient()

    def test_index_page(self) -> None:
        """
        Тест главной страницы.
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_task_description_page(self) -> None:
        """
        Тест страницы описания задачи.
        """
        response = self.client.get('/task_description/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
