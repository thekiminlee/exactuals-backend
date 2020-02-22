from django.shortcuts import render
from rest_framework import viewsets
from exactuals.models import User
from exactuals.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
