"""Module providing a form for a Transfer Transaction"""

from django import forms
from django.forms import ModelForm

from app_clients.models import Client

from . import models


class TransferTransactionForm(ModelForm):
    """This class describes the form for a Transfer Transaction"""

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
    transfer_amount = forms.FloatField(widget=forms.NumberInput(attrs={
        "class": "form-control form-control-user"
    }))
    currency = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control form-control-user",
        'readonly': '',
        "value": "TREATS"
    }))
    from_puppy = forms.ModelChoiceField(queryset=Client.objects.all(), widget=forms.Select(attrs={
        "class": "form-control",
        "style": "border-radius: 10rem; height: 3rem"
    }))
    to_puppy = forms.ModelChoiceField(queryset=Client.objects.all(), widget=forms.Select(attrs={
        "class": "form-control",
        "style": "border-radius: 10rem; height: 3rem"
    }))

    class Meta:
        """Transfer Transaction fields"""

        model = models.TransferTransaction
        fields = ['transaction_date',
                  'transaction_reference',
                  'status',
                  'transfer_amount',
                  'currency',
                  'from_puppy',
                  'to_puppy']
