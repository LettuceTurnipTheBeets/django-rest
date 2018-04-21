from rest_framework import serializers
from api.models import Animal


class AnimalSerializer(serializers.ModelSerializer):
    """Serialize the Animal object and return ID as a string"""
    id = serializers.SerializerMethodField()
    
    def get_id(self, obj):
        return str(obj.id)

    class Meta:
        model = Animal
        fields = ('id', 'commonName', 'imageURL')
