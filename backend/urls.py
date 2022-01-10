from django.urls import path, include
from backend import views
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

router.register('type', TypeViewSet, basename='type')
router.register('genre', GenreViewSet, basename='genre')
router.register('technic', TechnicViewSet, basename='technic')
router.register('location', LocationViewSet, basename='location')
router.register('owner', OwnerViewSet, basename='owner')
router.register('book', BookViewSet, basename='book')
router.register('letter', LetterViewSet, basename='letter')
router.register('article', ArticleViewSet, basename='article')
router.register('exhibition', ExhibitionViewSet, basename='exhibitions')
router.register('document', DocumentViewSet, basename='document')
router.register('picture', PictureViewSet, basename='picture')
router.register('persone', PersoneViewSet, basename='persone')

urlpatterns = [
    path('', include(router.urls))
    # path("", views.index, name="index"),
    # path("group/<slug:slug>/", views.group_pictures, name="group"),
    # path('<int:picture_id>/', views.picture_view, name='picture'),

]
