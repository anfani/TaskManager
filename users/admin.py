from django.contrib import admin
from .models import User, Task

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'is_active', 'is_staff')  # Показывает эти поля в списке пользователей
    search_fields = ('name', 'email')  # Позволяет искать по имени и электронной почте
    list_filter = ('is_active', 'is_staff')  # Добавляет фильтры справа

class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'status', 'user')  # Показывает основные поля задачи
    search_fields = ('title', 'description', 'user__email')  # Поиск по названию, описанию и электронной почте пользователя
    list_filter = ('status',)  # Фильтр для статуса задачи
    raw_id_fields = ('user',)  # Использование виджета выбора для связанных полей

# Регистрируем кастомные классы для отображения в админке
admin.site.register(User, UserAdmin)
admin.site.register(Task, TaskAdmin)
