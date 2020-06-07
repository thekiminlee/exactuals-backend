from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from exactuals.models import User, Address, Payor, Payee, Payor_Payee, Bank, Transaction, UserData
from exactuals.serializers import UserSerializer, AddressSerializer, PayorSerializer, PayeeSerializer, PayorPayeeSerializer, BankSerializer, TransactionSerializer, UserDataSerializer

from exactuals.prediction.predict import Prediction
from exactuals.logics import logic
import json

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

    @action(detail=True, methods=['put'])
    def update_satisfaction(self, request, pk):
        ppid = request.data['ppid']
        tid = request.data['tid']

        transaction = Transaction.objects.filter(tid=tid)
        payor_payee = Payor_Payee.objects.filter(ppid=ppid)

        if transaction.exists() and payor_payee.exists():
            transaction = transaction.first()
            payor_payee = payor_payee.first()

        
            transaction.satisfaction = pk
            transaction.save()

            payor_payee.feedback_count += 1
            if pk:
                payor_payee.satisfaction = (payor_payee.satisfaction + 1.00)
            payor_payee.satisfaction /= payor_payee.feedback_count
            payor_payee.save()
        
            return Response({'status': 'update success'})
        return Response(status=status.HTTP_400_BAD_REQUEST)


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

class UserDataViewSet(viewsets.ModelViewSet):
    queryset = UserData.objects.all()
    serializer_class = UserDataSerializer

    def _mutate_data(self, data):
        data._mutable = True
        data['pyr_id'] = 0
        data['pye_id'] = 0
        data['ppid'] = 0
        data._mutable = False

        return data

    def create(self, request, pk=None):
        data = self._mutate_data(request.data)
        serializer = UserDataSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            predict = Prediction(serializer.data)
            prediction = predict.predict()

            result = {
                "A": prediction['A'],
                "B": prediction['B'],
                "C": prediction['C']
            }
            
            return Response(result, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    @action(detail=True)
    def predict_by_payee_rating(self, request, pk):
        data = self._mutate_data(request.data) 
        serializer = UserDataSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            predict = Prediction(serializer.data)
            prediction = None
            predictor = "_satisfaction"

            if pk == 'payee':
                prediction = predict.predict_payee()
                predictor = 'payee' + predictor
            elif pk == 'payor':
                prediction = predict.predict_payor()
                predictor = 'payor' + predictor
            elif pk == 'overall':
                prediction = predict.predict_overall()
                predictor = 'overall' + predictor

            result = {
                predictor: prediction
            }

            return Response(result, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            

        return None


