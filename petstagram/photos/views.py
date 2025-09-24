from django.shortcuts import render
from petstagram.accounts import models
from petstagram.photos.models import Photo

def photo_add(request):
    return render(request, 'photos/photo-add-page.html')

def show_photo_details(request, pk):
    photo = Photo.objects.get(pk=pk)
    likes = photo.like_set.all()    
    comments = photo.comment_set.all()

    context = {
        'likes': likes,
        'comments': comments,
        'photo': photo,
    }
    return render(request, template_name='photos/photo-details-page.html', context=context)

def photo_edit_view(request, pk):
    return render(request, 'photos/photo-edit-page.html', {'pk': pk})