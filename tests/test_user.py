"""
Модуль тестов API для управления пользователями.

Содержит тесты для проверки функциональности API, включая:
- Создание новых пользователей.
- Получение списка пользователей.
- Обновление данных пользователей.
- Удаление пользователей.

Тесты используют APIClient для отправки HTTP-запросов к соответствующим эндпоинтам.
"""


from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from users.models import User


class UserAPITest(TestCase):
    """
    Тесты для проверки API управления пользователями.
    """
    def setUp(self) -> None:
        self.client = APIClient()
        self.user_data = {
            "email": "testuser@example.com",
            "name": "Test User",
            "password": "password123"
        }
        self.user = User.objects.create_user(**self.user_data)
        self.client.force_authenticate(user=self.user)

    def test_create_user(self) -> None:
        """
        Тест создания нового пользователя через API.
        """
        new_user_data = {
            "email": "newuser@example.com",
            "name": "New User",
            "password": "newpassword123"
        }
        response = self.client.post('/api/users/', data=new_user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)

    def test_get_user_list(self) -> None:
        """
        Тест получения списка пользователей через API.
        """
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_user(self) -> None:
        """
        Тест обновления данных пользователя через API.
        """
        updated_data = {
            "name": "Updated User",
            "email": self.user.email,
            "password": "password123"
        }
        response = self.client.put(f'/api/users/{self.user.id}/', data=updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.name, updated_data['name'])

    def test_delete_user(self) -> None:
        """
        Тест удаления пользователя через API.
        """
        response = self.client.delete(f'/api/users/{self.user.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.count(), 0)
