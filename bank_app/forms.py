from django import forms

class TransferForm(forms.Form):
    from_account_number = forms.CharField(label='From Account Number')
    to_account_number = forms.CharField(label='To Account Number')
    amount = forms.DecimalField(label='Amount')
    