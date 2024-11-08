from rest_framework import serializers
from tasks.models import Task


class TaskSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели задачи.
    """

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'user']
