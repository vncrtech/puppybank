"""Module providing the views for the Generic Application"""

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect


def home(request):
    """Function-based view for Home"""
    return render(request, "app_generic/login.html")


def login_view(request):
    """Function-based view for Login"""
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # if user was redirected to the login page from a page inside the application
            if 'next' in request.POST:
                if request.POST['next']:
                    return redirect(request.POST.get('next'))
            return redirect('app_dashboard:dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'app_generic/login.html', {'form': form})


def logout_view(request):
    """Function-based view for Logout"""
    logout(request)
    return redirect('app_generic:login')


def about_outside(request):
    """Function-based view for About Page"""
    return render(request, 'app_generic/about_outside.html')

def about_inside(request):
    """Function-based view for About Page"""
    return render(request, 'app_generic/about_inside.html')