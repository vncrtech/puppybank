"""Module providing the views for the Withdrawal Transactions"""
import uuid

from datetime import date

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView
from django.views.generic.edit import FormView, CreateView

from . import forms, models

LoginRequiredMixin.login_url = "/app_generic/login"


class WithdrawTransactionList(LoginRequiredMixin, ListView):
    """Class-based view for Withdrawal Transaction List"""
    model = models.WithdrawTransaction
    template_name = 'app_withdrawals/list.html'


class WithdrawCreate(LoginRequiredMixin, CreateView):
    """Class-based view for Withdrawal Transaction Create"""
    model = models.WithdrawTransaction
    form_class = forms.WithdrawalTransactionForm
    template_name = 'app_withdrawals/create.html'
    success_url = 'list'
    extra_context = {'delete_hidden': 'hidden',
                     'warning': 'style=display:none',
                     'warning_message': ''}

    def __init__(self):
        self.initial = {'transaction_date': date.today(),
                        'transaction_reference': uuid.uuid4(),
                        'status': 'OPEN'}

    def form_valid(self, form):
        obj_client = get_object_or_404(
            models.Client, pk=self.request.POST['puppy'])
        current_balance = obj_client.account_balance
        if float(self.request.POST['withdraw_amount']) <= 0:
            return redirect('app_withdrawals:create_warning_zero')
        if current_balance < float(self.request.POST['withdraw_amount']):
            return redirect('app_withdrawals:create_warning')
        form.instance.start_balance = current_balance
        form.instance.new_balance = form.instance.start_balance - \
            float(self.request.POST['withdraw_amount'])
        form.instance.status = 'DONE'
        form.instance.created_by = self.request.user
        response = super().form_valid(form)
        # update balance of the client object
        obj_client.account_balance = form.instance.new_balance
        obj_client.save()
        return response


class WithdrawCreateWarning(WithdrawCreate):
    """Class-based view for Withdrawal Transaction Create with Warning"""
    extra_context = {'delete_hidden': 'hidden',
                     'warning': 'style=display:true',
                     'warning_message': 'The withdraw amount cannot be more than the account balance.'}


class WithdrawCreateWarningAmountLessThanZero(WithdrawCreate):
    """Class-based view for Withdrawal Transaction Create with Warning"""
    extra_context = {'delete_hidden': 'hidden',
                     'warning': 'style=display:true',
                     'warning_message': 'The withdraw amount should be more than zero.'}


class WithdrawView(LoginRequiredMixin, FormView):
    """Class-based view for Withdrawal Transaction View"""
    model = models.WithdrawTransaction
    template_name = 'app_withdrawals/create.html'
    success_url = 'list'

    def get_context_data(self, **kwargs):
        l_id = self.kwargs['pk']
        obj_withdraw_trx = get_object_or_404(
            models.WithdrawTransaction, pk=l_id)
        form = forms.WithdrawalTransactionForm(instance=obj_withdraw_trx)
        context = {'form': form,
                   'id': l_id,
                   'confirm_hidden': 'hidden',
                   'delete_hidden': 'hidden',
                   'disabled': 'disabled',
                   'warning': 'style=display:none',
                   'warning_message': ''}
        return context
