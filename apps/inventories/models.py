from django.db import models
from characters.models import Character
# Create your models here.

class Inventory(models.Model):
    size = models.IntegerField(default=10)
    money = models.FloatField()
    owner = models.OneToOneField(Character)

    def __str__(self):
        return f"{self.owner}'s inventory"
    
    class Meta:
        verbose_name_plural = 'Inventories'
        ordering = ['owner']