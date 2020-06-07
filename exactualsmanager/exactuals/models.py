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

class Processors(models.IntegerChoices):
    A = 1
    B = 2
    C = 3


class User(models.Model):
    uid = models.CharField(max_length=20, unique=True, primary_key=True)
    password = models.CharField(max_length=30)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Type(models.TextChoices):
        PYR = "Payor"
        PYE = "Payee"
    user_type = models.CharField(max_length=10, choices=Type.choices)

class Address(models.Model):
    uid = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    street = models.CharField(max_length=100)
    street_2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    zipcode = models.IntegerField()
    country = models.CharField(max_length=30)

class Payor(models.Model):
    uid = models.OneToOneField(User, to_field='uid', primary_key=True, on_delete=models.CASCADE)
    send_payment_method = models.CharField(max_length=20)

class Payee(models.Model):
    uid = models.OneToOneField(User, to_field='uid', primary_key=True, on_delete=models.CASCADE)
    preference = models.CharField(max_length=100)
    receive_payment_method = models.CharField(max_length=20)

class Payor_Payee(models.Model):
    ppid = models.CharField(max_length=20, primary_key=True, unique=True)
    payor_id = models.ForeignKey(Payor, on_delete=models.CASCADE)
    payee_id = models.ForeignKey(Payee, on_delete=models.CASCADE)
    satisfaction = models.IntegerField(default=0)
    feedback_count = models.IntegerField(default=0)

class Bank(models.Model):
    uid = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    bank_name = models.CharField(max_length=50)
    account_num = models.IntegerField()
    rounting_num = models.IntegerField()

class Transaction(models.Model):
    tid = models.CharField(max_length=20, primary_key=True, unique=True) # transaction id
    ppid = models.ForeignKey(Payor_Payee, on_delete=models.SET("Payor_payee removed"))
    description = models.TextField(blank=True) # optioal field
    memo = models.TextField(blank=True) # optional field
    bid = models.CharField(max_length=20, blank=True) # batch id
    date = models.DateTimeField(verbose_name="Transaction Date")
    disbursement = models.CharField(max_length=20)
    amount = models.DecimalField(decimal_places=2, max_digits=14)
    trans_type = models.CharField(max_length=20)
    timezone = models.CharField(max_length=10)
    status = models.CharField(max_length=20)
    status_date = models.DateTimeField(auto_now=True, verbose_name="Transaction Status Date")
    satisfaction = models.IntegerField(null=True)
    processor = models.IntegerField(choices=Processors.choices)

class UserData(models.Model):
    # Transaction information
    payor_id = models.ForeignKey(Payor, on_delete=models.DO_NOTHING)
    pyr_id = models.IntegerField(blank=True)
    payee_id = models.ForeignKey(Payee, on_delete=models.DO_NOTHING)
    pye_id = models.IntegerField(blank=True)
    payor_payee_id = models.ForeignKey(Payor_Payee, on_delete=models.DO_NOTHING)
    ppid = models.IntegerField(blank=True)
    bank_name = models.CharField(max_length=50, blank=True)
    amount = models.DecimalField(decimal_places=2, max_digits=14)
    transaction_status = models.BooleanField(null=True) # T: Delivered, F: Returned
    transaction_profit = models.DecimalField(decimal_places=2, max_digits=14)
    transaction_start_date = models.DateTimeField(auto_now=True)
    transaction_end_date = models.DateTimeField(null=True)
    # transaction_revenue = models.BooleanField()
    processor = models.IntegerField(choices=Processors.choices)
    class Countries(models.IntegerChoices):
        # maps UN A3 country abbr to UN NUM country abbr
        KOR = 410
        CHN = 156
        USA = 840
        FRA = 250
        BRA = 76
        DEU = 276
        MEX = 484
        IND = 356
    country = models.IntegerField(choices=Countries.choices)

    # Currency information
    class Currency(models.IntegerChoices):
        # maps ISO currency abbr to NUM abbr
        KRW = 410
        CNY = 156
        USD = 840
        EUR = 978 # FRA & DEU
        BRL = 986
        MXN = 484
        INR = 356
    original_currency = models.IntegerField(choices=Currency.choices)
    target_currency = models.IntegerField(choices=Currency.choices)
    fx = models.BooleanField()

    # Satisfaction
    payee_satisfaction = models.BooleanField(null=True)
    payor_satisfaction = models.BooleanField(null=True)
    overall_satisfaction = models.BooleanField(null=True)
    

