from django.shortcuts import render
from rest_framework import viewsets
from exactuals.models import User, Address, Payor, Payee, Payor_Payee, Bank, Transaction
from exactuals.serializers import UserSerializer, AddressSerializer, PayorSerializer, PayeeSerializer, PayorPayeeSerializer, BankSerializer, TransactionSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class PayorViewSet(viewsets.ModelViewSet):
    queryset = Payor.objects.all()
    serializer_class = PayorSerializer

class PayeeViewSet(viewsets.ModelViewSet):
    queryset = Payee.objects.all()
    serializer_class = PayeeSerializer
    
class PayorPayeeViewSet(viewsets.ModelViewSet):
    queryset = Payor_Payee.objects.all()
    serializer_class = PayorPayeeSerializer

class BankViewSet(viewsets.ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.order_by('-date').all()
    serializer_class = TransactionSerializer
