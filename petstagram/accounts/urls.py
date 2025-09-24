from django.urls import path
from petstagram.accounts import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('profile/<int:pk>/', views.show_profile_details, name='profile-details'),
    path('profile/<int:pk>/edit/', views.edit_profile, name='profile-edit'),
    path('profile/<int:pk>/delete/', views.delete_profile, name='profile-delete'),
]