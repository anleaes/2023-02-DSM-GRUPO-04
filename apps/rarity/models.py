from django.db import models

# Create your models here.

class Rarity(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    base_multiplier = models.DecimalField(max_digits=5, decimal_places=2, default=1.00)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Rarities'
        ordering = ['name']
