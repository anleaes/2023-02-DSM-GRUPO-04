from .models import Effect
from rest_framework import viewsets
from .serializers import EffectSerializer
# Create your views here.


class EffectViewSet (viewsets.ModelViewSet):
    queryset = Effect.objects.all()
    serializer_class = EffectSerializer