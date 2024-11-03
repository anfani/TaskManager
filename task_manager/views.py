# task_manager/views.py

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


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
