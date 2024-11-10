"""
ASGI-конфигурация для проекта Task Manager.

Этот модуль инициализирует ASGI-приложение, используемое для обслуживания проекта.
ASGI (асинхронный шлюзовый интерфейс сервера) — стандарт взаимодействия между
асинхронными веб-серверами и приложениями на Python, обеспечивающий масштабируемую и эффективную связь.

ASGI-приложение доступно как переменная уровня модуля с именем `application`.

Подробнее см.:
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""


import os
from typing import Any

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_manager.settings')

application: Any = get_asgi_application()
