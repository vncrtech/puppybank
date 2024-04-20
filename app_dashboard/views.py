from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from app_deposits.models import DepositTransaction
from app_withdrawals.models import WithdrawTransaction
from app_transfers.models import TransferTransaction


@login_required(login_url="/app_generic/login")
def dashboard(request):
    """This method is for generating the dashboard"""
    l_deposit_aggregate, l_withdraw_aggregate, l_transfer_aggregate = 0, 0, 0
    l_deposit_trx_count, l_withdraw_trx_count, l_transfer_trx_count = 0, 0, 0
    obj_list_deposit_trx = DepositTransaction.objects.all()
    obj_list_withdraw_trx = WithdrawTransaction.objects.all()
    obj_list_transfer_trx = TransferTransaction.objects.all()
    for item in obj_list_deposit_trx:
        l_deposit_trx_count += 1
        l_deposit_aggregate += item.deposit_amount
    for item in obj_list_withdraw_trx:
        l_withdraw_trx_count += 1
        l_withdraw_aggregate += item.withdraw_amount
    for item in obj_list_transfer_trx:
        l_transfer_trx_count += 1
        l_transfer_aggregate += item.transfer_amount
    l_trx_count = l_deposit_trx_count + l_withdraw_trx_count + l_transfer_trx_count
    l_context = {'l_deposit_aggregate': l_deposit_aggregate,
                 'l_withdraw_aggregate': l_withdraw_aggregate,
                 'l_transfer_aggregate': l_transfer_aggregate,
                 'l_trx_count': l_trx_count}
    return render(request, 'app_dashboard/dashboard.html', l_context)
