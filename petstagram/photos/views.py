from django.shortcuts import render

def photo_add_view(request):
    return render(request, 'photos/photo-add-page.html')

def photo_details_view(request, pk):
    return render(request, 'photos/photo-details-page.html', {'pk': pk})

def photo_edit_view(request, pk):
    return render(request, 'photos/photo-edit-page.html', {'pk': pk})