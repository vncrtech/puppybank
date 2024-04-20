"""Module providing the URL patterns for the Deposit Transaction"""
from django.urls import path

from . import views

app_name = "app_deposits"

urlpatterns = [
    path('list', views.DepositTransactionList.as_view(), name='list'),
    path('view/<int:pk>/', views.DepositView.as_view(), name='view'),
    path('create', views.DepositCreate.as_view(), name='create'),
    path('create_warning_zero', views.DepositCreateWarningZero.as_view(),
         name='create_warning_zero'),
]
