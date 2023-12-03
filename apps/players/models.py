from django.db import models
from characters.models import Character
# Create your models here.

class Player(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    character = models.OneToOneField(Character)