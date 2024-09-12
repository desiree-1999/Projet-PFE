from django.shortcuts import render
from .models import Person
from .serializers import PersonSerializer
from rest_framework import viewsets, status, serializers
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .permissions import is_admin



class PersonViewSet (viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
     # permission_classes = [IsAuthenticated , is_admin]