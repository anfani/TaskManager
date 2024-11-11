"""
Модуль моделей для приложения Tasks.

Содержит модель Task, которая представляет задачу, связанную с пользователем.
Каждая задача имеет заголовок, описание, статус и привязку к пользователю.
"""


from django.db import models
from enum import Enum
from users.models import User

class TaskStatus(Enum):
    NEW = 'новая'
    IN_PROGRESS = 'в процессе'
    COMPLETED = 'завершена'

    @classmethod
    def choices(cls):
        """
        Возвращает статусы в формате, подходящем для поля choices Django.
        """
        return [(tag.value, tag.name.capitalize()) for tag in cls]

class Task(models.Model):
    """
    Модель, представляющая задачу, которую может выполнять пользователь.
    """
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=TaskStatus.choices(),  # Использование статусов из Enum
        default=TaskStatus.NEW.value  # Установка значения по умолчанию через Enum
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self) -> str:
        return self.title

