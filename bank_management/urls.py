"""
URL configuration for bank_management project.

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
from django.urls import path
from bank_app.views import *


urlpatterns = [
    path("admin/", admin.site.urls),
    path("customer/<int:customer_id>/", customer_detail, name="customer_detail"),
    path("account/<int:account_id>/", account_detail, name="account_detail"),
    path('card/<int:card_id>/', card_detail, name='card_detail'),
    path('transaction/<int:transaction_id>/', transaction_detail, name='transaction_detail'),
    path('loan/<int:loan_id>/', loan_detail, name='loan_detail'),
    path('service/<int:purchase_id>/', service_purchase_detail, name='service_purchase_detail'),
]

