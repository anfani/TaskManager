"""
Модуль маршрутов (URLs) для API приложения Task Manager.

Содержит:
- Регистрацию маршрутов для моделей User и Task с использованием DefaultRouter.
- Маршруты для работы с JWT-аутентификацией, включая получение и обновление токенов.

Маршруты:
- `/users/`: управление пользователями.
- `/tasks/`: управление задачами.
- `/token/`: получение JWT-токена.
- `/token/refresh/`: обновление JWT-токена.
"""

from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from .views import TaskViewSet, UserViewSet

# Создаем роутер для управления URL API.
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'tasks', TaskViewSet, basename='task')

# Определение URL-шаблонов для приложения.
urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
