from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Task, User
from .serializers import TaskSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'delete', 'put']

    def get_queryset(self):
        # Проверяем, является ли это вызовом Swagger
        if getattr(self, 'swagger_fake_view', False):
            return User.objects.none()  # Возвращаем пустой QuerySet для Swagger

        # Возвращаем всех пользователей (для аутентифицированных пользователей)
        return User.objects.all()

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'delete', 'put']

    def get_queryset(self):
        # Проверяем, является ли это вызовом Swagger
        if getattr(self, 'swagger_fake_view', False):
            return Task.objects.none()  # Возвращаем пустой QuerySet для Swagger

        # Фильтруем задачи по текущему пользователю
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
