from django.db import models
from rarities.models import Rarity
from itemcategories.models import ItemCategory

# Create your models here.

class Item(models.Model):
    name = models.CharField("Nome", max_length=50)
    description = models.TextField("Descrição")
    category = models.ForeignKey(ItemCategory, on_delete=models.SET_NULL, null=True)
    rarity = models.ForeignKey(Rarity, on_delete=models.SET_NULL, null=True)
    value = models.FloatField("Valor")
    weight = models.FloatField("Peso")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Items'
        ordering = ['name']
