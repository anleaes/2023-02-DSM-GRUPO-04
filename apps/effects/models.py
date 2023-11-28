from django.db import models

# Create your models here.

class Effect(models.Model):
    TIPOS = [
        ('H', 'healing'), ('D', 'damage')
    ]
    name = models.CharField(max_length=50)
    description = models.TextField()
    type =  models.CharField(choices= TIPOS, max_length=1)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name_plural = 'Effects'
        ordering = ['name']