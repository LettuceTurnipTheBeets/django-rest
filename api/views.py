from api.models import Animal
from api.serializers import AnimalListSerializer, AnimalDetailSerializer
from api.pagination import CustomDetailPagination, CustomListPagination
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response


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

@api_view(['POST'])
def AnimalDelete(request, pk):
    """ Delete an object with a POST request"""
    try:
        animal = Animal.objects.get(pk=pk)
        print(animal.id)
    except Animal.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    animal.delete()

    return Response(status=status.HTTP_200_OK)
