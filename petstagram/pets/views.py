from django.shortcuts import render

def pet_add_view(request):
    return render(request, 'pets/pet-add-page.html')

def pet_details_view(request, username, pet_slug):
    ctx = {'username': username, 'pet_slug': pet_slug}
    return render(request, 'pets/pet-details-page.html', ctx)

def pet_edit_view(request, username, pet_slug):
    ctx = {'username': username, 'pet_slug': pet_slug}
    return render(request, 'pets/pet-edit-page.html', ctx)

def pet_delete_view(request, username, pet_slug):
    ctx = {'username': username, 'pet_slug': pet_slug}
    return render(request, 'pets/pet-delete-page.html', ctx)