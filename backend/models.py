from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Genre(models.Model):
    name = models.CharField('Название жанра', unique=True, max_length=20)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ('-name',)
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'

    def __str__(self):
        return self.name


class Picture(models.Model):
   pass

class Photo(models.Model):
    pass

class Letter(models.Model):
    pass

class Document(models.Model):
    pass

class Exhibition(models.Model):
    pass

class Book(models.Model):
    pass

class Persone(models.Model):
    pass

class Type(models.Model):
    pass

class Descripton(models.Model):
    pass

class Location(models.Model):
    pass

class Event(models.Model):
    pass
