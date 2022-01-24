from django.contrib import admin
from django import forms
from .models import (
    Picture,
    PictureInTheBook,
    PictureProvenance,
    PictureTechnic,
    BookOfExhibition,
    PersoneOnExhibition,
    PersoneInLetter,
    PersoneInThePicture,
    PersoneInTheBook,
    LocationOfExhibition,
    DocsOfExhibition,
    Letter,
    Document,
    Exhibition,
    Genre,
    Book,
    Persone,
    PersoneInDocument,
    Owner,
    Technic,
    Type,
    Location,
    PictureOnExhibition,
    Article,
    ArticlePicture,
    ArticleExhibitions,
    ArticleAuthor)
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from modeltranslation.admin import TranslationAdmin


class ExhibitionAdminForm(forms.ModelForm):
    description_ru = forms.CharField(
        label='Описание',
        widget=CKEditorUploadingWidget()
    )
    description_en = forms.CharField(
        label='Description',
        widget=CKEditorUploadingWidget()
    )
    description_fr = forms.CharField(
        label='La description',
        widget=CKEditorUploadingWidget()
    )
    description_zh_cn = forms.CharField(
        label='Описание',
        widget=CKEditorUploadingWidget()
    )

    class Meta:
        model = Exhibition
        fields = '__all__'


class ArticleAdminForm(forms.ModelForm):
    text_ru = forms.CharField(
        label='Текст',
        widget=CKEditorUploadingWidget()
    )
    text_en = forms.CharField(
        label='Text',
        widget=CKEditorUploadingWidget()
    )
    text_fr = forms.CharField(
        label='Text',
        widget=CKEditorUploadingWidget()
    )
    text_zh_cn = forms.CharField(
        label='Text_ch',
        widget=CKEditorUploadingWidget()
    )

    class Meta:
        model = Article
        fields = '__all__'


class PersoneAdminForm(forms.ModelForm):
    description_ru = forms.CharField(
        label='Описание',
        widget=CKEditorUploadingWidget()
    )
    description_en = forms.CharField(
        label='Description',
        widget=CKEditorUploadingWidget()
    )
    description_fr = forms.CharField(
        label='La description',
        widget=CKEditorUploadingWidget()
    )
    description_zh_cn = forms.CharField(
        label='Описание',
        widget=CKEditorUploadingWidget()
    )

    class Meta:
        model = Persone
        fields = '__all__'


class BookAdminForm(forms.ModelForm):
    description_ru = forms.CharField(
        label='Описание',
        widget=CKEditorUploadingWidget()
    )
    description_en = forms.CharField(
        label='Description',
        widget=CKEditorUploadingWidget()
    )
    description_fr = forms.CharField(
        label='La description',
        widget=CKEditorUploadingWidget()
    )
    description_zh_cn = forms.CharField(
        label='Описание',
        widget=CKEditorUploadingWidget()
    )

    class Meta:
        model = Book
        fields = '__all__'


class DocumentAdminForm(forms.ModelForm):
    description_ru = forms.CharField(
        label='Описание',
        widget=CKEditorUploadingWidget()
    )
    description_en = forms.CharField(
        label='Description',
        widget=CKEditorUploadingWidget()
    )
    description_fr = forms.CharField(
        label='La description',
        widget=CKEditorUploadingWidget()
    )
    description_zh_cn = forms.CharField(
        label='Описание',
        widget=CKEditorUploadingWidget()
    )

    class Meta:
        model = Document
        fields = '__all__'


class BookOfExhibitionInLine(admin.StackedInline):
    model = BookOfExhibition


class PictureTechnicInLine(admin.StackedInline):
    model = PictureTechnic


class PictureProvenanceInLine(admin.StackedInline):
    model = PictureProvenance


class PersoneInThePictureInLine(admin.StackedInline):
    model = PersoneInThePicture


class PictureOnExhibitionInline(admin.StackedInline):
    model = PictureOnExhibition


class DocsOfExhibitionInLine(admin.StackedInline):
    model = DocsOfExhibition


class PersoneInTheBookInLine(admin.StackedInline):
    model = PersoneInTheBook


class PictureInTheBookInline(admin.StackedInline):
    model = PictureInTheBook


class PersoneInDocumentInLine(admin.StackedInline):
    model = PersoneInDocument


class ArticlePictureInLine(admin.StackedInline):
    model = ArticlePicture


class ArticleExhibitionInLine(admin.StackedInline):
    model = ArticleExhibitions


class PersoneInLetterInLine(admin.StackedInline):
    model = PersoneInLetter


class ArticleAuthorInLine(admin.StackedInline):
    model = ArticleAuthor


class PersoneOnExhhibitonInLine(admin.StackedInline):
    model = PersoneOnExhibition


class LocationOfExhibitionInLine(admin.StackedInline):
    model = LocationOfExhibition


@admin.register(Location)
class LocationAdmin(TranslationAdmin):
    list_display = ('name', 'slug')
    empty_value_display = '-пусто-'
    search_fields = ('name',)
    list_filter = ('name',)


@admin.register(Genre)
class GenreAdmin(TranslationAdmin):
    list_display = ('name', 'slug')
    empty_value_display = '-пусто-'
    search_fields = ('name',)
    list_filter = ('name',)


@admin.register(Type)
class TypeAdmin(TranslationAdmin):
    list_display = ('name', 'slug')
    empty_value_display = '-пусто-'
    search_fields = ('name',)
    list_filter = ('name',)


@admin.register(Technic)
class TechnicAdmin(TranslationAdmin):
    list_display = ('name', 'slug')
    empty_value_display = '-пусто-'
    search_fields = ('name',)
    list_filter = ('name',)


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'persone', 'image', 'slug')
    empty_value_display = '-пусто-'
    search_fields = ('name',)
    list_filter = ('name',)


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    inlines = (
        PictureOnExhibitionInline,
        PictureInTheBookInline,
        PictureProvenanceInLine,
        PictureTechnicInLine,
        PersoneInThePictureInLine
    )
    list_display = ('title', 'type', 'genre', 'year',)
    empty_value_display = '-пусто-'
    search_fields = ('title', 'type', 'genre')
    list_filter = ('title', 'exhibition', 'publishing',)


@admin.register(Persone)
class PersoneAdmin(admin.ModelAdmin):
    inlines = (PersoneInTheBookInLine,)
    form = PersoneAdminForm
    list_display = ('name', 'birth', 'death', 'description', 'link', 'slug')
    empty_value_display = '-пусто-'
    search_fields = ('name',)
    list_filter = ('name',)


@admin.register(Book)
class BookAdmin(TranslationAdmin):
    list_display = (
        'title',
        'location',
        'year',
        'pub_house',
        'isbn',
        'pdf',
        'description',
        'image',
        'slug'
    )
    form = BookAdminForm
    empty_value_display = '-пусто-'
    search_fields = ('name', 'year')
    list_filter = ('title', 'year')


@admin.register(Exhibition)
class ExhibitionAdmin(TranslationAdmin):
    inlines = (
        BookOfExhibitionInLine,
        DocsOfExhibitionInLine,
        LocationOfExhibitionInLine,
        PersoneOnExhhibitonInLine
    )
    form = ExhibitionAdminForm
    list_display = ('title', 'date', 'description', 'slug')
    empty_value_display = '-пусто-'
    search_fields = ('title', 'location', 'date',)
    list_filter = ('date',)


@admin.register(Document)
class DocumentAdmin(TranslationAdmin):
    inlines = (PersoneInDocumentInLine,)
    form = DocumentAdminForm
    list_display = ('title', 'type', 'date', 'location', 'image', 'slug')
    empty_value_display = '-пусто-'
    search_fields = ('title',)
    list_filter = ('title', 'date')


@admin.register(Letter)
class LetterAdmin(admin.ModelAdmin):
    inlines = (PersoneInLetterInLine,)
    list_display = (
        'title',
        'from_who',
        'to',
        'location',
        'date',
        'pdf',
        'image',
        'slug'
    )
    empty_value_display = '-пусто-'
    search_fields = ('title', 'from_who', 'to', 'date')
    list_filter = ('to',)


class PhotoAdmin(admin.ModelAdmin):
    list_display = ()
    empty_value_display = '-пусто-'
    search_fields = ()
    list_filter = ()
    pass


@admin.register(Article)
class ArticleAdmin(TranslationAdmin):
    form = ArticleAdminForm
    inlines = (
        ArticleAuthorInLine,
        ArticleExhibitionInLine,
        ArticlePictureInLine
    )
    list_display = ('title', 'text', 'date', 'slug')
    empty_value_display = '-пусто-'
    search_fields = ('title',)
    list_filter = ('author',)
