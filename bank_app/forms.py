from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()

class TransferForm(forms.Form):
    from_account_number = forms.CharField(label='From Account Number')
    to_account_number = forms.CharField(label='To Account Number')
    amount = forms.DecimalField(label='Amount')
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)  # Get and remove 'request' from kwargs
        super().__init__(*args, **kwargs)
        
    def clean(self):
        cleaned_data = super().clean()
        from_account_number = cleaned_data.get("from_account_number")
        to_account_number = cleaned_data.get("to_account_number")
        
        if from_account_number == to_account_number:
            raise ValidationError("Cannot transfer funds to your own account.")
        
        return cleaned_data
    
    def clean_from_account_number(self):
        from_account_number = self.cleaned_data.get("from_account_number")
        
        # Check if the from_account_number belongs to the logged in user
        if User.objects.filter(account=from_account_number, id=self.request.user.id).exists():
            raise ValidationError("Cannot transfer funds from your own account.")
    
        return from_account_number