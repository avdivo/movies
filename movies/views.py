from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Film
from .forms import FilmForm

class FilmListView(ListView):
    model = Film
    template_name = 'movies/films_list.html'
    context_object_name = 'films'

class FilmDetailView(DetailView):
    model = Film
    template_name = 'movies/film_detail.html'

class FilmCreateView(CreateView):
    model = Film
    form_class = FilmForm
    template_name = 'movies/film_form.html'
    success_url = reverse_lazy('film-list')

class FilmUpdateView(UpdateView):
    model = Film
    form_class = FilmForm
    template_name = 'movies/film_form.html'
    success_url = reverse_lazy('film-list')

class FilmDeleteView(DeleteView):
    model = Film
    template_name = 'movies/film_confirm_delete.html'
    success_url = reverse_lazy('film-list')
