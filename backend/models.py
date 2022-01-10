from django.db import models
from django.contrib.auth import get_user_model
import datetime

User = get_user_model()


class Genre(models.Model):
    name = models.CharField('Название жанра', unique=True, max_length=20)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ('-name',)
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField('Тип работы', unique=True, max_length=20)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ('-name',)
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'

    def __str__(self):
        return self.name


class Technic(models.Model):
    name = models.CharField('Техника', unique=True, max_length=20)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ('-name',)
        verbose_name = 'Техника'
        verbose_name_plural = 'Техники'

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField('Локация', unique=True, max_length=20)
    image = models.ImageField(verbose_name='Изображение', blank=True, upload_to='locations/')
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ('-name',)
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=500, verbose_name='Название')
    location = models.ForeignKey(Location, on_delete=models.CASCADE, verbose_name='место издания')
    year = models.DateField(verbose_name='Дата', default=datetime.date.today)
    pub_house = models.CharField(max_length=500, verbose_name='издательство')
    isbn = models.CharField(verbose_name='ISBN', max_length=14)
    pdf = models.FileField
    description = models.TextField(max_length=1000, verbose_name='описание')
    image = models.ImageField(verbose_name='Изображение', upload_to='books/')
    slug = models.SlugField(null=False, unique=False, help_text='URL')

    class Meta:
        ordering = ('-title',)
        verbose_name = 'Издание'
        verbose_name_plural = 'Издания'

    def __str__(self):
        return self.title


class Photo(models.Model):
    pass


class Persone(models.Model):
    name = models.CharField(max_length=200, verbose_name='имя')
    birth = models.DateField(verbose_name='Дата рождения', default=datetime.date.today)
    death = models.DateField(verbose_name='Дата смерти', blank=True, null=True, default=datetime.date.today)
    description = models.TextField(max_length=1000, verbose_name='Описание')
    link = models.URLField(blank=True)
    publishing = models.ManyToManyField(Book, through='PersoneInTheBook', blank=True, verbose_name='Публикации')
    image = models.ImageField(verbose_name='Изображение', upload_to='persons/')
    slug = models.SlugField(unique=True, help_text='URL')
    # provenance = models.ForeignKey(Owner, on_delete=models.CASCADE, null=True)
    # publishing = models.ForeignKey(Book, on_delete=models.CASCADE, null=True, blank=True)
    # letter = models.ForeignKey(Letter, on_delete=models.CASCADE, null=True, related_name='letter')
    # event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True, related_name='event')

    class Meta:
        ordering = ('-name',)
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'

    def __str__(self):
        return self.name


class Owner(models.Model):
    name = models.CharField(max_length=500, blank=True, null=True, verbose_name='Название или имя')
    persone = models.ForeignKey(Persone, blank=True, null=True, on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='Изображение', upload_to='owners/')
    slug = models.SlugField(unique=True, help_text='URL')

    class Meta:
        ordering = ('-name',)
        verbose_name = 'Владелец'
        verbose_name_plural = 'Владельцы'

    def __str__(self):
        return self.name


class Letter(models.Model):
    title = models.CharField(max_length=500, verbose_name='Название')
    from_who = models.CharField(max_length=500, verbose_name='От кого')
    to = models.CharField(max_length=500, verbose_name='Кому')
    location = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Локация')
    date = models.DateField(verbose_name='Дата', default=datetime.date.today)
    # persons = models.ForeignKey(Persone, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Люди')
    persons = models.ManyToManyField(Persone, through='PersoneInLetter', blank=True, verbose_name='Люди')
    pdf = models.FileField(verbose_name='PDF-файл')
    image = models.ImageField(verbose_name='Изображение', upload_to='letters/')
    slug = models.SlugField(unique=True, help_text='URL')

    class Meta:
        ordering = ('-title',)
        verbose_name = 'Письмо'
        verbose_name_plural = 'Письма'

    def __str__(self):
        return self.title


class Document(models.Model):
    title = models.CharField(max_length=500, verbose_name='Название')
    type = models.CharField(max_length=100, blank=True, null=True, verbose_name='Тип документа')
    date = models.DateField(verbose_name='Дата', default=datetime.date.today)
    # event = models.ForeignKey
    location = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True,  verbose_name='Локация')
    # persons = models.ForeignKey(Persone, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Люди')
    persons = models.ManyToManyField(Persone, through='PersoneInDocument', blank=True, verbose_name='Люди')
    image = models.ImageField(verbose_name='Изображение', upload_to='docs/')
    slug = models.SlugField(unique=True, help_text='URL')

    class Meta:
        ordering = ('-title',)
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'

    def __str__(self):
        return self.title




class Exhibition(models.Model):
    title = models.CharField(max_length=500, verbose_name='Название')
    location = models.ManyToManyField(Location, through='LocationOfExhibition', verbose_name='Локации')
    date = models.DateField(verbose_name='Дата', default=datetime.date.today)
    persons = models.ManyToManyField(Persone, through='PersoneOnExhibition', blank=True, verbose_name='Люди')
    publishing = models.ManyToManyField(Book, through='BookOfExhibition', blank=True, verbose_name='Книга')
    docs = models.ManyToManyField(Document, through='DocsOfExhibition', blank=True, verbose_name='Документ')
    description = models.TextField(max_length=1000, verbose_name='Описание')
    image = models.ImageField(verbose_name='Изображение', upload_to='exhibitions/')
    slug = models.SlugField(null=False, unique=False, help_text='URL')
    # location = models.ForeignKey(Location, on_delete=models.CASCADE, null=False, verbose_name='Локация')
    # persons = models.ForeignKey(Persone, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Люди')
    # publishing = models.ForeignKey(Book, on_delete=models.CASCADE,  blank=True, null=True, verbose_name='Издания')
    # docs = models.ForeignKey(Document, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Документы')
    # publishing = models.ManyToManyField(Book, related_name='book')
    # pictures = models.ManyToManyField(Picture, through='')

    class Meta:
        ordering = ('-title',)
        verbose_name = 'Выставка'
        verbose_name_plural = 'Выставки'

    def __str__(self):
        return self.title


class Picture(models.Model):
    title = models.CharField(max_length=500, verbose_name='Название')
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='type', verbose_name='Тип')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, blank=False, help_text='Жанр')
    year = models.DateField(verbose_name='Год', default=datetime.date.today)
    technic = models.ManyToManyField(Technic, through='PictureTechnic', blank=False, related_name='technic', verbose_name='техника')
    size_vertical = models.PositiveIntegerField(verbose_name='Размер по вертикали', blank=False)
    size_horisontal = models.PositiveIntegerField(verbose_name='Размер по горизонтали', blank=False)
    publishing = models.ManyToManyField(Book, through='PictureInTheBook', blank=True, related_name='publishing', verbose_name='Публикации')
    provenance = models.ManyToManyField(Owner, through='PictureProvenance', blank=True, related_name='provenance', verbose_name='Владельцы')
    exhibition = models.ManyToManyField(Exhibition, through='PictureOnExhibition', blank=True, related_name='exhibition', verbose_name='Выставки')
    persons = models.ManyToManyField(Persone, through='PersoneInThePicture', blank=True, related_name='persone', verbose_name='Люди')
    image = models.ImageField(verbose_name='Изображение', upload_to='pictures/')
    # technic = models.ForeignKey(Technic, on_delete=models.CASCADE, blank=False)
    # publishing = models.ForeignKey(Book, on_delete=models.CASCADE, blank=True, null=True)
    # provenance = models.ForeignKey(Owner, on_delete=models.CASCADE, blank=True, null=True)
    # event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True, related_name='event')
    # exhibition = models.ForeignKey(Exhibition, on_delete=models.CASCADE,  blank=True, null=True, verbose_name='Выставки', related_name='exhibitions')

    class Meta:
        ordering = ('-title',)
        verbose_name = 'Работа'
        verbose_name_plural = 'Работы'

    def __str__(self):
        return self.title


class PictureOnExhibition(models.Model):
    picture = models.ForeignKey(Picture, on_delete=models.CASCADE, verbose_name='Работа')
    exhibition = models.ForeignKey(Exhibition, on_delete=models.CASCADE, verbose_name='Выставка')

    class Meta:
        verbose_name = 'Работа на выставке'
        verbose_name_plural = 'Работы на выставке'
        constraints = [ models.UniqueConstraint(
            fields= ['picture', 'exhibition'],
            name= 'picture_exhibition_unique'
          )
        ]

    def __str__(self):
        return f'{self.picture} / {self.exhibition}'

class PictureInTheBook(models.Model):
    picture = models.ForeignKey(Picture, on_delete=models.CASCADE, verbose_name='Работа')
    publishing = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='Издание')

    class Meta:
        verbose_name = 'Работа опубликована'
        verbose_name_plural = 'Работы опубликованы'
        constraints = [models.UniqueConstraint(
            fields=['picture', 'publishing'],
            name='picture_publishing_unique'
        )
        ]

    def __str__(self):
        return f'{self.picture} / {self.publishing}'

class PictureProvenance(models.Model):
    picture = models.ForeignKey(Picture, on_delete=models.CASCADE, verbose_name='Работа')
    provenance = models.ForeignKey(Owner, on_delete=models.CASCADE, verbose_name='Провенанс')

    class Meta:
        verbose_name = 'Владелец работы'
        verbose_name_plural = 'Владельцы работы'
        constraints = [models.UniqueConstraint(
            fields=['picture', 'provenance'],
            name='picture_provenance_unique'
        )
        ]

    def __str__(self):
        return f'{self.picture} / {self.provenance}'

class PictureTechnic(models.Model):
    picture = models.ForeignKey(Picture, on_delete=models.CASCADE, verbose_name='Работа')
    technic = models.ForeignKey(Technic, on_delete=models.CASCADE, verbose_name='Техника')

    class Meta:
        verbose_name = 'Техника'
        constraints = [models.UniqueConstraint(
            fields=['picture', 'technic'],
            name='picture_technic_unique'
        )
        ]

    def __str__(self):
        return f'{self.picture} / {self.technic}'






class Article(models.Model):
   title = models.CharField(max_length=500, verbose_name='Название')
   text = models.TextField(verbose_name='Текст')
   author = models.ManyToManyField(Persone, through='ArticleAuthor', related_name='author',verbose_name='Автор')
   date = models.DateField(verbose_name='Дата', auto_now=datetime.date.today())
   exhibition = models.ManyToManyField(Exhibition, through='ArticleExhibitions', related_name='a_exhibition', verbose_name='Выставка' )
   picture = models.ManyToManyField(Picture, through='ArticlePicture', related_name='a_picture', verbose_name='Работа')
   image = models.ImageField(verbose_name='Изображение', blank=True, null=True, upload_to='articles/')
   slug = models.SlugField(null=False, unique=True, help_text='URL')
   # author = models.ForeignKey(Persone, on_delete=models.CASCADE, blank=True, verbose_name='Автор', related_name='persone')
   # exhibition = models.ForeignKey(Exhibition, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Выставки')
   # picture = models.ForeignKey(Picture, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Работы')

   class Meta:
       ordering = ('-title',)
       verbose_name = 'Статья'
       verbose_name_plural = 'Статьи'

   def __str__(self):
       return self.title

class ArticleAuthor(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='Cтатья')
    author = models.ForeignKey(Persone, on_delete=models.CASCADE, verbose_name='Автор')


    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        constraints = [models.UniqueConstraint(
            fields=['article', 'author'],
            name='article_author_unique'
        )
        ]
    def __str__(self):
        return f'{self.article} / {self.author}'

class ArticleExhibitions(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='Cтатья')
    exhibition = models.ForeignKey(Exhibition, on_delete=models.CASCADE, verbose_name='Выставка')

    class Meta:
        verbose_name = 'Выставка'
        verbose_name_plural = 'Выставки'

    constraints = [models.UniqueConstraint(
        fields=['article', 'exhibition'],
        name='article_exhibition_unique'
    )
    ]

    def __str__(self):
        return f'{self.article} / {self.exhibition}'

class ArticlePicture(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='Cтатья')
    picture = models.ForeignKey(Picture, on_delete=models.CASCADE, verbose_name='Работа')

    class Meta:
        verbose_name = 'Работа'
        verbose_name_plural = 'Работы'

    constraints = [models.UniqueConstraint(
        fields=['article', 'picture'],
        name='article_picture_unique'
    )
    ]

    def __str__(self):
        return f'{self.article} / {self.picture}'

class PersoneInDocument(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE, verbose_name='Документ')
    persone = models.ForeignKey(Persone, on_delete=models.CASCADE, verbose_name='Человек')

    class Meta:
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'

    constraints = [models.UniqueConstraint(
        fields=['persone', 'document'],
        name='document_persone_unique'
    )
    ]

    def __str__(self):
        return f'{self.document} / {self.persone}'

class LocationOfExhibition(models.Model):
    exhibition = models.ForeignKey(Exhibition, on_delete=models.CASCADE, verbose_name='Выставка')
    location = models.ForeignKey(Location, on_delete=models.CASCADE, verbose_name='Локация')

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'

    constraints = [models.UniqueConstraint(
        fields=['exhibition', 'location'],
        name='exhibition_location_unique'
    )
    ]

    def __str__(self):
        return f'{self.exhibition} / {self.location}'


class PersoneOnExhibition(models.Model):
    exhibition = models.ForeignKey(Exhibition, on_delete=models.CASCADE, verbose_name='Выставка')
    persone = models.ForeignKey(Persone, on_delete=models.CASCADE, verbose_name='Человек')

    class Meta:
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'

    constraints = [models.UniqueConstraint(
        fields=['exhibition', 'persone'],
        name='exhibition_persone_unique'
    )
    ]

    def __str__(self):
        return f'{self.exhibition} / {self.persone}'


class DocsOfExhibition(models.Model):
    exhibition = models.ForeignKey(Exhibition, on_delete=models.CASCADE, verbose_name='Выставка')
    document = models.ForeignKey(Document, on_delete=models.CASCADE, verbose_name='Документ')

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'

    constraints = [models.UniqueConstraint(
        fields=['exhibition', 'document'],
        name='exhibition_document_unique'
    )
    ]

    def __str__(self):
        return f'{self.exhibition} / {self.document}'

class BookOfExhibition(models.Model):
    exhibition = models.ForeignKey(Exhibition, on_delete=models.CASCADE, verbose_name='Выставка')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='Книга')

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    constraints = [models.UniqueConstraint(
        fields=['exhibition', 'book'],
        name='exhibition_book_unique'
    )
    ]

    def __str__(self):
        return f'{self.exhibition} / {self.book}'

class PersoneInLetter(models.Model):
    letter = models.ForeignKey(Letter, on_delete=models.CASCADE, verbose_name='Письмо')
    persone = models.ForeignKey(Persone, on_delete=models.CASCADE, verbose_name='Человек')

    class Meta:
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'

    constraints = [models.UniqueConstraint(
        fields=['letter', 'persone'],
        name='persone_letter_unique'
    )
    ]

    def __str__(self):
        return f'{self.letter} / {self.persone}'


class PersoneInTheBook(models.Model):
    persone = models.ForeignKey(Persone, on_delete=models.CASCADE, verbose_name='Человек')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='Книга')

    class Meta:
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'

    constraints = [models.UniqueConstraint(
        fields=['persone', 'book'],
        name='persone_book_unique'
    )
    ]

    def __str__(self):
        return f'{self.book} / {self.persone}'

class PersoneInThePicture(models.Model):
    persone = models.ForeignKey(Persone, on_delete=models.CASCADE, verbose_name='Человек')
    picture = models.ForeignKey(Picture, on_delete=models.CASCADE, verbose_name='Работа')

    class Meta:
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'

    constraints = [models.UniqueConstraint(
        fields=['persone', 'picture'],
        name='persone_picture_unique'
    )
    ]

    def __str__(self):
        return f'{self.picture} / {self.persone}'








class Event(models.Model): # при необходимости можно также добавить и использовать связующую модель
    pass
