"""
Модуль моделей для приложения Tasks.

Содержит модель Task, которая представляет задачу, связанную с пользователем.
Каждая задача имеет заголовок, описание, статус и привязку к пользователю.
"""


from django.db import models
from users.models import User


class Task(models.Model):
    """
    Модель, представляющая задачу, которую может выполнять пользователь.
    """
    STATUS_CHOICES = [
        ('новая', 'Новая'),
        ('в процессе', 'В процессе'),
        ('завершена', 'Завершена'),
    ]

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='новая')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self) -> str:
        return self.title
