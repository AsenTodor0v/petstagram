from django.shortcuts import render

# Create your views here.

def add_page(request):
    return render(request, 'pets/pet-add-page.html')

def delete_page(request, username: str, pet_slug: str):
    return render(request, 'pets/pet-delete-page.html')

def details_page(request, username: str, pet_slug: str):
    return render(request, 'pets/pet-details-page.html')

def edit_page(request, username: str, pet_slug: str):
    return render(request, 'pets/pet-edit-page.html')