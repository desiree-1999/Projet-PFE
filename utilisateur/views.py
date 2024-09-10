from django.shortcuts import render
from .models import Person
from .serializers import PersonSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .permissions import is_admin


class PersonViewSet (viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    # permission_classes = [IsAuthenticated , is_admin]

    def create(self, request, *args, **kwargs):
        if request.user.role !=  "admin" :
            return Response ({'error':" vous n'avez pas la permission pour créer un utilisateur" },  status = status.HTTP_403_FORBIDDEN)
        return super().create(request, *args, **kwargs)
    

    def destroy(self, request, *args, **kwargs):
        if request.user.role != 'admin' :
            return Response ({'error' : "vous n'avez pas la permission pour détruire un utilisateur " }, status = status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)