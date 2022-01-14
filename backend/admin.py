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
    Photo,
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
    description_ru = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())
    description_en = forms.CharField(label='Description', widget=CKEditorUploadingWidget())
    description_fr = forms.CharField(label='La description', widget=CKEditorUploadingWidget())
    description_zh_cn = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())


    class Meta:
        model = Exhibition
        fields = '__all__'


class AritcleAdminForm(forms.ModelForm):
    text_ru = forms.CharField(label='Текст', widget=CKEditorUploadingWidget())
    text_en= forms.CharField(label='Text', widget=CKEditorUploadingWidget())
    text_fr = forms.CharField(label='Text', widget=CKEditorUploadingWidget())
    text_zh_cn = forms.CharField(label='Text_ch', widget=CKEditorUploadingWidget())

    class Meta:
        model = Article
        fields = '__all__'


class PersoneAdminForm(forms.ModelForm):
    description_ru = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())
    description_en = forms.CharField(label='Description', widget=CKEditorUploadingWidget())
    description_fr = forms.CharField(label='La description', widget=CKEditorUploadingWidget())
    description_zh_cn = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())

    class Meta:
        model = Persone
        fields = '__all__'


class BookAdminForm(forms.ModelForm):
    description_ru = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())
    description_en = forms.CharField(label='Description', widget=CKEditorUploadingWidget())
    description_fr = forms.CharField(label='La description', widget=CKEditorUploadingWidget())
    description_zh_cn = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())


    class Meta:
        model = Book
        fields = '__all__'


class DocumentAdminForm(forms.ModelForm):
    description_ru = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())
    description_en = forms.CharField(label='Description', widget=CKEditorUploadingWidget())
    description_fr = forms.CharField(label='La description', widget=CKEditorUploadingWidget())
    description_zh_cn = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())

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


# class LocationAdmin(admin.ModelAdmin):
class LocationAdmin(TranslationAdmin):
    list_display = ('name', 'slug')
    empty_value_display = '-пусто-'
    search_fields = ('name',)
    list_filter = ('name',)


# class GenreAdmin(admin.ModelAdmin):
class GenreAdmin(TranslationAdmin):
    list_display = ('name', 'slug')
    empty_value_display = '-пусто-'
    search_fields = ('name',)
    list_filter = ('name',)

# class TypeAdmin(admin.ModelAdmin):
class TypeAdmin(TranslationAdmin):
    list_display = ('name', 'slug')
    empty_value_display = '-пусто-'
    search_fields = ('name',)
    # list_filter = ()


# class TechnicAdmin(admin.ModelAdmin):
class TechnicAdmin(TranslationAdmin):
    list_display = ('name', 'slug')
    empty_value_display = '-пусто-'
    search_fields = ('name',)
    list_filter = ('name',)

class OwnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'persone', 'image', 'slug')
    empty_value_display = '-пусто-'
    search_fields = ('name',)
    list_filter = ('name',)

class PictureAdmin(admin.ModelAdmin):
    inlines = (PictureOnExhibitionInline, PictureInTheBookInline, PictureProvenanceInLine, PictureTechnicInLine,
               PersoneInThePictureInLine)
    list_display = ('title', 'type', 'genre', 'year',)
    empty_value_display = '-пусто-'
    search_fields = ('title', 'type', 'genre')
    list_filter = ('title', 'exhibition', 'publishing',)


class PersoneAdmin(admin.ModelAdmin):
    inlines = (PersoneInTheBookInLine,)
    form = PersoneAdminForm
    list_display = ('name', 'birth', 'death', 'description', 'link', 'slug')
    empty_value_display = '-пусто-'
    search_fields = ('name',)
    list_filter = ('name',)


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'year', 'pub_house', 'isbn', 'pdf', 'description', 'image', 'slug')
    form = BookAdminForm
    empty_value_display = '-пусто-'
    search_fields = ('name', 'year')
    list_filter = ('title', 'year')


class ExhibitionAdmin(admin.ModelAdmin):
    inlines = (BookOfExhibitionInLine, DocsOfExhibitionInLine, LocationOfExhibitionInLine, PersoneOnExhhibitonInLine)
    form = ExhibitionAdminForm
    list_display = ('title', 'date', 'description', 'slug')
    empty_value_display = '-пусто-'
    search_fields = ('title', 'location', 'date',)
    list_filter = ('date',)


class DocumentAdmin(admin.ModelAdmin):
    inlines = (PersoneInDocumentInLine,)
    form = DocumentAdminForm
    list_display = ('title', 'type', 'date', 'location', 'image', 'slug')
    empty_value_display = '-пусто-'
    search_fields = ('title',)
    list_filter = ('title', 'date')


class LetterAdmin(admin.ModelAdmin):
    inlines = (PersoneInLetterInLine,)
    list_display = ('title', 'from_who', 'to', 'location', 'date', 'pdf', 'image', 'slug')
    empty_value_display = '-пусто-'
    search_fields = ('title', 'from_who', 'to', 'date')
    list_filter = ('to',)


class PhotoAdmin(admin.ModelAdmin):
    list_display = ()
    empty_value_display = '-пусто-'
    search_fields = ()
    list_filter = ()
    pass


class ArticleAdmin(admin.ModelAdmin):
    form = AritcleAdminForm
    inlines = (ArticleAuthorInLine, ArticleExhibitionInLine, ArticlePictureInLine)
    list_display = ('title', 'text', 'date', 'slug')
    empty_value_display = '-пусто-'
    search_fields = ('title',)
    list_filter = ('author',)


admin.site.register(Type, TypeAdmin)
admin.site.register(Picture, PictureAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Owner, OwnerAdmin)
admin.site.register(Letter, LetterAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(Exhibition, ExhibitionAdmin)
admin.site.register(Persone, PersoneAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Technic, TechnicAdmin)
admin.site.register(Article, ArticleAdmin)
