from rest_framework import serializers
from .models import Capteur, Incendie, Zone

class CapteursSerializer (serializers.ModelSerializer):
    class Meta :
        model = Capteur
        fields = ['type', 'localisation', 'etat']


class IncendieSerializer (serializers.ModelSerializer):
    class Meta : 
        model = Incendie
        fields = ['gravite','dateDebut' ,'description']


class ZoneSerializer (serializers.ModelSerializer):
    class Meta : 
        model = Zone
        fields = ['nom', 'description', 'localisation']