from django.contrib import admin

from users.models import User
from tasks.models import Task


class UserAdmin(admin.ModelAdmin):
    """
    Настройки отображения модели User в админке.
    """
    list_display = ('id', 'name', 'email', 'is_active', 'is_staff')  # Показывает эти поля в списке пользователей
    search_fields = ('name', 'email')  # Поиск по имени и электронной почте
    list_filter = ('is_active', 'is_staff')  # Фильтры по статусу активности и административной роли


class TaskAdmin(admin.ModelAdmin):
    """
    Настройки отображения модели Task в админке.
    """
    list_display = ('id', 'title', 'description', 'status', 'user')  # Основные поля задачи для отображения
    search_fields = ('title', 'description', 'user__email')  # Поиск по названию, описанию и почте пользователя
    list_filter = ('status',)  # Фильтр по статусу задачи
    raw_id_fields = ('user',)  # Виджет для выбора связанных полей (оптимизация при большом количестве пользователей)


# Регистрация моделей в админке с кастомными настройками
admin.site.register(User, UserAdmin)
admin.site.register(Task, TaskAdmin)
