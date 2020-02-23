from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # full URL of existing User object required as field
    street = models.CharField(max_length=100)
    street_2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    zipcode = models.IntegerField()
    country = models.CharField(max_length=30)

    