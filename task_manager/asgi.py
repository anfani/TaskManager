"""
ASGI конфигурация для проекта task_manager.

Этот модуль содержит ASGI-приложение, используемое для обслуживания вашего проекта.
Он предоставляет вызов ASGI на уровне модуля, который называется "application".

ASGI (Асинхронный шлюзовый интерфейс сервера) — это стандарт для асинхронных веб-серверов и приложений на Python,
и предоставляет интерфейс между ними.

Для получения дополнительной информации об этом файле, см.
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os
from typing import Any

from django.core.asgi import get_asgi_application

# Установка переменной окружения для модуля настроек проекта.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_manager.settings')

# Получение ASGI-приложения.
application: Any = get_asgi_application()
