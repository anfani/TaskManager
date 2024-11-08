"""
Настройки Django для проекта task_manager.

Создано с помощью 'django-admin startproject' с использованием версии Django 5.1.2.

Для получения дополнительной информации об этом файле, см.
https://docs.djangoproject.com/en/5.1/topics/settings/

Полный список настроек и их значений можно найти здесь:
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

import os
from datetime import timedelta

from dotenv import load_dotenv
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

load_dotenv()

# Определение базового пути к проекту.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Основные настройки разработки - не подходят для использования в продакшене.
# Дополнительная информация: https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# Секретный ключ. Храните его в тайне в продакшене!
SECRET_KEY = os.getenv('SECRET_KEY')

# Настройка режима отладки. Не используйте режим отладки в продакшене!
DEBUG = True

# Разрешенные хосты для проекта.
ALLOWED_HOSTS = []

# Определение установленных приложений.
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'users',
    'tasks',
    'drf_yasg',
]

# Пользовательская модель пользователя.
AUTH_USER_MODEL = 'users.User'

# Определение используемых промежуточных программ (middleware).
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Основной URL-конфигурационный файл проекта.
ROOT_URLCONF = 'task_manager.urls'

# Определение шаблонов.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # Путь к корневой папке с шаблонами.
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Определение WSGI приложения.
WSGI_APPLICATION = 'task_manager.wsgi.application'

# Настройки базы данных.
# Подробнее: https://docs.djangoproject.com/en/5.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Валидация паролей.
# Подробнее: https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Интернационализация.
# Подробнее: https://docs.djangoproject.com/en/5.1/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Статические файлы (CSS, JavaScript, Изображения).
# Подробнее: https://docs.djangoproject.com/en/5.1/howto/static-files/
STATIC_URL = 'static/'

# Тип первичного ключа по умолчанию.
# Подробнее: https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Настройки Django REST Framework (DRF).
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}

# Настройки JWT токенов.
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'AUTH_HEADER_TYPES': ('Bearer',),
}

# Настройки Swagger для автоматической документации API.
SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization',
            'description': 'Введите JWT токен с префиксом "Bearer ", например: Bearer <ваш_токен>',
        },
    },
}

# Определение схемы представления для Swagger.
schema_view = get_schema_view(
    openapi.Info(
        title="My API",
        default_version='v1',
        description="Описание вашего API",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
