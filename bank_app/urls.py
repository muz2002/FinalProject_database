from django.urls import path
from .views import *

urlpatterns = [
    
    path("customer/", customer_detail, name="customer_detail"),
    path("account/", account_detail, name="account_detail"),
    path('card/<int:card_id>/', card_detail, name='card_detail'),
    path('transaction/<int:transaction_id>/', transaction_detail, name='transaction_detail'),
    path('loan/<int:loan_id>/', loan_detail, name='loan_detail'),
    path('service/<int:purchase_id>/', service_purchase_detail, name='service_purchase_detail'),
    path("home/",home,name="home")
]