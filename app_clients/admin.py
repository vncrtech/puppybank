"""This is for regisering models to the admin site"""
from django.contrib import admin

from app_clients.models import Client
from app_deposits.models import DepositTransaction
from app_withdrawals.models import WithdrawTransaction
from app_transfers.models import TransferTransaction

admin.site.register(Client)
admin.site.register(DepositTransaction)
admin.site.register(WithdrawTransaction)
admin.site.register(TransferTransaction)
