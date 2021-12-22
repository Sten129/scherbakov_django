from django.urls import path
from . import views

urlpatterns = [
path("", views.index, name="index"),
path("group/<slug:slug>/", views.group_pictures, name="group"),
path('<int:picture_id>/', views.picture_view, name='picture'),

]