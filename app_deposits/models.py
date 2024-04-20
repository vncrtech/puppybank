"""Module providing a model for a Deposit Transaction"""

from django.db import models
from django.contrib.auth.models import User

from app_clients.models import Client


class DepositTransaction(models.Model):
    """This class describes the data for a Deposit Transaction"""

    # General Transaction Information
    transaction_date = models.DateField('Date')
    transaction_reference = models.UUIDField(
        'Reference #', unique=True, max_length=10)
    status = models.CharField('Status', max_length=50)

    # Transaction Computation
    deposit_amount = models.FloatField('Deposit Amount')
    currency = models.CharField('Currency', default='TREATS', max_length=20)
    start_balance = models.FloatField('Start Balance')
    new_balance = models.FloatField('New Balance')

    # Foreign Key
    puppy = models.ForeignKey(Client, default=None, on_delete=models.CASCADE)
    created_by = models.ForeignKey(
        User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.transaction_reference)
