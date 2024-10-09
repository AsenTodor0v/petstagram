from django.shortcuts import redirect, render

from petstagram.photos.models import Photo

# Create your views here.
def add_page(request):
    return render(request, 'photos/photo-add-page.html')

def photo_details_page(request, pk: int):
    return render(request, 'photos/photo-details-page.html')

def photo_edit_page(request, pk: int):
    
    return render(request, 'photos/photo-edit-page.html')

def photo_delete(request, pk: int):
    Photo.objects.get(pk=pk).delete()
    return redirect('home')
