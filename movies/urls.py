from django.urls import path
from .views import FilmListView, FilmDetailView, FilmCreateView, FilmUpdateView, FilmDeleteView

urlpatterns = [
    path('', FilmListView.as_view(), name='film-list'),
    path('films/<int:pk>/', FilmDetailView.as_view(), name='film-detail'),
    path('films/add/', FilmCreateView.as_view(), name='film-add'),
    path('films/<int:pk>/edit/', FilmUpdateView.as_view(), name='film-edit'),
    path('films/<int:pk>/delete/', FilmDeleteView.as_view(), name='film-delete'),
]