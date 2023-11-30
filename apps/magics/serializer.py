from .models import Magic
from rest_framework import serializers

class MagicSerializer (serializers.ModelSerializer):
    class Meta:
        model = Magic
        fields = '__all__'