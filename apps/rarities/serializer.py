from .models import Rarity 
from rest_framework import serializers

class RaritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Rarity
        fields = '__all__'