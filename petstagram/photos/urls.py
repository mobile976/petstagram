# photos/urls.py
from django.urls import path
from . import views

app_name = 'photos'

urlpatterns = [
    path('add/', views.photo_add_view, name='photo-add'),
    path('<int:pk>/', views.photo_details_view, name='photo-details'),
    path('<int:pk>/edit/', views.photo_edit_view, name='photo-edit'),
]