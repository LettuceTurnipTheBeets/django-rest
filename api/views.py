from api.models import Animal
from api.serializers import AnimalListSerializer, AnimalDetailSerializer
from api.pagination import CustomDetailPagination, CustomListPagination
from rest_framework import generics


class AnimalList(generics.ListAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalListSerializer
    pagination_class = CustomListPagination

class AnimalDetail(generics.RetrieveAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalDetailSerializer
    pagination_class = CustomDetailPagination

class AnimalCreate(generics.CreateAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalDetailSerializer

class AnimalDelete(generics.DestroyAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalDetailSerializer
