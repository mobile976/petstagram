from django.shortcuts import render, redirect
from petstagram.photos.models import Photo
from petstagram.photos.forms import PhotoCreateForm, PhotoEditForm
from petstagram.common.forms import CommentForm

def add_photo(request):
    form = PhotoCreateForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    context = {
        'form': form,
    }
    return render(request, template_name='photos/photo-add-page.html', context=context)

def show_photo_details(request, pk):
    photo = Photo.objects.get(pk=pk)
    likes = photo.like_set.all()    
    comments = photo.comment_set.all()

    context = {
        'likes': likes,
        'comments': comments,
        'photo': photo,
        'comment_form': CommentForm(),
    }
    return render(request, template_name='photos/photo-details-page.html', context=context)

def edit_photo(request, pk):
    photo = Photo.objects.get(pk=pk)
    form = PhotoEditForm(request.POST or None, request.FILES or None, instance=photo)
    if form.is_valid():
        form.save()
        return redirect('show photo details', pk=pk)
    context = {
        'form': form,
        'pk': pk,
    }
    return render(request, template_name='photos/photo-edit-page.html', context=context)

def delete_photo(request, pk):
    photo = Photo.objects.get(pk=pk)
    photo.delete()
    return redirect('home')