from django.urls import path
from .views import FilmListView, FilmDetailView, FilmCreateView, FilmUpdateView, FilmDeleteView

urlpatterns = [
    path('', FilmListView.as_view(), name='film-list'),  # Главная страница
    path('films/<int:pk>/', FilmDetailView.as_view(), name='film-detail'),  # Страница деталей фильма
    path('films/add/', FilmCreateView.as_view(), name='film-add'),  # Страница добавления фильма
    path('films/<int:pk>/edit/', FilmUpdateView.as_view(), name='film-edit'),  # Страница редактирования фильма
    path('films/<int:pk>/delete/', FilmDeleteView.as_view(), name='film-delete'),  # Страница удаления фильма
]
