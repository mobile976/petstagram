from django.shortcuts import render
from petstagram.pets.models import Pet

def pet_add_view(request):
    return render(request, 'pets/pet-add-page.html')

def show_pet_details(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    all_photos = pet.photo_set.all()
    context = {
        'pet': pet,
        'all_photos': all_photos,
    }
    return render(request, template_name='pets/pet-details-page.html', context=context)

def pet_edit_view(request, username, pet_slug):
    ctx = {'username': username, 'pet_slug': pet_slug}
    return render(request, 'pets/pet-edit-page.html', ctx)

def pet_delete_view(request, username, pet_slug):
    ctx = {'username': username, 'pet_slug': pet_slug}
    return render(request, 'pets/pet-delete-page.html', ctx)