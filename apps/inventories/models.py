from django.db import models
from characters.models import Character
from items.models import Item
# Create your models here.

class Inventory(models.Model):
    size = models.IntegerField("Tamanho", default=10)
    money = models.FloatField("Dinheiro")
    owner = models.OneToOneField(Character)

    def __str__(self):
        return f"{self.owner}'s inventory"
    
    class Meta:
        verbose_name_plural = 'Inventories'
        ordering = ['owner']


class InventorySlot(models.Model):
    item = models.ForeignKey(Item)
    inventory = models.ForeignKey(Inventory)
    quantity = models.IntegerField("Quantidade", default=1)

    def __str__(self):
        return f"{self.inventory} - {self.item} - {self.quantity}"