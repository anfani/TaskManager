# Dockerfile для проекта task_manager

# Используем официальный образ Python в качестве базового
FROM python:3.12-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файл зависимостей в контейнер
COPY requirements.txt /app/

# Устанавливаем зависимости и инструменты для проверки качества кода
RUN pip install --no-cache-dir -r requirements.txt && \
    pip install setuptools flake8==7.1.1 isort==5.13.2

# Копируем весь проект в рабочую директорию контейнера
COPY . /app/

# Устанавливаем переменные окружения для настройки Django
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE task_manager.settings

# Открываем порт для доступа к приложению
EXPOSE 8000

# Команда для запуска приложения
CMD ["gunicorn", "task_manager.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "4"]
