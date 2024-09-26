from django.urls import path
from django.urls import include

from petstagram.photos import views

urlpatterns = [
    path('add/', views.add_page, name='add'),
    path('<int:pk>/', include([
        path('', views.details_page, name='details'),
        path('edit/', views.edit_page, name='edit'),
    ]))
]