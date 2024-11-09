"""
Конфигурация приложения Users.

Определяет базовые настройки приложения, включая имя приложения
и тип автоматического поля для первичных ключей моделей.
"""


from django.apps import AppConfig


class UsersConfig(AppConfig):
    """
    Конфигурация приложения 'users'.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
