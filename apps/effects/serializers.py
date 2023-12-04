from .models import Effect
from rest_framework import serializers

class EffectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Effect
        fields = '__all__'