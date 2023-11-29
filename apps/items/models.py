from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    category = models.ForeignKey(max_length=50)
    rarity = models.ForeignKey(max_length=50)
    value = models.FloatField()
    weight = models.FloatField()
