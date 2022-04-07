import os

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Actor(models.Model):
    GENDERS = [
        ('Male', 'Erkak'),
        ('Female', 'Ayol'),
    ]

    first_name = models.CharField(max_length=50, verbose_name='Ismi')
    last_name = models.CharField(max_length=50, verbose_name='Familiyasi')
    birthdate = models.DateField(verbose_name="Tug`ilgan sanasi")
    gender = models.CharField(max_length=30, choices=GENDERS, verbose_name='Jinsi')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Movie(models.Model):
    FILM_GENRES = [
        ('Horror', 'Qo`rqinchli'),
        ('Comedy', 'Komediya'),
        ('Adventure', 'Sarguzasht'),
        ('Romace', 'Romantika'),
        ('Historical', 'Tarixiy'),
    ]

    title = models.CharField(max_length=100, verbose_name="Sarlavhasi")
    actors = models.ManyToManyField(Actor)
    year = models.PositiveIntegerField(verbose_name="Chiqarilgan yili")
    imdb = models.IntegerField(verbose_name="IMDB")
    genre = models.CharField(max_length=30, choices=FILM_GENRES, verbose_name='Kino janri')

    def __str__(self):
        return self.title


class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)


