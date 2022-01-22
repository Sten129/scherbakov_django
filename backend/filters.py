from django_filters import rest_framework as filters

from .models import Picture, Type, Exhibition, Persone, Book, Letter, Document


class PictureFilter(filters.FilterSet):
    title = filters.CharFilter(field_name='name', lookup_expr='contains')
    type = filters.CharFilter(field_name='category__slug',
                              lookup_expr='contains')
    genre = filters.CharFilter(field_name='genre__slug',
                               lookup_expr='contains')
    year = filters.DateFromToRangeFilter()
    technic = filters.CharFilter(field_name='tecnic', lookup_expr='contains')
    size = filters.NumberFilter()
    publishing = filters.CharFilter(field_name='publishing', lookup_expr='contains')
    provenance = filters.CharFilter(field_name='provenance', lookup_expr='contains')

    class Meta:
        model = Type
        fields = [
            'title',
            'type',
            'genre',
            'year',
            'technic',
            'size',
            'publishing',
            'provenance'
        ]


class BookFilter(filters.FilterSet):
    title = filters.CharFilter(field_name='title', lookup_expr='contains')
    year = filters.DateFromToRangeFilter
    pub_house = filters.CharFilter(field_name='pub_house', lookup_expr='contains')
    description = filters.CharFilter(field_name='description', lookup_expr='contains')
    location = filters.CharFilter(field_name='location', lookup_expr='contains')
    isbn = filters.CharFilter(field_name='isbn', lookup_expr='contains')

    class Meta:
        model = Book
        fields = ['title', 'year', 'pub_house', 'description', 'location', 'isbn']



class DocumentFilter(filters.FilterSet):
    title = filters.CharFilter(field_name='title', lookup_expr='contains')
    date = filters.DateFromToRangeFilter
    description = filters.CharFilter(field_name='description', lookup_expr='contains')
    location = filters.CharFilter(field_name='location', lookup_expr='contains')
    persons = filters.CharFilter(field_name='persons', lookup_expr='contains ')

    class Meta:
        model = Document
        fields = ['title', 'date', 'description', 'location', 'persons']




class ExhibitionFilter(filters.FilterSet):
    title = filters.CharFilter(field_name='title', lookup_expr='contains')
    date = filters.DateFromToRangeFilter()
    description = filters.CharFilter(field_name='description', lookup_expr='contains')
    location = filters.CharFilter(field_name='location', lookup_expr='contains')
    persons = filters.CharFilter(field_name='persons', lookup_expr='contains ')
    publishing = filters.CharFilter(field_name='publishing', lookup_expr='contains')

    class Meta:
        model = Exhibition
        fields = ['title', 'date', 'description', 'location', 'persons', 'publishing']



class LetterFilter(filters.FilterSet):
    title = filters.CharFilter(field_name='title', lookup_expr='contains')
    from_who = filters.CharFilter(field_name='from_who', lookup_expr='contains')
    to = filters.CharFilter(field_name='to', lookup_expr='contains')
    date = filters.DateFromToRangeFilter
    persons = filters.CharFilter(field_name='persons', lookup_expr='contains ')

    class Meta:
        model = Letter
        fields = ['title', 'from_who', 'to', 'date', 'persons']



class PersoneFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='contains')
    birth = filters.DateFromToRangeFilter()
    death = filters.DateFromToRangeFilter()
    description = filters.CharFilter(field_name='description', lookup_expr='contains')
    publishing = filters.CharFilter(field_name='publishing', lookup_expr='contains')

    class Meta:
        model = Letter
        fields = ['name', 'birth', 'death', 'description', 'publishing']

