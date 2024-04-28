from django.shortcuts import render,redirect

# Create your views here.
# views.py
from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import Customer, Account, Card, Transaction, Loan, Customerservicepurchase
from django.db import transaction
from decimal import Decimal

from django.contrib import messages

def home(request):
    return render(request, "home.html")


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
@transaction.atomic
def perform_transaction(request):
    # Get the accounts involved in the transaction
    source_account_id = request.POST.get('source_account_id')
    target_account_id = request.POST.get('target_account_id')
    amount = request.POST.get('amount')

    # Fetch source and target accounts from the database
    source_account = get_object_or_404(Account, pk=source_account_id)
    target_account = get_object_or_404(Account, pk=target_account_id)

    try:
        # Perform the transaction operations
        source_account.balance -= Decimal(amount)
        target_account.balance += Decimal(amount)
        source_account.save()
        target_account.save()

        # Create a transaction record
        Transaction.objects.create(
            account=source_account,
            transaction_mode='Transfer',
            party_involved=f'Transfer to Account {target_account_id}',
            amount=Decimal(amount),
            transaction_status='Completed',
        )

        # Optionally, you can do additional operations or handle exceptions here

        return render(request, 'transaction_success.html')
    except Exception as e:
        # Handle exceptions, rollback if needed
        transaction.set_rollback(True)
        return render(request, 'transaction_failed.html')




def process_transaction(request):
    if request.method == 'POST':
        # Process transaction logic here
        amount = request.POST.get('amount')
        # Update account balances, create transaction records, etc.
        messages.success(request, 'Transaction processed successfully!')
        return render(request, 'process_transaction.html')

    return redirect('account_detail')