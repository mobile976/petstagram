from django.shortcuts import render, redirect
from petstagram.pets.models import Pet
from petstagram.pets.forms import PetDeleteForm, PetForm
from petstagram.common.forms import CommentForm
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy

def add_pet(request):
    form = PetForm(request.POST or None)
    if form.is_valid():
        pet = form.save(commit=False)
        pet.user = request.user
        pet.save()
        return redirect('profile-details', pk=request.user.pk)
    context = {'form': form}
    return render(request, template_name='pets/pet-add-page.html', context=context)

class AddPetView(CreateView):
    model = Pet
    form_class = PetForm
    template_name = 'pets/pet-add-page.html'

    def form_valid(self, form):
        pet = form.save(commit=False)
        pet.user = self.request.user
        pet.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={'pk': self.request.user.pk})

def show_pet_details(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    all_photos = pet.photo_set.all()
    context = {
        'pet': pet,
        'all_photos': all_photos,
        'comment_form': CommentForm(),
    }
    return render(request, template_name='pets/pet-details-page.html', context=context)

class PetDetailsView(DetailView):
    model = Pet
    template_name = 'pets/pet-details-page.html'
    context_object_name = 'pet'
    slug_url_kwarg = 'pet_slug'   # URL дээрх <slug:pet_slug>

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pet = self.object
        context['all_photos'] = pet.photo_set.all()
        context['comment_form'] = CommentForm()
        return context

def edit_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    if request.method == 'GET':
        form = PetForm(instance=pet, initial=pet.__dict__)
    else:
        form = PetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect(to='pet-details', username=username, pet_slug=pet_slug)
        
        context = {'form': form}
        return render(request, template_name='pets/pet-edit-page.html', context=context)
    
class EditPetView(UpdateView):
    model = Pet
    form_class = PetForm
    template_name = 'pets/pet-edit-page.html'
    slug_url_kwarg = 'pet_slug'

    def get_success_url(self):
        return reverse_lazy('pet-details', kwargs={
            'username': self.kwargs['username'],
            'pet_slug': self.kwargs['pet_slug'],
        })

def delete_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    if request.method == 'POST':
        pet.delete()
        return redirect('profile-details', pk=request.user.pk)
    form = PetDeleteForm(initial=pet.__dict__)
    context = {'form': form}
    return render(request, template_name='pets/pet-delete-page.html', context=context)

class DeletePetView(DeleteView):
    model = Pet
    template_name = 'pets/pet-delete-page.html'
    context_object_name = 'pet'

    def get_object(self, queryset=None):
        return Pet.objects.get(slug=self.kwargs['pet_slug'])

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={'pk': self.request.user.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PetDeleteForm(initial=self.object.__dict__)
        return context

    def delete(self, request, *args, **kwargs):
        pet = self.get_object()
        pet.delete()
        return redirect(self.get_success_url())