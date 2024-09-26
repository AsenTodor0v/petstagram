from django.urls import path
from django.urls import include

from petstagram.pets import views

urlpatterns = [
    path('add/', views.add_page, name='add'),
    path('<str:username>/pet/<slug:pet_slug>/', include([
        path('', views.details_page, name='details'),
        path('edit/', views.edit_page, name='edit'),
        path('delete/', views.delete_page, name='delete'),
    ]))
]
