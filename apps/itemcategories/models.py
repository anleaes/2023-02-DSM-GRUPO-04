from django.db import models


# Create your models here.

class ItemCategory(models.Model):
    name = models.CharField("Nome", max_length=50)
    description = models.TextField("Descrição")
    max_stack = models.PositiveIntegerField("Número Máximo")

    def __str__(self):
        return self.name   
    
    class Meta:
        verbose_name_plural = 'Item Categories'
        ordering = ['name']