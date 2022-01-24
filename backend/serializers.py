from rest_framework import serializers
from .models import (Picture,
                     Letter,
                     Document,
                     Exhibition,
                     Genre,
                     Book,
                     Persone,
                     Owner,
                     Technic,
                     Type,
                     Location,
                     Article,
                     PictureOnExhibition)


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Type


class GenreSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Genre


class TechnicSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Technic


class PhotoSerializer(serializers.ModelSerializer):
    pass


class BookSerializer(serializers.ModelSerializer):
    title = serializers.ReadOnlyField(source='get_book_title')
    location = serializers.SlugRelatedField(
        queryset=Location.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = Book
        fields = '__all__'


class PersoneSerializer(serializers.ModelSerializer):
    publishing = BookSerializer(read_only=True, many=True)

    class Meta:
        model = Persone
        fields = '__all__'


class LetterSerializer(serializers.ModelSerializer):
    persons = PersoneSerializer(read_only=True, many=True)

    class Meta:
        model = Letter
        fields = '__all__'

    pass


class DocumentSerializer(serializers.ModelSerializer):
    title = serializers.ReadOnlyField()
    type = serializers.ReadOnlyField()
    location = serializers.SlugRelatedField(
        queryset=Location.objects.all(),
        slug_field='name'
    )
    persons = PersoneSerializer(read_only=True, many=True)

    class Meta:
        model = Document
        fields = "__all__"


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class ExhibitionSerializer(serializers.ModelSerializer):
    location = LocationSerializer(read_only=True, many=True)
    persons = PersoneSerializer(read_only=True, many=True)
    publishing = BookSerializer(read_only=True, many=True)
    docs = DocumentSerializer(read_only=True, many=True)

    class Meta:
        model = Exhibition
        fields = '__all__'

    # pass


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = '__all__'


class PictureSerializer(serializers.ModelSerializer):
    title = serializers.ReadOnlyField()
    type = serializers.SlugRelatedField(
        queryset=Type.objects.all(),
        slug_field='name')
    genre = serializers.SlugRelatedField(
        queryset=Genre.objects.all(),
        slug_field='name'
    )
    technic = TechnicSerializer(read_only=True, many=True)
    publishing = BookSerializer(read_only=True, many=True)
    provenance = OwnerSerializer(read_only=True, many=True)
    exhibition = ExhibitionSerializer(read_only=True, many=True)
    persons = PersoneSerializer(read_only=True, many=True)

    class Meta:
        model = Picture
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    title = serializers.ReadOnlyField()
    text = serializers.ReadOnlyField()
    author = PersoneSerializer(read_only=True, many=True)
    exhibition = ExhibitionSerializer(read_only=True, many=True)
    picture = PictureSerializer(read_only=True, many=True)
    date = serializers.ReadOnlyField()

    class Meta:
        model = Article
        fields = '__all__'


class PictureOnExhibitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PictureOnExhibition
        fields = '__all__'
