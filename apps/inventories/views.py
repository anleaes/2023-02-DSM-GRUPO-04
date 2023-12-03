from django.shortcuts import render
from rest_framework import viewsets
from .models import Inventory, InventorySlot
from .serializers import InventorySerializer, InventorySlotSerializer

# Create your views here.
class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer


class InventorySlotsViewSet(viewsets.ModelViewSet):
    queryset = InventorySlot.objects.all()
    serializer_class = InventorySlotSerializer
