from django.shortcuts import render
from rest_framework import viewsets
from exactuals.models import User, Address
from exactuals.serializers import UserSerializer, AddressSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer