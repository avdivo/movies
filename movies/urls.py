from django.urls import path
from .views import (
    film_list_view,
    film_detail_view,
    film_create_view,
    film_update_view,
    film_delete_view
)

urlpatterns = [
    path('', film_list_view, name='film-list'),  # Главная страница - список фильмов
    path('films/<int:pk>/', film_detail_view, name='film-detail'),  # Страница деталей фильма
    path('films/add/', film_create_view, name='film-add'),  # Страница добавления фильма
    path('films/<int:pk>/edit/', film_update_view, name='film-edit'),  # Страница редактирования фильма
    path('films/<int:pk>/delete/', film_delete_view, name='film-delete'),  # Страница удаления фильма
]
