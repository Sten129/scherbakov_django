from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from backend.models import (Picture,
                            Type,
                            Exhibition,
                            Letter,
                            Persone,
                            Location,
                            Document,
                            Genre,
                            Technic,
                            Book,
                            Owner,
                            Article)
from .forms import ContactForm
from .serializers import (
    TypeSerializer,
    GenreSerializers,
    BookSerializer,
    PictureSerializer,
    ExhibitionSerializer,
    TechnicSerializer,
    DocumentSerializer,
    PersoneSerializer,
    LocationSerializer,
    OwnerSerializer,
    LetterSerializer,
    ArticleSerializer
)


class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    pagination_class = PageNumberPagination


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializers
    pagination_class = PageNumberPagination


class TechnicViewSet(viewsets.ModelViewSet):
    queryset = Technic.objects.all()
    serializer_class = TechnicSerializer
    pagination_class = PageNumberPagination


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    pagination_class = PageNumberPagination


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = PageNumberPagination


class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
    pagination_class = PageNumberPagination


class PersoneViewSet(viewsets.ModelViewSet):
    queryset = Persone.objects.all()
    serializer_class = PersoneSerializer
    pagination_class = PageNumberPagination


class LetterViewSet(viewsets.ModelViewSet):
    queryset = Letter.objects.all()
    serializer_class = LetterSerializer
    pagination_class = PageNumberPagination


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    pagination_class = PageNumberPagination


class ExhibitionViewSet(viewsets.ModelViewSet):
    queryset = Exhibition.objects.all()
    serializer_class = ExhibitionSerializer
    pagination_class = PageNumberPagination


class PictureViewSet(viewsets.ModelViewSet):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer
    pagination_class = PageNumberPagination

    class Meta:
        fields = '__all__'


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Пробное сообщение"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())
            try:
                send_mail(subject, message,
                          'admin@example.com',
                          ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Найден некорректный заголовок')
            return redirect("main:homepage")

    form = ContactForm()
    return render(request, "main/contact.html", {'form': form})

# def index(request):
#     picture_list = Picture.objects.all()
#     paginator = Paginator(picture_list, 10)
#     page_number = request.GET.get('page')
#     page = paginator.get_page(page_number)
#     return render(
#         request,
#         'index.html',
#         {'page': page, 'paginator': paginator}
#     )
#
# def group_pictures(request, slug):
#     # подставить переменную - критерий группировки
#     # queryset = Book.objects.filter(title__startswith='M') - пример Queryset.
#     # делаем queryset по выставкам, жанрам, годам, технике, людям, музеям, владельцам
#     # queryset = Picture.objects.filter(slug=request.slug)
#     # group = get_object_or_404(queryset, slug=slug)
#     group = get_object_or_404(Type, slug=slug)
#     picture_list_group = type.pictures.all()
#     paginator = Paginator(picture_list_group, 10)
#     page_number = request.GET.get('page')
#     page = paginator.get_page(page_number)
#     return render(
#         request,
#         'group.html',
#         {
#             'group': group,
#             'page': page,
#             'paginator': paginator
#         }
#     )
#
# def picture_view(request, picture_id):
#     post = get_object_or_404(Picture, id=picture_id)
#     description = pictures.descriptions.all()
#     # form = PictureForm()
#     return render(request, 'preview.html',
#                   {'picture': picture, 'type': picture.type, 'description': description, 'form': form})
#
#
# def page_not_found(request, exception):  # noqa
#     return render(
#         request,
#         "misc/404.html",
#         {"path": request.path},
#         status=404
#     )
#
#
# def server_error(request):
#     return render(request, "misc/500.html", status=500)
