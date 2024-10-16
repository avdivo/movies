# Generated by Django 5.1.2 on 2024-10-11 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('release_year', models.IntegerField(verbose_name='Год выпуска')),
                ('director', models.CharField(max_length=255, verbose_name='Режиссер')),
                ('genre', models.CharField(max_length=100, verbose_name='Жанр')),
                ('poster', models.ImageField(upload_to='posters/', verbose_name='Постер')),
            ],
        ),
    ]
