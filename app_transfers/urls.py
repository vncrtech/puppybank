"""Module providing the URL patterns for the Transfer Transaction"""
from django.urls import path

from . import views

app_name = "app_transfers"

urlpatterns = [
    path('list', views.TransferTransactionList.as_view(), name='list'),
    path('view/<int:pk>/', views.TransferView.as_view(), name='view'),
    path('create', views.TransferCreate.as_view(), name='create'),
    path('create_warning_account', views.TransferCreateWarningAccount.as_view(),
         name='create_warning_account'),
    path('create_warning_balance', views.TransferCreateWarningBalance.as_view(),
         name='create_warning_balance'),
    path('create_warning_zero', views.TransferCreateWarningZero.as_view(),
         name='create_warning_zero')
]
