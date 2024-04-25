from django.shortcuts import render
from .models import Person
from .serializers import PersonSerializer, Userserializer
from rest_framework import generics
from rest_framework.filters import SearchFilter

from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, AllowAny

class PersonListCreate(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class PersonRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    
    
#usser creation view 
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = Userserializer
    permission_classes = [AllowAny]

