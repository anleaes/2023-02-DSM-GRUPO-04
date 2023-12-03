from django.shortcuts import render
from rest_framework import viewsets
from .models import Character
from .serializer import CharacterSerializer
# Create your views here.

class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer