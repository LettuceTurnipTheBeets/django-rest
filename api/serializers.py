from rest_framework import serializers
from api.models import Animal


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ('id', 'commonName', 'scientificName', 'family', 'imageURL')
