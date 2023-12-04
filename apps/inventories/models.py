from django.db import models
from characters.models import Character
from items.models import Item
# Create your models here.

class Inventory(models.Model):
    size = models.IntegerField("Tamanho", default=10)
    money = models.FloatField("Dinheiro")
    owner = models.OneToOneField(Character, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.owner}'s inventory"
    
    class Meta:
        verbose_name_plural = 'Inventories'
        ordering = ['owner']


class InventorySlot(models.Model):
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING)
    inventory = models.ForeignKey(Inventory, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField("Quantidade", default=1)

    def __str__(self):
        return f"{self.inventory} - {self.item} - {self.quantity}"