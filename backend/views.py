from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Picture, Type, Event, Exhibition, Letter, Persone, Location, Photo, Document, Description

from django.core.paginator import Paginator

def index(request):
    picture_list = Picture.objects.all()
    paginator = Paginator(picture_list, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(
        request,
        'index.html',
        {'page': page, 'paginator': paginator}
    )

def group_pictures(request, slug):
    # подставить переменную - критерий группировки
    # queryset = Book.objects.filter(title__startswith='M') - пример Queryset.
    # делаем queryset по выставкам, жанрам, годам, технике, людям, музеям, владельцам
    # queryset = Picture.objects.filter(slug=request.slug)
    # group = get_object_or_404(queryset, slug=slug)
    group = get_object_or_404(Type, slug=slug)
    picture_list_group = type.pictures.all()
    paginator = Paginator(picture_list_group, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(
        request,
        'group.html',
        {
            'group': group,
            'page': page,
            'paginator': paginator
        }
    )

def picture_view(request, picture_id):
    post = get_object_or_404(Picture, id=picture_id)
    description = pictures.descriptions.all()
    # form = PictureForm()
    return render(request, 'preview.html',
                  {'picture': picture, 'type': picture.type, 'description': description, 'form': form})


def page_not_found(request, exception):  # noqa
    return render(
        request,
        "misc/404.html",
        {"path": request.path},
        status=404
    )


def server_error(request):
    return render(request, "misc/500.html", status=500)
