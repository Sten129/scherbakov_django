from django.contrib import admin
from .models import Picture, Photo, Letter, Document, Exhibition, Genre, Book, Persone, Owner, Technic, Type, Location

class TypeAdmin(admin.ModelAdmin):
    list_display = ()
    empty_value_display = '-пусто-'
    search_fields = ()
    list_filter = ()
    pass

class PictureAdmin(admin.ModelAdmin):
    list_display = ()
    empty_value_display = '-пусто-'
    search_fields = ()
    list_filter = ()
    pass

class LocationAdmin(admin.ModelAdmin):
    list_display = ()
    empty_value_display = '-пусто-'
    search_fields = ()
    list_filter = ()
    pass

class GenreAdmin(admin.ModelAdmin):
    list_display = ()
    empty_value_display = '-пусто-'
    search_fields = ()
    list_filter = ()
    pass

class LocationAdmin(admin.ModelAdmin):
    list_display = ()
    empty_value_display = '-пусто-'
    search_fields = ()
    list_filter = ()
    pass

class ExhibitionAdmin(admin.ModelAdmin):
    list_display = ()
    empty_value_display = '-пусто-'
    search_fields = ()
    list_filter = ()
    pass

class TechnicAdmin(admin.ModelAdmin):
    list_display = ()
    empty_value_display = '-пусто-'
    search_fields = ()
    list_filter = ()
    pass

class OwnerAdmin(admin.ModelAdmin):
    list_display = ()
    empty_value_display = '-пусто-'
    search_fields = ()
    list_filter = ()
    pass

class PersoneAdmin(admin.ModelAdmin):
    list_display = ()
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
    list_display = ()
    empty_value_display = '-пусто-'
    search_fields = ()
    list_filter = ()
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