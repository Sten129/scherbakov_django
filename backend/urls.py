from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    TypeViewSet,
    TechnicViewSet,
    GenreViewSet,
    BookViewSet,
    PersoneViewSet,
    PictureViewSet,
    ArticleViewSet,
    LetterViewSet,
    LocationViewSet,
    DocumentViewSet,
    ExhibitionViewSet,
    OwnerViewSet,
)

router = DefaultRouter()

router.register('types', TypeViewSet, basename='types')
router.register('genres', GenreViewSet, basename='genres')
router.register('technics', TechnicViewSet, basename='technics')
router.register('locations', LocationViewSet, basename='locations')
router.register('owners', OwnerViewSet, basename='owners')
router.register('books', BookViewSet, basename='books')
router.register('letters', LetterViewSet, basename='letters')
router.register('articles', ArticleViewSet, basename='articles')
router.register('exhibitions', ExhibitionViewSet, basename='exhibitions')
router.register('documents', DocumentViewSet, basename='documents')
router.register('pictures', PictureViewSet, basename='pictures')
router.register('persons', PersoneViewSet, basename='persons')

urlpatterns = [
    path('', include(router.urls))
]
