from rest_framework import serializers
from api.models import Animal


class AnimalSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    commonName = serializers.CharField(max_length=20)
    scientificName = serializers.CharField(max_length=50)
    family = serializers.CharField(max_length=20)
    imageURL = serializers.URLField(max_length=200)

    def create(self, validated_data):
        """Create and return a new Animal instance"""
        return Animal.objects.create(**validate_data)

    def update(self, instance, validated_data):
        """Update and return an existing Animal instance"""
        instance.commonName = validated_data.get('commonName', instance.commonName)
        instance.scientificName = validated_data.get('scientificName', instance.scientificName)
        instance.family = validated_data.get('family', instance.family)
        instance.imageURL = validated_data.get('imageURL', instance.imageURL)
