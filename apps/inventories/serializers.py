from rest_framework import serializers
from .models import Inventory

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        queryset = Inventory.objects.all()
        fields = "__all__" 