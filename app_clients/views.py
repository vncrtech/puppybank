"""Module providing the views for the Clients"""
import uuid

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import redirect
from django.urls import reverse_lazy

from . import forms, models

LoginRequiredMixin.login_url = "/bank/login"


class ClientList(LoginRequiredMixin, ListView):
    """Class-based view for Client List"""
    model = models.Client
    template_name = 'app_clients/list.html'


class ClientCreate(LoginRequiredMixin, CreateView):
    """Class-based view for Client Create"""
    model = models.Client
    form_class = forms.ClientForm
    template_name = 'app_clients/create.html'
    success_url = 'list'
    extra_context = {'delete_hidden': 'hidden'}

    def __init__(self):
        self.initial = {
            'account_number': uuid.uuid4()}

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        response = super().form_valid(form)
        return response


class ClientUpdate(LoginRequiredMixin, UpdateView):
    """Class-based view for Client Update"""
    model = models.Client
    form_class = forms.ClientForm
    template_name = 'app_clients/update.html'
    success_url = reverse_lazy('app_clients:list')

    def get_context_data(self, **kwargs):
        form = forms.ClientForm(instance=self.object)
        context = {'form': form,
                   'id': self.object.id,
                   'confirm_add_hidden': 'hidden'}
        return context

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        response = super().form_valid(form)
        return response


class ClientDelete(LoginRequiredMixin, DeleteView):
    """Class-based view for Client Delete"""
    model = models.Client
    success_url = reverse_lazy('app_clients:list')

    def form_valid(self, form):
        response = super().form_valid(form)
        if 'delete_object' in self.request.POST:
            return redirect('app_clients:list')
        return response
