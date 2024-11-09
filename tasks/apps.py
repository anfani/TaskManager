"""
Конфигурация приложения Tasks.

Этот модуль определяет конфигурацию приложения Tasks, включая настройки имени
и автоматического поля первичного ключа по умолчанию.
"""


from django.apps import AppConfig


class TasksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tasks'
