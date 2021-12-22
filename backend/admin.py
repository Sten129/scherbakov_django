from django.contrib import admin
from .models import Picture, Photo, Letter, Document, Exhibition, Genre, Book, Persone, Owner, Technic, Type, Location

class TypeAdmin(admin.ModelAdmin):
    pass

class PictureAdmin(admin.ModelAdmin):
    pass

class LocationAdmin(admin.ModelAdmin):
    pass

class GenreAdmin(admin.ModelAdmin):
    pass

class LocationAdmin(admin.ModelAdmin):
    pass

class ExhibitionAdmin(admin.ModelAdmin):
    pass

class TechnicAdmin(admin.ModelAdmin):
    pass

class OwnerAdmin(admin.ModelAdmin):
    pass

class PersoneAdmin(admin.ModelAdmin):
    pass

class BookAdmin(admin.ModelAdmin):
    pass

class DocumentAdmin(admin.ModelAdmin):
    pass

class LetterAdmin(admin.ModelAdmin):
    pass

class PhotoAdmin(admin.ModelAdmin):
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