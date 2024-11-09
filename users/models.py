"""
Модуль моделей пользователей для приложения Users.

Содержит пользовательскую модель User и менеджер CustomUserManager:
- User: настраиваемая модель пользователя, заменяющая стандартную модель Django.
  Пользователи идентифицируются по email, включают базовые поля и права доступа.
- CustomUserManager: менеджер модели пользователя, предоставляющий методы для создания
  обычных пользователей и суперпользователей.

Модель User совместима с системой аутентификации Django.
"""

from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models


class CustomUserManager(BaseUserManager):
    """
    Менеджер для пользовательской модели User.
    """

    def create_user(self, email: str, password: str = None, **extra_fields) -> 'User':
        """
        Создает и сохраняет пользователя с указанным email и паролем.

        Args:
            email (str): Адрес электронной почты пользователя.
            password (str, optional): Пароль пользователя.
            **extra_fields: Дополнительные поля пользователя.

        Returns:
            User: Созданный пользователь.
        """
        if not email:
            raise ValueError('Email должен быть указан')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  # Шифрует пароль
        user.save(using=self._db)
        return user

    def create_superuser(self, email: str, password: str = None, **extra_fields) -> 'User':
        """
        Создает и сохраняет суперпользователя с указанным email и паролем.

        Args:
            email (str): Адрес электронной почты суперпользователя.
            password (str, optional): Пароль суперпользователя.
            **extra_fields: Дополнительные поля пользователя.

        Returns:
            User: Созданный суперпользователь.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    Модель, представляющая пользователя системы.
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self) -> str:
        return self.name
