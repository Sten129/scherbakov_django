from django.contrib import admin
from .models import Picture, Photo, Letter, Document, Exhibition, Genre, Book, Persone, Owner, Technic, Type, Location

class TypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    empty_value_display = '-пусто-'
    search_fields = ()
    list_filter = ()
    pass

class PictureAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'genre', 'year', 'publishing', 'provenance', 'exhibition')
    empty_value_display = '-пусто-'
    search_fields = ('title', 'type', 'genre')
    list_filter = ('title',)
    pass

class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    empty_value_display = '-пусто-'
    search_fields = ('name',)
    list_filter = ('name',)
    pass

class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    empty_value_display = '-пусто-'
    search_fields = ('name',)
    list_filter = ('name',)
    pass


class ExhibitionAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'date', 'pictures', 'persons', 'publishing', 'docs', 'description', 'slug' )
    empty_value_display = '-пусто-'
    search_fields = ('title', 'location', 'date', 'pictures')
    list_filter = ('date',)
    pass

class TechnicAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    empty_value_display = '-пусто-'
    search_fields = ('name',)
    list_filter = ('name',)
    pass

class OwnerAdmin(admin.ModelAdmin):
    list_display = ()
    empty_value_display = '-пусто-'
    search_fields = ()
    list_filter = ()
    pass

class PersoneAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth', 'death', 'description', 'link', 'provenance', 'publishing', 'slug')
    empty_value_display = '-пусто-'
    search_fields = ()
    list_filter = ()
    pass

class BookAdmin(admin.ModelAdmin):
    list_display = ()
    empty_value_display = '-пусто-'
    search_fields = ()
    list_filter = ()
    pass

class DocumentAdmin(admin.ModelAdmin):
    list_display = ()
    empty_value_display = '-пусто-'
    search_fields = ()
    list_filter = ()
    pass

class LetterAdmin(admin.ModelAdmin):
    list_display = ('title', 'from_who', 'to', 'location', 'date', 'persons', 'pdf', 'image', 'slug')
    empty_value_display = '-пусто-'
    search_fields = ('title', 'from_who', 'to', 'date')
    list_filter = ('to', )
    pass

class PhotoAdmin(admin.ModelAdmin):
    list_display = ()
    empty_value_display = '-пусто-'
    search_fields = ()
    list_filter = ()
    pass


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