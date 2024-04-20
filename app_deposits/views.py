"""Module providing the views for the Deposit Transactions"""
import uuid

from datetime import date

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import FormView, CreateView
from django.shortcuts import redirect, get_object_or_404

from . import forms, models

LoginRequiredMixin.login_url = "/app_generic/login"


class DepositTransactionList(LoginRequiredMixin, ListView):
    """Class-based view for Deposit Transaction List"""
    model = models.DepositTransaction
    template_name = 'app_deposits/list.html'


class DepositCreate(LoginRequiredMixin, CreateView):
    """Class-based view for Deposit Transaction Create"""
    model = models.DepositTransaction
    form_class = forms.DepositTransactionForm
    template_name = 'app_deposits/create.html'
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
        if float(self.request.POST['deposit_amount']) <= 0:
            return redirect('app_deposits:create_warning_zero')
        form.instance.start_balance = obj_client.account_balance
        form.instance.new_balance = form.instance.start_balance + \
            float(self.request.POST['deposit_amount'])
        form.instance.status = 'DONE'
        form.instance.created_by = self.request.user
        response = super().form_valid(form)
        # update balance of the client object
        obj_client.account_balance = form.instance.new_balance
        obj_client.save()
        return response


class DepositCreateWarningZero(DepositCreate):
    """Class-based view for Deposit Transaction Create with Warning"""
    extra_context = {'delete_hidden': 'hidden',
                     'warning': 'style=display:true',
                     'warning_message': 'The deposit amount should be more than zero.'}


class DepositView(LoginRequiredMixin, FormView):
    """Class-based view for Deposit Transaction View"""
    model = models.DepositTransaction
    template_name = 'app_deposits/create.html'
    success_url = 'list'

    def get_context_data(self, **kwargs):
        l_id = self.kwargs['pk']
        obj_deposit_trx = get_object_or_404(models.DepositTransaction, pk=l_id)
        form = forms.DepositTransactionForm(instance=obj_deposit_trx)
        context = {'form': form,
                   'id': l_id,
                   'confirm_hidden': 'hidden',
                   'delete_hidden': 'hidden',
                   'disabled': 'disabled',
                   'warning': 'style=display:none',
                   'warning_message': ''}
        return context
