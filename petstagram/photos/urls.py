# photos/urls.py
from django.urls import path
from petstagram.photos import views

urlpatterns = [
    path('add/', views.photo_add, name='photo-add'),
    path('<int:pk>/', views.show_photo_details, name='photo-details'),
    path('<int:pk>/edit/', views.photo_edit_view, name='edit-photo'),
]