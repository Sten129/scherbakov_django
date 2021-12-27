from django.db import models
from django.contrib.auth import get_user_model
import datetime

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


class Type(models.Model):
    name = models.CharField('Тип работы', unique=True, max_length=20)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ('-name',)
        verbose_name = 'Type'
        verbose_name_plural = 'Type'

    def __str__(self):
        return self.name


class Technic(models.Model):
    name = models.CharField('Техника', unique=True, max_length=20)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ('-name',)
        verbose_name = 'Technic'
        verbose_name_plural = 'Technics'

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField('Локация', unique=True, max_length=20)
    image = models.ImageField(verbose_name='Изображение', upload_to='locations/')
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ('-name',)
        verbose_name = 'Technic'
        verbose_name_plural = 'Technics'

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=500, verbose_name='Название')
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=False, verbose_name='место издания')
    year = models.DateField(verbose_name='Дата', default=datetime.date.today)
    pub_house = models.CharField(max_length=500, verbose_name='издательство')
    isbn = models.CharField(verbose_name='ISBN', max_length=14)
    pdf = models.FileField
    description = models.TextField(max_length=1000, verbose_name='описание')
    image = models.ImageField(verbose_name='Изображение', upload_to='books/')
    slug = models.SlugField(null=False, unique=False, help_text='URL')


class Photo(models.Model):
    pass


class Persone(models.Model):
    name = models.CharField(max_length=200, verbose_name='имя')
    birth = models.DateField(verbose_name='Дата рождения', default=datetime.date.today)
    death = models.DateField(verbose_name='Дата смерти', default=datetime.date.today)
    description = models.TextField(max_length=1000, verbose_name='Описание')
    link = models.URLField
    # provenance = models.ForeignKey(Owner, on_delete=models.CASCADE, null=True)
    publishing = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
    # letter = models.ForeignKey(Letter, on_delete=models.CASCADE, null=True, related_name='letter')
    # event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True, related_name='event')
    image = models.ImageField(verbose_name='Изображение', upload_to='persons/')
    slug = models.SlugField(unique=True, help_text='URL')


class Owner(models.Model):
    name = models.CharField(max_length=500, verbose_name='Название или имя')
    persone = models.ForeignKey(Persone, null=True, on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='Изображение', upload_to='owners/')
    slug = models.SlugField(unique=True, help_text='URL')


class Letter(models.Model):
    title = models.CharField(max_length=500, verbose_name='Название')
    from_who = models.CharField(max_length=500, verbose_name='От кого')
    to = models.CharField(max_length=500, verbose_name='Кому')
    location = models.ForeignKey(Location, on_delete=models.CASCADE, verbose_name='Локация')
    date = models.DateField(verbose_name='Дата', default=datetime.date.today)
    persons = models.ForeignKey(Persone, on_delete=models.CASCADE, verbose_name='Люди')
    pdf = models.FileField(verbose_name='PDF-файл')
    image = models.ImageField(verbose_name='Изображение', upload_to='letters/')
    slug = models.SlugField(unique=True, help_text='URL')


class Document(models.Model):
    title = models.CharField(max_length=500, verbose_name='Название')
    type = models.CharField(max_length=100, verbose_name='Тип документа')
    date = models.DateField(verbose_name='Дата', default=datetime.date.today)
    # event = models.ForeignKey
    location = models.ForeignKey(Location, on_delete=models.CASCADE, verbose_name='Локация')
    persons = models.ForeignKey(Persone, on_delete=models.CASCADE, verbose_name='Люди')
    image = models.ImageField(verbose_name='Изображение', upload_to='docs/')
    slug = models.SlugField(unique=True, help_text='URL')
    pass


class Exhibition(models.Model):
    title = models.CharField(max_length=500, verbose_name='Название')
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=False, verbose_name='Локация')
    date = models.DateField(verbose_name='Дата', default=datetime.date.today)
    # pictures = models.ForeignKey(Picture, on_delete=models.CASCADE, null=False, related_name='pictures')
    persons = models.ForeignKey(Persone, on_delete=models.CASCADE, null=True, verbose_name='Люди')
    publishing = models.ForeignKey(Book, on_delete=models.CASCADE, null=True, verbose_name='Издания')
    docs = models.ForeignKey(Document, on_delete=models.CASCADE, null=True, verbose_name='Документы')
    description = models.TextField(max_length=1000, verbose_name='Описание')
    image = models.ImageField(verbose_name='Изображение', upload_to='exhibitions/')
    slug = models.SlugField(null=False, unique=False, help_text='URL')


class Picture(models.Model):
    title = models.CharField(max_length=500, verbose_name='Название')
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='type', verbose_name='Тип')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, null=False, help_text='Жанр')
    year = models.DateField(verbose_name='Год', default=datetime.date.today)
    technic = models.ForeignKey(Technic, on_delete=models.CASCADE)
    size = models.IntegerField(verbose_name='Размер', null=True)
    publishing = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
    provenance = models.ForeignKey(Owner, on_delete=models.CASCADE, null=True)
    # event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True, related_name='event')
    exhibition = models.ForeignKey(Exhibition, on_delete=models.CASCADE, verbose_name='Выставки')
    image = models.ImageField(verbose_name='Изображение', upload_to='pictures/')

class Article(models.Model):
   title = models.CharField(max_length=500, verbose_name='Название')
   text = models.TextField(verbose_name='Текст')
   author = models.ForeignKey(Persone, on_delete=models.CASCADE, blank=True, verbose_name='Автор')
   date = models.DateField(verbose_name='Дата', auto_now=datetime.date.today())
   exhibition = models.ForeignKey(Exhibition, on_delete=models.CASCADE, blank=True, verbose_name='Выставки')
   picture = models.ForeignKey(Picture, on_delete=models.CASCADE, blank=True, verbose_name='Работы')
   # image = models.ImageField
   slug = models.SlugField(null=False, unique=True, help_text='URL')


class Event(models.Model):
    pass
