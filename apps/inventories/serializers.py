from rest_framework import serializers
from .models import Inventory, InventorySlot

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        queryset = Inventory.objects.all()
        fields = "__all__"

class InventorySlotSerializer(serializers.ModelSerializer):
    class Meta:
        queryset = InventorySlot.objects.all()
        fields = "__all__"