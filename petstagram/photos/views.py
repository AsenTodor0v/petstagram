from django.shortcuts import render

# Create your views here.
def add_page(request):
    return render(request, 'photos/photo-add-page.html')

def details_page(request):
    return render(request, 'photos/photo-details-page.html')

def edit_page(request):
    return render(request, 'photos/photo-edit-page.html')