"""Module providing the URL patterns for the Clients"""
from django.urls import path

from . import views

app_name = "app_clients"

urlpatterns = [
    path('list', views.ClientList.as_view(), name='list'),
    path('create', views.ClientCreate.as_view(), name='create'),
    path('update/<int:pk>/',
         views.ClientUpdate.as_view(), name='update'),
    path('delete/<int:pk>/',
         views.ClientDelete.as_view(), name='delete'),
]
