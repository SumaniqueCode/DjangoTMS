from rest_framework import viewsets
from .models import House
from . serializers import HouseSerializer

class HouseViewSets(viewsets.ModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer