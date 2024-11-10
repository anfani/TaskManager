"""
Конфигурация URL для проекта task_manager.

Список `urlpatterns` перенаправляет URL-адреса на представления. Дополнительную информацию см. по ссылке:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Примеры:
Функциональные представления
    1. Добавьте импорт:  from my_app import views
    2. Добавьте URL в urlpatterns:  path('', views.home, name='home')
Классовые представления
    1. Добавьте импорт:  from other_app.views import Home
    2. Добавьте URL в urlpatterns:  path('', Home.as_view(), name='home')
Включение другого URLconf
    1. Импортируйте функцию include(): from django.urls import include, path
    2. Добавьте URL в urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from . import views

schema_view = get_schema_view(
    openapi.Info(
        title="My API",
        default_version='v1',
        description="Описание и тестирование вашего API",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    authentication_classes=(),
)


swagger_schema_view = schema_view.with_ui('swagger', cache_timeout=0)


urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('task_description/', views.task_description, name='task_description'),
]
