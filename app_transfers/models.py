"""Module providing a model for a Transfer Transaction"""

from django.db import models
from django.contrib.auth.models import User

from app_clients.models import Client


class TransferTransaction(models.Model):
    """This model describes the data for a Transfer Transaction"""

    # General Transaction Information
    transaction_date = models.DateField('Date')
    transaction_reference = models.UUIDField(
        'Reference #', unique=True, max_length=10)
    status = models.CharField('Status', max_length=50)

    # Transaction Computation
    transfer_amount = models.FloatField('Transfer Amount')
    currency = models.CharField('Currency', default='TREATS', max_length=20)

    # Foreign Key
    created_by = models.ForeignKey(
        User, default=None, on_delete=models.CASCADE)
    from_puppy = models.ForeignKey(
        Client, related_name='from_puppy', default=None, on_delete=models.CASCADE)
    to_puppy = models.ForeignKey(
        Client, related_name='to_puppy', default=None, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.transaction_reference)
