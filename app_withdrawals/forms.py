"""Module providing a form for a Withdrawal Transaction"""

from django import forms
from django.forms import ModelForm

from app_clients.models import Client

from . import models


class WithdrawalTransactionForm(ModelForm):
    """This class describes the form for a Withdrawal Transaction"""

    transaction_date = forms.DateField(widget=forms.TextInput(attrs={
        "class": "form-control form-control-user",
        'readonly': '',
    }))
    transaction_reference = forms.UUIDField(widget=forms.TextInput(attrs={
        "class": "form-control form-control-user",
        'readonly': '',
    }))
    status = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control form-control-user",
        'readonly': '',
    }))
    withdraw_amount = forms.FloatField(widget=forms.NumberInput(attrs={
        "class": "form-control form-control-user"
    }))
    currency = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control form-control-user",
        'readonly': '',
        "value": "TREATS"
    }))
    puppy = forms.ModelChoiceField(queryset=Client.objects.all(), widget=forms.Select(attrs={
        "class": "form-control",
        "style": "border-radius: 10rem; height: 3rem"
    }))

    class Meta:
        """Withdrawal Transaction fields"""

        model = models.WithdrawTransaction
        fields = ['transaction_date',
                  'transaction_reference',
                  'status',
                  'withdraw_amount',
                  'currency',
                  'puppy']
