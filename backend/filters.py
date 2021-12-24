from django_filters import rest_framework as filters

from .models import Picture, Type


class PictureFilter(filters.FilterSet):
    title = filters.CharFilter(field_name='name', lookup_expr='contains')
    type = filters.CharFilter(field_name='category__slug',
                                  lookup_expr='contains')
    genre = filters.CharFilter(field_name='genre__slug',
                               lookup_expr='contains')
    year = filters.DateFromToRangeFilter
    technic = filters.CharFilter
    size = filters.NumberFilter
    publishing = filters.CharFilter
    provenance = filters.CharFilter

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
