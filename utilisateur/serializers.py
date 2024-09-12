from rest_framework import serializers
from .models import Person

class PersonSerializer (serializers.ModelSerializer):
    class Meta :
        model = Person
        fields = ['nom', 'prenom', 'email', 'password', 'username']
        # extra_kwargs = {'password': {'write_only': True}}


def create(self, validated_data):
        user = Person.objects.create_user(
            email=validated_data['email'],
            nom=validated_data['nom'],
            prenom=validated_data['prenom'],
            password=validated_data['password'],
            # role=validated_data.get('role', 'user')
        )
        return user