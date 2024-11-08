from rest_framework import serializers

from users.models import User
from tasks.models import Task

class TaskSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели задачи.
    """

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'user']
