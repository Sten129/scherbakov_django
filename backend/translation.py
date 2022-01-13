from modeltranslation.translator import register, TranslationOptions, translator
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

# @register(Persone)
# class PersoneTranslationOptions(TranslationOptions):
#     fields =


# translator.register(Type, TypeTranslationOptions)