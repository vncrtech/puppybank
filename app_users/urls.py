"""Module providing the URL patterns for the Users"""
from django.urls import path

from . import views

app_name = "app_users"

urlpatterns = [
    path('register', views.UserRegister.as_view(), name='register'),
    path('list', views.UserList.as_view(), name='list'),
    path('create', views.UserCreate.as_view(), name='create'),
    path('update/<int:pk>/', views.UserUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', views.UserDelete.as_view(), name='delete'),
]
