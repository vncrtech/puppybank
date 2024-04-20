"""Module providing the views for the Transfer Transactions"""
import uuid

from datetime import date

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import FormView, CreateView
from django.shortcuts import redirect, get_object_or_404

from . import forms, models

LoginRequiredMixin.login_url = "/app_generic/login"


class TransferTransactionList(LoginRequiredMixin, ListView):
    """Class-based view for Transfer Transaction List"""
    model = models.TransferTransaction
    template_name = 'app_transfers/list.html'


class TransferCreate(LoginRequiredMixin, CreateView):
    """Class-based view for Transfer Transaction Create"""
    model = models.TransferTransaction
    form_class = forms.TransferTransactionForm
    template_name = 'app_transfers/create.html'
    success_url = 'list'
    extra_context = {'delete_hidden': 'hidden',
                     'warning': 'style=display:none',
                     'warning_message': ''}

    def __init__(self):
        self.initial = {'transaction_date': date.today(),
                        'transaction_reference': uuid.uuid4(),
                        'status': 'OPEN'}

    def form_valid(self, form):
        obj_from_client = get_object_or_404(
            models.Client, pk=self.request.POST['from_puppy'])
        obj_to_client = get_object_or_404(
            models.Client, pk=self.request.POST['to_puppy'])
        if float(self.request.POST['transfer_amount']) <= 0:
            return redirect('app_transfers:create_warning_zero')
        if obj_from_client == obj_to_client:
            return redirect('app_transfers:create_warning_account')
        if obj_from_client.account_balance < form.instance.transfer_amount:
            return redirect('app_transfers:create_warning_balance')
        form.instance.status = 'DONE'
        form.instance.created_by = self.request.user
        response = super().form_valid(form)
        # update balance of the from-client object
        obj_from_client.account_balance = obj_from_client.account_balance - \
            form.instance.transfer_amount
        obj_from_client.save()
        # update balance of the to-client object
        obj_to_client.account_balance = obj_to_client.account_balance + \
            form.instance.transfer_amount
        obj_to_client.save()
        return response


class TransferCreateWarningAccount(TransferCreate):
    """Class-based view for Transfer Transaction Create"""
    extra_context = {'delete_hidden': 'hidden',
                     'warning': 'style=display:true',
                     'warning_message': 'The source and destination puppy cannot be the same.'}


class TransferCreateWarningBalance(TransferCreate):
    """Class-based view for Transfer Transaction Create"""
    extra_context = {'delete_hidden': 'hidden',
                     'warning': 'style=display:true',
                     'warning_message': 'The transfer amount cannot be more than the account balance.'}


class TransferCreateWarningZero(TransferCreate):
    """Class-based view for Transfer Transaction Create"""
    extra_context = {'delete_hidden': 'hidden',
                     'warning': 'style=display:true',
                     'warning_message': 'The transfer amount should be more than zero.'}


class TransferView(LoginRequiredMixin, FormView):
    """Class-based view for Transfer Transaction View"""
    model = models.TransferTransaction
    template_name = 'app_transfers/create.html'
    success_url = 'list'

    def get_context_data(self, **kwargs):
        l_id = self.kwargs['pk']
        obj_transfer_trx = get_object_or_404(
            models.TransferTransaction, pk=l_id)
        form = forms.TransferTransactionForm(instance=obj_transfer_trx)
        context = {'form': form,
                   'id': l_id,
                   'confirm_hidden': 'hidden',
                   'delete_hidden': 'hidden',
                   'disabled': 'disabled',
                   'warning': 'style=display:none',
                   'warning_message': ''}
        return context
