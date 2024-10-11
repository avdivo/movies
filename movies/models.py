from django.db import models

class Film(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    release_year = models.IntegerField(verbose_name='Год выпуска')
    director = models.CharField(max_length=255, verbose_name='Режиссер')
    genre = models.CharField(max_length=100, verbose_name='Жанр')
    poster = models.ImageField(upload_to='posters/', verbose_name='Постер')

    def __str__(self):
        return self.title
