from django.urls import include, path

from petstagram.accounts import views

urlpatterns = [
    path('register/', views.register_page, name='register'),
    path('login/', views.login_page, name='login'),
    path('profile/<int:pk>/', include([
        path('', views.details_page, name='details'),
        path('edit/', views.edit_page, name='edit'),
        path('delete/', views.delete_page, name='delete'),
    ]
    ))
]