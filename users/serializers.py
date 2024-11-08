from rest_framework import serializers

from users.models import User
from tasks.models import Task


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
