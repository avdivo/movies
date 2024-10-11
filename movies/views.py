from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import FilmSerializer
from django.shortcuts import render, get_object_or_404, redirect
from .models import Film
from .forms import FilmForm


# Вьюха для отображения списка фильмов
def film_list_view(request):
    """
    Отображает список всех фильмов.
    """
    films = Film.objects.all()  # Получаем все фильмы из базы данных
    context = {
        'films': films  # Передаем фильмы в контекст
    }
    return render(request, 'movies/films_list.html', context)  # Рендерим шаблон

# Вьюха для отображения деталей фильма
def film_detail_view(request, pk):
    """
    Отображает детали конкретного фильма по его ID.
    """
    film = get_object_or_404(Film, pk=pk)  # Получаем фильм по ID или 404
    context = {
        'film': film  # Передаем фильм в контекст
    }
    return render(request, 'movies/film_detail.html', context)  # Рендерим шаблон

# Вьюха для создания нового фильма
def film_create_view(request):
    """
    Обрабатывает создание нового фильма.
    """
    if request.method == 'POST':  # Если метод POST, значит отправили форму
        form = FilmForm(request.POST, request.FILES)  # Создаем форму с данными
        if form.is_valid():  # Проверяем валидность формы
            form.save()  # Сохраняем новый фильм в базу данных
            return redirect('film-list')  # Перенаправляем на список фильмов
    else:
        form = FilmForm()  # Создаем пустую форму для GET-запроса

    context = {
        'form': form  # Передаем форму в контекст
    }
    return render(request, 'movies/film_form.html', context)  # Рендерим шаблон

# Вьюха для редактирования фильма
def film_update_view(request, pk):
    """
    Обрабатывает редактирование существующего фильма.
    """
    film = get_object_or_404(Film, pk=pk)  # Получаем фильм по ID
    if request.method == 'POST':  # Если метод POST, значит отправили форму
        form = FilmForm(request.POST, request.FILES, instance=film)  # Создаем форму с данными
        if form.is_valid():  # Проверяем валидность формы
            form.save()  # Сохраняем изменения в базе данных
            return redirect('film-list')  # Перенаправляем на список фильмов
    else:
        form = FilmForm(instance=film)  # Создаем форму с текущими данными фильма

    context = {
        'form': form,  # Передаем форму в контекст
        'film': film  # Передаем фильм в контекст
    }
    return render(request, 'movies/film_form.html', context)  # Рендерим шаблон

# Вьюха для удаления фильма
def film_delete_view(request, pk):
    """
    Обрабатывает удаление существующего фильма.
    """
    film = get_object_or_404(Film, pk=pk)  # Получаем фильм по ID
    if request.method == 'POST':  # Если метод POST, значит пользователь подтвердил удаление
        film.delete()  # Удаляем фильм
        return redirect('film-list')  # Перенаправляем на список фильмов

    context = {
        'film': film  # Передаем фильм в контекст
    }
    return render(request, 'movies/film_confirm_delete.html', context)  # Рендерим шаблон

# Вьюха для API (остается без изменений)
class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]
