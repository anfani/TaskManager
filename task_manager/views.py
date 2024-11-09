"""
Модуль представлений (views) для приложения Task Manager.

Содержит функции-обработчики HTTP-запросов, возвращающие соответствующие HTML-страницы.
Каждая функция принимает запрос пользователя и возвращает ответ в виде отрендеренной страницы.
"""


from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    """
    Главная страница приложения.

    Args:
        request (HttpRequest): HTTP запрос пользователя.

    Returns:
        HttpResponse: HTML-страница 'index.html'.
    """
    return render(request, 'index.html')


def task_description(request: HttpRequest) -> HttpResponse:
    """
    Страница с описанием задач.

    Args:
        request (HttpRequest): HTTP запрос пользователя.

    Returns:
        HttpResponse: HTML-страница 'task_description.html'.
    """
    return render(request, 'task_description.html')
