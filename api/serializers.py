from rest_framework import serializers
from api.models import Animal


class AnimalThreeSerializer(serializers.ModelSerializer):
    """Serialize the Animal object and show only three variables"""
    class Meta:
        model = Animal
        fields = ('id', 'commonName', 'imageURL')


class AnimalAllSerializer(serializers.ModelSerializer):
    """Serialize the Animal object and show all variables"""
    class Meta:
        model = Animal
        fields = '__all__'
