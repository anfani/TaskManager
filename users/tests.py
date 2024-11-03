from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import User, Task


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


class TaskAPITest(TestCase):
    """
    Тесты для проверки API управления задачами.
    """
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create_user(email="taskuser@example.com", name="Task User", password="password123")
        self.client.force_authenticate(user=self.user)
        self.task_data = {
            "title": "Test Task",
            "description": "Test Description",
            "status": "новая"
        }
        self.task = Task.objects.create(user=self.user, title=self.task_data['title'], description=self.task_data['description'], status=self.task_data['status'])

    def test_create_task(self) -> None:
        """
        Тест создания новой задачи через API.
        """
        create_data = {
            "title": "New Task",
            "description": "New Task Description",
            "status": "новая",
            "user": self.user.id
        }
        response = self.client.post('/api/tasks/', data=create_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 2)

    def test_get_task_list(self) -> None:
        """
        Тест получения списка задач через API.
        """
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_task(self) -> None:
        """
        Тест обновления данных задачи через API.
        """
        updated_data = {
            "title": "Updated Task Title",
            "description": "Updated Description",
            "status": "в процессе",
            "user": self.user.id
        }
        response = self.client.put(f'/api/tasks/{self.task.id}/', data=updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, updated_data['title'])
        self.assertEqual(self.task.status, updated_data['status'])

    def test_delete_task(self) -> None:
        """
        Тест удаления задачи через API.
        """
        response = self.client.delete(f'/api/tasks/{self.task.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)


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
        self.user = User.objects.create_user(email="validationuser@example.com", name="Validation User", password="password123")
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
