"""Module providing the URL patterns for the Generic Application"""

from django.urls import path

from . import views

app_name = "app_generic"

urlpatterns = [
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('about_inside', views.about_inside, name='about_inside'),
    path('about_outside', views.about_outside, name='about_outside'),
]
