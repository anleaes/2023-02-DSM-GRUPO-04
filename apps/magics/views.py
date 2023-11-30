from .models import Magic
from rest_framework import viewsets
from .serializer import MagicSerializer
# Create your views here.


class MagicViewSet (viewsets.ModelViewSet):
    queryset = Magic.objects.all()
    serializer_class = MagicSerializer