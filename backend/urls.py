from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

# router.register()

urlpatterns = [
path("", views.index, name="index"),
path("group/<slug:slug>/", views.group_pictures, name="group"),
path('<int:picture_id>/', views.picture_view, name='picture'),

]