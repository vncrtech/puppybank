"""
URL configuration for puppybank project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from app_generic.views import home

urlpatterns = [
    path("", home),
    path('admin/', admin.site.urls),
    path("app_generic/", include("app_generic.urls")),
    path("app_users/", include("app_users.urls")),
    path("app_clients/", include("app_clients.urls")),
    path("app_deposits/", include("app_deposits.urls")),
    path("app_withdrawals/", include("app_withdrawals.urls")),
    path("app_transfers/", include("app_transfers.urls")),
    path("app_dashboard/", include("app_dashboard.urls"))
]
