from django.db import models

# Create your models here.

class Rarity(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    base_multiplier = models.DecimalField(max_digits=5, decimal_places=2, default=1.00)

    