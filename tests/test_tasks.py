from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from users.models import User
from tasks.models import Task


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
        self.task = Task.objects.create(
            user=self.user,
            title=self.task_data['title'],
            description=self.task_data['description'],
            status=self.task_data['status']
        )

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

