# task_manager/views.py

from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def task_description(request):
    return render(request, 'task_description.html')
