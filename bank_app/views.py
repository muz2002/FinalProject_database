from django.shortcuts import render,redirect

# Create your views here.
# views.py
from django.shortcuts import render, get_object_or_404
from .models import Customer, Account, Card, Transaction, Loan, Customerservicepurchase
from django.db import transaction
from . forms import TransferForm 
from datetime import datetime


def home(request):
    return render(request, "home.html")

def transaction_success(request):
    return render(request, 'transaction_success.html')

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
    transactions = Transaction.objects.filter(account=account).order_by('-transaction_date')
    return render(
        request,
        "account_detail.html",
        {"account": account, "transactions": transactions},
    )




def card_detail(request):
    customer_id = request.user.account.customer_id
    cards = Card.objects.filter(customer_id=customer_id)
    customer_name = [card.customer.name if card.customer else "Unknown" for card in cards]
    return render(request, "card_detail.html", {"cards": cards, "customer_name": customer_name})

def transaction_detail(request):
    account_id = request.user.account.customer_id
    transactions = Transaction.objects.filter(account_id=account_id).order_by('-transaction_date')
    return render(request, "transaction_detail.html", {"transaction": transactions})


def loan_detail(request, loan_id):
    loan = get_object_or_404(Loan, pk=loan_id)
    return render(request, "loan_detail.html", {"loan": loan})


def service_purchase_detail(request, purchase_id):
    service_purchase = get_object_or_404(Customerservicepurchase, pk=purchase_id)
    return render(
        request, "service_purchase_detail.html", {"service_purchase": service_purchase}
    )
def transfer_funds(request):
    if request.method == 'POST':
        form = TransferForm(request.POST)
        if form.is_valid():
            from_account_number = form.cleaned_data['from_account_number']
            to_account_number = form.cleaned_data['to_account_number']
            amount = form.cleaned_data['amount']
            
            try:
                with transaction.atomic():
                    from_account = Account.objects.get(account_number=from_account_number)
                    to_account = Account.objects.get(account_number=to_account_number)
                    
                    if from_account.balance < amount:
                        raise ValueError("Insufficient funds")
                
                    from_account.balance -= amount
                    to_account.balance += amount
                    from_account.save()
                    to_account.save()
                    
                    Transaction.objects.create(
                        account=from_account,
                        transaction_mode='Transfer',
                        party_involved=to_account.customer.name,
                        amount=amount,
                        transaction_status='Completed',
                        transaction_date = datetime.now()
                        
                    )
                    
                    return redirect('transaction_success')  # Redirect to a success page
            except Account.DoesNotExist:
                return render(request, 'error.html', {'message': 'Account not found'})
            except ValueError as e:
                return render(request, 'error.html', {'message': str(e)})
            except Exception as e:
                return render(request, 'error.html', {'message': 'An error occurred'})
    else:
        form = TransferForm()
    
    return render(request, 'transfer.html', {'form': form})
