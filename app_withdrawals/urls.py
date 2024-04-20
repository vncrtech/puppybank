"""Module providing the URL patterns for the Withdraw Transaction"""
from django.urls import path

from . import views

app_name = "app_withdrawals"

urlpatterns = [
    path('list', views.WithdrawTransactionList.as_view(), name='list'),
    path('view/<int:pk>/', views.WithdrawView.as_view(), name='view'),
    path('create', views.WithdrawCreate.as_view(), name='create'),
    path('create_warning', views.WithdrawCreateWarning.as_view(),
         name='create_warning'),
    path('create_warning_zero', views.WithdrawCreateWarningAmountLessThanZero.as_view(),
         name='create_warning_zero'),
]
