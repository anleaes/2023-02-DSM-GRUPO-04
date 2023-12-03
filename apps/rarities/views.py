from .models import Rarity
from rest_framework import viewsets
from .serializers import RaritySerializer
# Create your views here.

class RarityViewSet(viewsets.ModelViewSet):
    queryset = Rarity.objects.all()
    serializer_class = RaritySerializer

