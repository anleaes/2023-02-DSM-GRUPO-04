from django.db import models

# Create your models here.

class Effect(models.Model):
    TIPOS = [
        ('H', 'healing'), ('D', 'damage')
    ]
    name = models.CharField("Nome", max_length=50)
    description = models.TextField("Descrição")
    type =  models.CharField("Tipo", choices= TIPOS, max_length=1)
    duration = models.IntegerField("Duração")
    base_power = models.IntegerField("Poder base")

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name_plural = 'Effects'
        ordering = ['name']