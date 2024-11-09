"""
Модуль сериализаторов для API приложения Task Manager.

Содержит:
- UserSerializer: сериализатор для модели пользователя. Поддерживает создание
  нового пользователя с зашифрованным паролем и позволяет безопасно работать с данными.
- TaskSerializer: сериализатор для модели задачи, предоставляющий преобразование данных
  задач в формат JSON и обратно.
"""


from rest_framework import serializers
from tasks.models import Task
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели пользователя.
    """

    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data: dict) -> User:
        """
        Создает нового пользователя с зашифрованным паролем.

        Args:
            validated_data (dict): Проверенные данные пользователя.

        Returns:
            User: Созданный пользователь.
        """
        user = User.objects.create_user(**validated_data)
        return user


class TaskSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели задачи.
    """

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'user']
