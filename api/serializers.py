from rest_framework import serializers
from api.models import Animal


class AnimalListSerializer(serializers.ModelSerializer):
    """Serialize the Animal object, show three variables, and return ID as a string"""
    id = serializers.SerializerMethodField()
    
    def get_id(self, obj):
        return str(obj.id)

    class Meta:
        model = Animal
        fields = ('id', 'commonName', 'imageURL')

class AnimalDetailSerializer(serializers.ModelSerializer):
    """Serialize the Animal object, show all variables, and return ID as a string"""
    id = serializers.SerializerMethodField()

    def get_id(self, obj):
        return str(obj.id)

    class Meta:
        model = Animal
        fields = '__all__'
