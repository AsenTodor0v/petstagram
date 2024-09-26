from django.shortcuts import render

def login_page(request):
    return render(request, 'accounts/login-page.html')

def delete_page(request):
    return render(request, 'accounts/profile-delete-page.html')

def details_page(request):
    return render(request, 'accounts/profile-details-page.html')

def edit_page(request):
    return render(request, 'accounts/profile-edit-page.html')

def register_page(request):
    return render(request, 'accounts/register-page.html')