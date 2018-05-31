from api.models import Animal
from api.serializers import AnimalThreeSerializer, AnimalAllSerializer
from rest_framework import generics


class AnimalList(generics.ListCreateAPIView):
    """Read or write endpoint to represent a collection of Animal instances.
    /List/
    GET:
        list all Animal instances.
    POST:
        create one Animal instance.
    """
    queryset = Animal.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return AnimalThreeSerializer
        if self.request.method == 'POST':
            return AnimalAllSerializer


class AnimalDetail(generics.RetrieveDestroyAPIView):
    """Read or delete endpoint to represent a single Animal instance.
    /ID/$/
    GET:
        list a single Animal instance.
    DELETE:
        delete one Animal instance.
    """
    queryset = Animal.objects.all()
    serializer_class = AnimalAllSerializer
