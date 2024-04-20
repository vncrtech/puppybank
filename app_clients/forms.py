"""Module providing a form for a Client Data"""

from django import forms
from django.forms import ModelForm

from . import models


class ClientForm(ModelForm):
    """This class describes the form for a Client Data"""

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control form-control-user"
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control form-control-user"
    }))
    address = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control form-control-user"
    }))
    account_number = forms.UUIDField(widget=forms.TextInput(attrs={
        "class": "form-control form-control-user",
        'readonly': ''
    }))
    mobile_number = forms.IntegerField(widget=forms.TextInput(attrs={
        "class": "form-control form-control-user"
    }))
    email_address = forms.EmailField(widget=forms.EmailInput(attrs={
        "class": "form-control form-control-user"
    }))
    account_balance = forms.FloatField(widget=forms.TextInput(attrs={
        "class": "form-control form-control-user",
        'readonly': '',
        'value': 0
    }))

    class Meta:
        """Client Data fields"""

        model = models.Client
        fields = ['account_number',
                  'account_balance',
                  'first_name',
                  'last_name',
                  'address',
                  'mobile_number',
                  'email_address']
