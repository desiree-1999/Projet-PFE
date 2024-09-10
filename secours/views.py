from django.shortcuts import render
from .models import Capteur, Incendie, Zone
from .serializers import CapteursSerializer, IncendieSerializer, ZoneSerializer
from rest_framework import viewsets


class CapteurViewSet (viewsets.ModelViewSet):
    queryset = Capteur.objects.all()
    serializer_class = CapteursSerializer



class IncendieViewSet (viewsets.ModelViewSet):
    queryset = Incendie.objects.all()
    serializer_class = IncendieSerializer
    # permission_classes = [IsAuthenticated , is_admin]


class ZoneViewSet (viewsets.ModelViewSet):
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer