# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views
from petstagram.photos.models import Photo

from petstagram.accounts.forms import (
    AppUserCreationForm,
    AppUserLoginForm,
    ProfileEditForm,
)
from petstagram.accounts.models import Profile

UserModel = get_user_model()


class AppUserLogoutView(auth_views.LogoutView):
    pass


class AppUserRegisterView(views.CreateView):
    model = UserModel
    form_class = AppUserCreationForm
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('login')


class AppUserLoginView(auth_views.LoginView):
    form_class = AppUserLoginForm
    template_name = 'accounts/login-page.html'

class AppUserDetailView(views.DetailView):
    model = UserModel
    template_name = 'accounts/profile-details-page.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.object

        profile = user.profile
        photos = user.photo_set.all()
        pets = user.pet_set.all()

        total_likes_count = sum(
            p.like_set.count() for p in photos
        )

        context['profile'] = profile
        context['photos_count'] = photos.count()
        context['pets_count'] = pets.count()
        context['total_likes_count'] = total_likes_count
        context['user_pets'] = pets
        context['all_photos'] = photos

        context['user_photos'] = (
            Photo.objects
            .filter(user_id=user.pk)
            .order_by('-date_of_publication')
        )

        return context

class ProfileEditView(views.UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'accounts/profile-edit-page.html'

    def get_object(self, queryset=None):
        return self.request.user.profile

    def get_success_url(self):
        return reverse_lazy(
            'profile-details',
            kwargs={'pk': self.object.pk},
        )

class AppUserDeleteView(views.DeleteView):
    model = UserModel
    template_name = 'accounts/profile-delete-page.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return self.request.user

    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        user.delete()
        return redirect(self.get_success_url())