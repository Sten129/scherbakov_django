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
    # name = serializers.ReadOnlyField(read_only=True)
    # slug = serializers.SlugRelatedField(read_only=True, slug_field='slug', queryset=Type.objects.all())

    class Meta:
        fields = '__all__'
        model = Type

    # pass


class GenreSerializers(serializers.ModelSerializer):
    # name = serializers.ReadOnlyField(read_only=True)
    # slug = serializers.SlugRelatedField(read_only=True, slug_field='slug', queryset=Genre.objects.all())

    class Meta:
        fields = '__all__'
        model = Genre

    # pass


class TechnicSerializer(serializers.ModelSerializer):
    # name = serializers.ReadOnlyField()
    # name = serializers.SlugRelatedField(read_only=True, slug_field='name')
    # slug = serializers.SlugRelatedField(read_only=True, slug_field='slug')

    class Meta:
        fields = '__all__'
        model = Technic

    # pass


class PhotoSerializer(serializers.ModelSerializer):
    pass


class BookSerializer(serializers.ModelSerializer):
    title = serializers.ReadOnlyField()
    location = serializers.SlugRelatedField(queryset=Location.objects.all(), slug_field='name')

    # year = serializers.ReadOnlyField
    # pub_house = serializers.ReadOnlyField
    # isbn = serializers.ReadOnlyField
    # pdf =
    # description = serializers.ReadOnlyField
    # image = serializers.ImageField(
    #     required=True,
    #     allow_empty_file=False,
    #     use_url=True,
    # )
    # slug = serializers.SlugRelatedField

    class Meta:
        model = Book
        fields = '__all__'

    pass


class PersoneSerializer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField()
    birth = serializers.ReadOnlyField()
    death = serializers.ReadOnlyField()
    publishing = BookSerializer(read_only=True, many=True)

    # publishing = serializers.SlugRelatedField(queryset=Book.objects.all(), slug_field='title')
    # description = serializers.ReadOnlyField
    # link = serializers.HyperlinkedRelatedField
    # provenance = serializers.SlugRelatedField
    # publishing = serializers.SlugRelatedField
    # image = serializers.ImageField(
    #     required=True,
    #     allow_empty_file=False,
    #     use_url=True,
    # )
    # slug = serializers.SlugRelatedField
    # provenance = serializers.SlugRelatedField(queryset=Picture.objects.all(), slug_field='provenance')

    class Meta:
        model = Persone
        fields = '__all__'

    # pass


class LetterSerializer(serializers.ModelSerializer):
    # title = serializers.ReadOnlyField
    # from_who = serializers.ReadOnlyField
    # to = serializers.ReadOnlyField
    # location = serializers.SlugRelatedField
    # date = serializers.ReadOnlyField
    persons = PersoneSerializer(read_only=True, many=True)

    # publishing
    # pdf
    # image = serializers.ImageField(
    #             required=True,
    #             allow_empty_file=False,
    #             use_url=True,
    #         )
    # slug = serializers.SlugRelatedField

    class Meta:
        model = Letter
        fields = '__all__'

    pass


class DocumentSerializer(serializers.ModelSerializer):
    title = serializers.ReadOnlyField()
    type = serializers.ReadOnlyField()
    location = serializers.SlugRelatedField(queryset=Location.objects.all(), slug_field='name')
    persons = PersoneSerializer(read_only=True, many=True)

    # persons = serializers.SlugRelatedField(queryset=Persone.objects.all(), slug_field='name')
    # date = serializers.ReadOnlyField
    # pdf = serializers.FileField

    # image = serializers.ImageField(
    #         required=True,
    #         allow_empty_file=False,
    #         use_url=True,
    #     )
    # slug = serializers.SlugRelatedField

    class Meta:
        model = Document
        fields = "__all__"

    # pass


class LocationSerializer(serializers.ModelSerializer):
    # name = serializers.ReadOnlyField
    # slug = serializers.SlugRelatedField
    # image = serializers.ImageField(
    #     required=True,
    #     allow_empty_file=False,
    #     use_url=True,
    # )

    class Meta:
        model = Location
        fields = '__all__'

    # pass


class ExhibitionSerializer(serializers.ModelSerializer):
    location = LocationSerializer(read_only=True, many=True)
    persons = PersoneSerializer(read_only=True, many=True)
    publishing = BookSerializer(read_only=True, many=True)
    docs = DocumentSerializer(read_only=True, many=True)

    # location = serializers.SlugRelatedField(queryset=Location.objects.all(), slug_field='name')
    # persons = serializers.SlugRelatedField(queryset=Persone.objects.all(),  slug_field='name')
    # publishing = serializers.SlugRelatedField(queryset=Book.objects.all(), slug_field='title')

    class Meta:
        model = Exhibition
        fields = '__all__'

    # pass


class OwnerSerializer(serializers.ModelSerializer):
    # name = serializers.ReadOnlyField - разобраться с првязкой к Persone
    # slug = serializers.SlugRelatedField
    # image = serializers.ImageField(
    #     required=True,
    #     allow_empty_file=False,
    #     use_url=True,
    # )

    class Meta:
        model = Owner
        fields = '__all__'

    # pass


class PictureSerializer(serializers.ModelSerializer):
    title = serializers.ReadOnlyField()
    type = serializers.SlugRelatedField(queryset=Type.objects.all(), slug_field='name')
    genre = serializers.SlugRelatedField(queryset=Genre.objects.all(), slug_field='name')
    technic = TechnicSerializer(read_only=True, many=True)
    publishing = BookSerializer(read_only=True, many=True)
    provenance = OwnerSerializer(read_only=True, many=True)
    exhibition = ExhibitionSerializer(read_only=True, many=True)
    persons = PersoneSerializer(read_only=True, many=True)

    # technic = serializers.SlugRelatedField(queryset=Technic.objects.all(), many=True, slug_field='name')
    # publishing = serializers.SlugRelatedField(queryset=Book.objects.all(), slug_field='title')
    # provenance = serializers.SlugRelatedField(queryset=Owner.objects.all(), slug_field='name')
    # exhibition = serializers.SlugRelatedField(queryset=Exhibition.objects.all(),  slug_field='location')
    # year = serializers.ReadOnlyField
    # size = serializers.ReadOnlyField
    # image = serializers.ImageField(
    #     required=True,
    #     allow_empty_file=False,
    #     use_url=True,
    # )

    class Meta:
        model = Picture
        fields = '__all__'

    # pass


class ArticleSerializer(serializers.ModelSerializer):
    title = serializers.ReadOnlyField()
    text = serializers.ReadOnlyField()
    author = PersoneSerializer(read_only=True, many=True)
    exhibition = ExhibitionSerializer(read_only=True, many=True)
    picture = PictureSerializer(read_only=True, many=True)
    date = serializers.ReadOnlyField()

    # picture = serializers.SlugRelatedField(queryset=Picture.objects.all(), slug_field='title')
    # exhibition = ExhibitionSerializer(read_only=True, many=True)
    # author = serializers.SlugRelatedField(queryset=Persone.objects.all(), slug_field='name')
    # exhibition = serializers.SlugRelatedField(queryset=Exhibition.objects.all(), slug_field='title')

    # slug

    class Meta:
        model = Article
        fields = '__all__'

    # pass


class PictureOnExhibitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PictureOnExhibition
        fields = '__all__'
