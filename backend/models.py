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


class Type(models.Model):
    name = models.CharField('Тип данных', unique=True, max_length=20)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ('-name',)
        verbose_name = 'Type'
        verbose_name_plural = 'Type'

    def __str__(self):
        return self.name
    pass

class Technic(models.Model):
    name = models.CharField('Техника', unique=True, max_length=20)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ('-name',)
        verbose_name = 'Technic'
        verbose_name_plural = 'Technics'

    def __str__(self):
        return self.name
    pass

class Location(models.Model):
    name = models.CharField('Локация', unique=True, max_length=20)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ('-name',)
        verbose_name = 'Technic'
        verbose_name_plural = 'Technics'

    def __str__(self):
        return self.name
    pass


class Book(models.Model):
    title = models.CharField(max_length=500, verbose_name='Название')
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=False )
    year = models.DateField(verbose_name='Дата')
    pub_house = models.CharField(max_length=500, verbose_name='издательство')
    isbn = models.CharField(verbose_name='ISBN', max_length=14)
    pdf = models.FileField
    description = models.TextField(max_length=1000, verbose_name='описание')
    image = models.ImageField
    slug = models.SlugField(null=False, unique=False, help_text='URL')

    pass

class Photo(models.Model):
    pass

class Owner(models.Model):
    # нужно унаследовать класс от Persone или правильно спопоставить его с ним
    # name = models.ForeignKey(Persone, on_delete=models.CASCADE, related_name='persone')
    slug = models.SlugField(null=False,
        unique=True,
        help_text='URL')
    pass

class Persone(models.Model):
    name = models.CharField(max_length=200, verbose_name='имя')
    birth = models.DateField(verbose_name='Дата рождения')
    death = models.DateField(verbose_name='Дата смерти')
    description = models.TextField(max_length=1000, verbose_name='Описание')
    link = models.URLField
    provenance = models.ForeignKey(Owner, on_delete=models.CASCADE, null=True)
    publishing = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
    # letter = models.ForeignKey(Letter, on_delete=models.CASCADE, null=True, related_name='letter')
    # event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True, related_name='event')
    image = models.ImageField
    slug = models.SlugField(null=False, unique=False, help_text='URL')
    pass

class Letter(models.Model):
    title = models.CharField(max_length=500, verbose_name='Название')
    from_who = models.CharField(max_length=500, verbose_name='От кого')
    to = models.CharField(max_length=500, verbose_name='Кому')
    location = models.ForeignKey(Location, on_delete=models.CASCADE, verbose_name='Локация')
    date = models.DateField
    persons = models.ForeignKey(Persone, on_delete=models.CASCADE)
    pdf = models.FileField
    image = models.ImageField
    slug = models.SlugField(null=False, unique=False, help_text='URL')
    pass

class Document(models.Model):
    title = models.CharField(max_length=500, )
    pass

class Exhibition(models.Model):
    title = models.CharField(max_length=500, verbose_name='Название')
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=False )
    date = models.DateField(verbose_name='Дата')
    # pictures = models.ForeignKey(Picture, on_delete=models.CASCADE, null=False, related_name='pictures')
    persons = models.ForeignKey(Persone, on_delete=models.CASCADE, null=True)
    publishing = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
    docs = models.ForeignKey(Document, on_delete=models.CASCADE, null=True)
    description = models.TextField(max_length=1000, verbose_name='Описание')
    image = models.ImageField()
    slug = models.SlugField(null=False, unique=False, help_text='URL')
    pass

class Picture(models.Model):
   title = models.CharField(max_length=500, verbose_name='Название')
   type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='type', verbose_name='Тип')
   genre = models.ForeignKey(Genre, on_delete=models.CASCADE, null=False, help_text='Жанр')
   year = models.DateField(verbose_name='Год')
   technic = models.ForeignKey(Technic, on_delete=models.CASCADE)
   size = models.IntegerField(verbose_name='Размер', null=True)
   publishing = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
   provenance = models.ForeignKey(Owner, on_delete=models.CASCADE,null=True)
   # event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True, related_name='event')
   # exhibition
   image = models.ImageField()
   pass

class Description(models.Model):
    pass



class Event(models.Model):
    pass