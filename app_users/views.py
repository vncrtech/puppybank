"""Module providing the views for Users"""

from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import redirect
from django.urls import reverse_lazy

from . import forms


LoginRequiredMixin.login_url = "/app_generic/login"


class UserRegister(CreateView):
    """Class-based view for User Register"""
    model = User
    form_class = forms.UserCreationFormExtended
    template_name = 'app_users/register.html'
    success_url = reverse_lazy('app_generic:login')


class UserList(LoginRequiredMixin, ListView):
    """Class-based view for User List"""
    model = User
    template_name = 'app_users/list.html'


class UserCreate(LoginRequiredMixin, CreateView):
    """Class-based view for User Create"""
    model = User
    form_class = forms.UserCreationFormExtended
    template_name = 'app_users/create.html'
    success_url = 'list'
    extra_context = {'delete_hidden': 'hidden'}

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        response = super().form_valid(form)
        return response


class UserUpdate(LoginRequiredMixin, UpdateView):
    """Class-based view for User Update"""
    model = User
    form_class = forms.UserCreationFormExtended
    template_name = 'app_users/update.html'
    success_url = reverse_lazy('app_users:list')

    def get_context_data(self, **kwargs):
        form = forms.UserCreationFormExtended(instance=self.object)
        context = {'form': form,
                   'id': self.object.id,
                   'confirm_hidden': 'hidden',
                   'disabled': 'disabled'}
        return context

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        response = super().form_valid(form)
        return response


class UserDelete(LoginRequiredMixin, DeleteView):
    """Class-based view for User Delete"""
    model = User
    success_url = reverse_lazy('app_users:list')

    def form_valid(self, form):
        response = super().form_valid(form)
        if 'delete_object' in self.request.POST:
            return redirect('app_users:list')
        return response
