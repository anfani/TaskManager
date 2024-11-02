from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import User, Task


class UserAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            "email": "testuser@example.com",
            "name": "Test User",
            "password": "password123"
        }
        self.user = User.objects.create_user(**self.user_data)
        self.client.force_authenticate(user=self.user)

    def test_create_user(self):
        new_user_data = {
            "email": "newuser@example.com",
            "name": "New User",
            "password": "newpassword123"
        }
        response = self.client.post('/api/users/', data=new_user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)

    def test_get_user_list(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_user(self):
        updated_data = {
            "name": "Updated User",
            "email": self.user.email,  # Обязательно указываем email, так как он является уникальным полем
            "password": "password123"  # Добавляем пароль, так как он обязателен для обновления
        }
        response = self.client.put(f'/api/users/{self.user.id}/', data=updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.name, updated_data['name'])

    def test_delete_user(self):
        response = self.client.delete(f'/api/users/{self.user.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.count(), 0)


class TaskAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(email="taskuser@example.com", name="Task User", password="password123")
        self.client.force_authenticate(user=self.user)
        self.task_data = {
            "title": "Test Task",
            "description": "Test Description",
            "status": "новая"
        }
        self.task = Task.objects.create(user=self.user, title=self.task_data['title'], description=self.task_data['description'], status=self.task_data['status'])

    def test_create_task(self):
        create_data = {
            "title": "New Task",
            "description": "New Task Description",
            "status": "новая",
            "user": self.user.id
        }
        response = self.client.post('/api/tasks/', data=create_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 2)

    def test_get_task_list(self):
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_task(self):
        updated_data = {
            "title": "Updated Task Title",
            "description": "Updated Description",
            "status": "в процессе",
            "user": self.user.id  # Добавляем поле user, так как оно обязательно для обновления
        }
        response = self.client.put(f'/api/tasks/{self.task.id}/', data=updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, updated_data['title'])
        self.assertEqual(self.task.status, updated_data['status'])

    def test_delete_task(self):
        response = self.client.delete(f'/api/tasks/{self.task.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)


class AuthenticationTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            "email": "authuser@example.com",
            "name": "Auth User",
            "password": "password123"
        }
        self.user = User.objects.create_user(**self.user_data)

    def test_access_protected_route_without_authentication(self):
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_access_protected_route_with_authentication(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_token_authentication(self):
        response = self.client.post('/api/token/', {"email": self.user.email, "password": "password123"}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)


class InputValidationTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(email="validationuser@example.com", name="Validation User", password="password123")
        self.client.force_authenticate(user=self.user)

    def test_create_task_with_missing_fields(self):
        invalid_data = {
            "description": "Missing title field",
        }
        response = self.client.post('/api/tasks/', data=invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('title', response.data)

    def test_create_user_with_invalid_email(self):
        invalid_user_data = {
            "email": "not-an-email",
            "name": "Invalid Email User",
            "password": "password123"
        }
        response = self.client.post('/api/users/', data=invalid_user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('email', response.data)


class CoreRoutesTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_index_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_task_description_page(self):
        response = self.client.get('/task_decription/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
