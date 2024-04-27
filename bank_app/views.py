from django.shortcuts import render

# Create your views here.
# views.py
from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import Customer, Account, Card, Transaction, Loan, Customerservicepurchase


def home(request):
    return render(request, "base.html")


def customer_detail(request):

    customer = get_object_or_404(Customer, pk=request.user.account.customer_id)
    accounts = Account.objects.filter(customer=customer)
    cards = Card.objects.filter(customer=customer)
    loans = Loan.objects.filter(customer=customer)
    services = Customerservicepurchase.objects.filter(customer=customer)
    return render(
        request,
        "customer_detail.html",
        {
            "customer": customer,
            "accounts": accounts,
            "cards": cards,
            "loans": loans,
            "services": services,
        },
    )


def account_detail(request):
    account = get_object_or_404(Account, pk=request.user.account.customer_id)
    transactions = Transaction.objects.filter(account=account)
    return render(
        request,
        "account_detail.html",
        {"account": account, "transactions": transactions},
    )


def card_detail(request, card_id):
    card = get_object_or_404(Card, pk=card_id)
    return render(request, "card_detail.html", {"card": card})


def transaction_detail(request, transaction_id):
    transaction = get_object_or_404(Transaction, pk=transaction_id)
    return render(request, "transaction_detail.html", {"transaction": transaction})


def loan_detail(request, loan_id):
    loan = get_object_or_404(Loan, pk=loan_id)
    return render(request, "loan_detail.html", {"loan": loan})


def service_purchase_detail(request, purchase_id):
    service_purchase = get_object_or_404(Customerservicepurchase, pk=purchase_id)
    return render(
        request, "service_purchase_detail.html", {"service_purchase": service_purchase}
    )
