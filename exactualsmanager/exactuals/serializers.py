from exactuals.models import User, Address, Payor, Payee, Payor_Payee, Bank, Transaction
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class PayorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payor
        fields = '__all__'

class PayeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payee
        fields = '__all__'

class PayorPayeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payor_Payee
        fields = '__all__'

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

