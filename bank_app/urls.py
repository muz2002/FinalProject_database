from django.urls import path
from .views import *
from django.contrib.staticfiles.urls import  staticfiles_urlpatterns
urlpatterns = [
    
    path("customer/", customer_detail, name="customer_detail"),
    path("account/", account_detail, name="account_detail"),
    path('card/', card_detail, name='card_detail'),
    path('transaction/', transaction_detail, name='transaction_detail'),
    path('loan/', loan_detail, name='loan_detail'),
    path('service/', service_purchase_detail, name='service_purchase_detail'),
    path("home/",home,name="home"),
    path('transfer/', transfer_funds, name='transfer_funds'),
    path('success/',  transaction_success, name='transaction_success'),
]

urlpatterns += staticfiles_urlpatterns()