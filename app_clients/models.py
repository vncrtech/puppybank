"""Module providing a model for a Clients"""

from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    """This model describes the data for a Client"""

    first_name = models.CharField('First Name', max_length=20)
    last_name = models.CharField('Last Name', max_length=20)
    address = models.CharField('Address', max_length=50)
    account_number = models.UUIDField(
        'Account Number', unique=True, max_length=10)
    mobile_number = models.IntegerField('Mobile Number')
    email_address = models.EmailField(
        'Email Address', max_length=200, unique=True)
    account_balance = models.FloatField('Account Balance')

    # Foreign Key
    created_by = models.ForeignKey(
        User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + " " + self.last_name
