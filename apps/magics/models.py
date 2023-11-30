from django.db import models

# Create your models here.

class Magic(models.Model):
    
    name = models.CharField(max_length=50)
    description = models.TextField()
    power = models.PositiveIntegerField()
    mana_cost = models.PositiveIntegerField() 
    duration = models.PositiveIntegerField() 

   