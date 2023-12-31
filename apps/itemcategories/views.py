from .models import ItemCategory
from rest_framework import viewsets
from .serializers import ItemCategorySerializer

# Create your views here.

class ItemCategoryViewSet (viewsets.ModelViewSet):
    queryset = ItemCategory.objects.all()
    serializer_class = ItemCategorySerializer