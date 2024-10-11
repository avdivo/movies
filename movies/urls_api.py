# movies/urls_api.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FilmViewSet

router = DefaultRouter()
router.register(r'films', FilmViewSet, basename='api-films')  # Укажите базовое имя для маршрута

urlpatterns = [
    path('', include(router.urls)),  # API маршруты
]