from django.db import models
from effects.models import Effect
# Create your models here.

class Magic(models.Model):
    
    name = models.CharField(max_length=50)
    description = models.TextField()
    power = models.PositiveIntegerField()
    mana_cost = models.PositiveIntegerField() 
    duration = models.PositiveIntegerField() 
    effects = models.ManyToManyField(Effect, blank=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name_plural = 'Effects'
        ordering = ['name']