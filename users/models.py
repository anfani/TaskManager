from django.db import models

class User(models.Model):
    """
    Модель, представляющая пользователя системы.
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name

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

    def __str__(self):
        return self.title
