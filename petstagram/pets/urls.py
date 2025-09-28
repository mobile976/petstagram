# pets/urls.py
from django.urls import path
from petstagram.pets import views

urlpatterns = [
    path('add/', views.AddPetView.as_view(), name='pet-add'),
    path('<str:username>/pet/<slug:pet_slug>/', views.PetDetailsView.as_view(), name='pet-details'),
    path('<str:username>/pet/<slug:pet_slug>/edit/', views.EditPetView.as_view(), name='pet-edit'),
    path('<str:username>/pet/<slug:pet_slug>/delete/', views.DeletePetView.as_view(), name='pet-delete'),
]