from django_filters import rest_framework as filters

from .models import Picture, Type, Exhibition, Persone, Book, Letter, Document


class PictureFilter(filters.FilterSet):
    title = filters.CharFilter(field_name='name', lookup_expr='contains')
    type = filters.CharFilter(field_name='category__slug',
                              lookup_expr='contains')
    genre = filters.CharFilter(field_name='genre__slug',
                               lookup_expr='contains')
    year = filters.DateFromToRangeFilter
    technic = filters.CharFilter(field_name='tecnic', lookup_expr='contains')
    size = filters.NumberFilter
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


class BookFiler(filters.FilterSet):
    title = filters.CharFilter(field_name='title', lookup_expr='contains')
    year = filters.DateFromToRangeFilter
    pub_house = filters.CharFilter(field_name='pub_house', lookup_expr='contains')
    description = filters.CharFilter(field_name='description', lookup_expr='contains')

    class Meta:
        model = Book
        fields = '__all__'
    pass


class DocumentFilter(filters.FilterSet):
    pass


class ExhibitionFilter(filters.FilterSet):
    pass


class LetterFilter(filters.FilterSet):
    pass


class PersoneFilter(filters.FilterSet):
    pass
