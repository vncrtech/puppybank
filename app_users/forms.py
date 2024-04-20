"""Module providing a form for a Transfer Transaction"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserCreationFormExtended(UserCreationForm):
    """This class describes the form for a Transfer Transaction"""

    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control form-control-user"
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control form-control-user"
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control form-control-user    "
    }))

    class Meta:
        """Transfer Transaction fields"""

        model = User
        fields = ['username',
                  'password1',
                  'password2',
                  ]
