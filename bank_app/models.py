# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.core.exceptions import ValidationError


class Account(models.Model):
    account_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey("Customer", models.DO_NOTHING, blank=True, null=True)
    account_number = models.CharField(unique=True, max_length=20, blank=True, null=True)
    ifsc_code = models.CharField(max_length=15, blank=True, null=True)
    balance = models.DecimalField(
        max_digits=15, decimal_places=2, blank=True, null=True
    )

    def __str__(self):
        if self.customer:
            return f"Account for {self.customer.name}"
        else:
            return f"Account {self.account_id}"

    class Meta:
        managed = False
        db_table = "account"


class Card(models.Model):
    card_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey("Customer", models.DO_NOTHING, blank=True, null=True)
    card_type = models.CharField(max_length=20, blank=True, null=True)
    card_number = models.CharField(unique=True, max_length=16, blank=True, null=True)
    expiry_date = models.DateField(blank=True, null=True)
    cvv = models.CharField(max_length=3, blank=True, null=True)

    def clean(self):

        if self.card_type == "Visa" and not self.card_number.startswith("44465920"):
            raise ValidationError("Visa card number must start with '44465920'.")

    def save(self, *args, **kwargs):

        if self.card_number.startswith("44465920"):
            self.card_type = "Visa"
        else:
            self.card_type = "Elcart"

        super().save(*args, **kwargs)

    def __str__(self):
        if self.customer:
            if self.card_type == "Visa":
                return f"Visa for {self.customer.name}"
            else:
                return f"Elcard for {self.customer.name}"
        else:
            return f"Card id is {self.card_id}"

    class Meta:
        managed = False
        db_table = "card"


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    account_type = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(unique=True, max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = "customer"


class Customerservicepurchase(models.Model):
    purchase_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, models.DO_NOTHING, blank=True, null=True)
    service_type = models.CharField(max_length=50, blank=True, null=True)
    service_id = models.IntegerField(blank=True, null=True)
    purchase_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "customerservicepurchase"


class Insurance(models.Model):
    insurance_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, models.DO_NOTHING, blank=True, null=True)
    insurance_type = models.CharField(max_length=50, blank=True, null=True)
    premium = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    coverage_amount = models.DecimalField(
        max_digits=15, decimal_places=2, blank=True, null=True
    )
    status = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "insurance"


class Loan(models.Model):
    loan_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, models.DO_NOTHING, blank=True, null=True)
    loan_type = models.CharField(max_length=50, blank=True, null=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    interest_rate = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True
    )
    status = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        if self.customer:
            return f"Loan for {self.customer.name}"
        else:
            return f"Loan_id {self.loan_id}"

    class Meta:
        managed = False
        db_table = "loan"


class Transaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    account = models.ForeignKey(Account, models.DO_NOTHING, blank=True, null=True)
    transaction_mode = models.CharField(max_length=20, blank=True, null=True)
    party_involved = models.CharField(max_length=100, blank=True, null=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    transaction_status = models.CharField(max_length=20, blank=True, null=True)
    transaction_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        if self.account:
            return f" Transactions history for {self.account} "
        else:
            return f" Transactiond id {self.transaction_id}"

    class Meta:
        managed = False
        db_table = "transaction"
