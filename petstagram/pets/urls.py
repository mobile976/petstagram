# pets/urls.py
from django.urls import path
from petstagram.pets import views

urlpatterns = [
    path('add/', views.add_pet, name='pet-add'),
    path('<str:username>/pet/<slug:pet_slug>/', views.show_pet_details, name='pet-details'),
    path('<str:username>/pet/<slug:pet_slug>/edit/', views.edit_pet, name='pet-edit'),
    path('<str:username>/pet/<slug:pet_slug>/delete/', views.delete_pet, name='pet-delete'),
]