from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from exactuals.models import User, Address, Payor, Payee, Payor_Payee, Bank, Transaction
from exactuals.serializers import UserSerializer, AddressSerializer, PayorSerializer, PayeeSerializer, PayorPayeeSerializer, BankSerializer, TransactionSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=True)
    def get_by_name(self, request, pk):
        users = User.objects.filter(first_name=pk) | User.objects.filter(last_name=pk)
        user_json = UserSerializer(users, many=True)
        return Response(user_json.data)


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class PayorViewSet(viewsets.ModelViewSet):
    lookup_field = 'uid'
    queryset = Payor.objects.all()
    serializer_class = PayorSerializer

class PayeeViewSet(viewsets.ModelViewSet):
    lookup_field = 'uid'
    queryset = Payee.objects.all()
    serializer_class = PayeeSerializer
    
class PayorPayeeViewSet(viewsets.ModelViewSet):
    queryset = Payor_Payee.objects.all()
    serializer_class = PayorPayeeSerializer

    @action(detail=True)
    def payor(self, request, pk):
        payor_payee = Payor_Payee.objects.filter(payor_id=pk)
        payor_payee_json = PayorPayeeSerializer(payor_payee, many=True)
        return Response(payor_payee_json.data)
    
    @action(detail=True)
    def payee(self, request, pk):
        payor_payee = Payor_Payee.objects.filter(payee_id=pk)
        payor_payee_json = PayorPayeeSerializer(payor_payee, many=True)
        return Response(payor_payee_json.data)


class BankViewSet(viewsets.ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.order_by('-date').all()
    serializer_class = TransactionSerializer

    @action(detail=True)
    def get_by_ppid(self, request, pk):
        transactions = Transaction.objects.filter(ppid=pk)
        transactions_json = TransactionSerializer(transactions, many=True)
        return Response(transactions_json.data)
    
    @action(detail=True)
    def get_by_payor_id(self, request, pk):
        ppids = Payor_Payee.objects.filter(payor_id=pk).values_list('ppid')
        transactions = Transaction.objects.filter(ppid__in=ppids)
        transactions_json = TransactionSerializer(transactions, many=True)
        return Response(transactions_json.data)

    @action(detail=True)
    def get_by_payee_id(self, request, pk):
        ppids = Payor_Payee.objects.filter(payee_id=pk).values_list('ppid')
        transactions = Transaction.objects.filter(ppid__in=ppids)
        transactions_json = TransactionSerializer(transactions, many=True)
        return Response(transactions_json.data)

