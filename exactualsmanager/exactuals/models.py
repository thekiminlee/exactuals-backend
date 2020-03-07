from django.db import models

'''
Foreign/OneToOne on_delete options:
    CASCADE = when ref deleted, delete object with ref
    PROTECT = forbid deletion of ref object
    SET_NULL = set the ref to null
    SET_DEFAULT = set the default value
    SET(...) = set a given value
    DO_NOTHING: "
'''

class User(models.Model):
    user_id = models.CharField(max_length=20, unique=True, primary_key=True)
    password = models.CharField(max_length=30)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)

class Address(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    street = models.CharField(max_length=100)
    street_2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    zipcode = models.IntegerField()
    country = models.CharField(max_length=30)

class Payor(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    send_payment_method = models.CharField(max_length=20)

class Payee(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    preference = models.CharField(max_length=100)
    receive_payment_method = models.CharField(max_length=20)

class Payor_Payee(models.Model):
    payor_payee_id = models.CharField(max_length=20, unique=True)
    payor_id = models.OneToOneField(Payor, on_delete=models.CASCADE)
    payee_id = models.OneToOneField(Payee, on_delete=models.CASCADE)

class Bank(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True)
    account_num = models.IntegerField()
    rounting_num = models.IntegerField()

class Transaction(models.Model):
    transaction_id = models.CharField(max_length=20, unique=True)
    payor_payee_id = models.OneToOneField(Payor_Payee, on_delete=models.SET("Payor_payee removed"))
    description = models.TextField(blank=True) # optioal field
    memo = models.TextField(blank=True) # optional field
    batch_id = models.CharField(max_length=20, unique=True, blank=True)
    date = models.DateTimeField(verbose_name="Transaction Date")
    disbursement = models.CharField(max_length=20)
    amount = models.DecimalField(decimal_places=2, max_digits=14)
    trans_type = models.CharField(max_length=20)
    timezone = models.CharField(max_length=10) 
    status = models.CharField(max_length=20)
    status_date = models.DateTimeField(verbose_name="Transaction Status Date") 