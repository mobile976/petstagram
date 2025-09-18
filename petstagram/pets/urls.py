# pets/urls.py
from django.urls import path
from . import views

app_name = 'pets'

urlpatterns = [
    path('add/', views.pet_add_view, name='pet-add'),
    path('<str:username>/pet/<slug:pet_slug>/', views.pet_details_view, name='pet-details'),
    path('<str:username>/pet/<slug:pet_slug>/edit/', views.pet_edit_view, name='pet-edit'),
    path('<str:username>/pet/<slug:pet_slug>/delete/', views.pet_delete_view, name='pet-delete'),
]