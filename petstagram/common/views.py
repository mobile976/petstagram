from django.shortcuts import redirect, render, resolve_url
from petstagram.common.models import Like
from petstagram.photos.models import Photo
from pyperclip import copy


def show_home_view(request):
    all_photos = Photo.objects.all()
    context = {
        'all_photos': all_photos,
    }
    return render(request, template_name='common/home-page.html', context=context)


def like_functionality(request, photo_id):
    photo = Photo.objects.get(id=photo_id)
    liked_object = Like.objects.filter(to_photo_id=photo_id).first()

    if liked_object:
        liked_object.delete()
    else:
        like = Like(to_photo=photo)
        like.save()
        
    return redirect(request.META.get('HTTP_REFERER') + f'#photo-{photo_id}')


def copy_link_to_clipboard(request, photo_id):
    link = request.META['HTTP_HOST'] + resolve_url('photo-details', photo_id)
    copy(link)
    return redirect(request.META.get('HTTP_REFERER') + f'#photo-{photo_id}')