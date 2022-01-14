from modeltranslation.translator import register, TranslationOptions
from .models import Type, Technic, Genre, Document, Letter, Exhibition, Picture, Persone, Book, Article, Owner, Location


@register(Type)
class TypeTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Genre)
class GenreTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Technic)
class TechnicTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Location)
class LocationTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Persone)
class PersoneTranslationOptions(TranslationOptions):
    fields = ('name', 'description', )


@register(Exhibition)
class ExhibitionTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Picture)
class PictureTranslationOptions(TranslationOptions):
    fields = ('title', )


@register(Article)
class ArticleTranslationOptions(TranslationOptions):
    fields = ('title', 'text', )


@register(Document)
class DocumentTraslationOptions(TranslationOptions):
    fields = ('title', 'type', 'description', )


@register(Letter)
class LetterTranslationOptions(TranslationOptions):
    fields = ('title', 'from_who', 'to', )


@register(Book)
class BookTranslationOptions(TranslationOptions):
    fields = ('title',  'pub_house', 'description')


@register(Owner)
class OwnerTranslationOptions(TranslationOptions):
    fields = ('name', )
