from rest_framework import serializers
from .models import Inventory, InventorySlot

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = "__all__"

class InventorySlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventorySlot
        fields = "__all__"