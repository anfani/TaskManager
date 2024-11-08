from django.contrib import admin

from users.models import User
from tasks.models import Task


class UserAdmin(admin.ModelAdmin):
    """
    Настройки отображения модели User в админке.

    Attributes:
        list_display (tuple): Поля, которые отображаются в списке пользователей.
        search_fields (tuple): Поля, по которым можно выполнить поиск в админке.
        list_filter (tuple): Поля, используемые для фильтрации пользователей в админке.
    """
    list_display = ('id', 'name', 'email', 'is_active', 'is_staff')
    search_fields = ('name', 'email')
    list_filter = ('is_active', 'is_staff')


class TaskAdmin(admin.ModelAdmin):
    """
    Настройки отображения модели Task в админке.

    Attributes:
        list_display (tuple): Поля, которые отображаются в списке задач.
        search_fields (tuple): Поля, по которым можно выполнить поиск в админке.
        list_filter (tuple): Поля, используемые для фильтрации задач в админке.
        raw_id_fields (tuple): Поля, в которых используется виджет для выбора связанных объектов
            (оптимизация для большого количества пользователей).
    """
    list_display = ('id', 'title', 'description', 'status', 'user')
    search_fields = ('title', 'description', 'user__email')
    list_filter = ('status',)
    raw_id_fields = ('user',)


# Регистрация моделей в админке с кастомными настройками
admin.site.register(User, UserAdmin)
admin.site.register(Task, TaskAdmin)
