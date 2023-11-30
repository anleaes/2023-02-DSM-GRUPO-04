from django.db import models


# Create your models here.

class ItemCategory(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    max_stack = models.PositiveIntegerField()

    def __str__(self):
        return self.name   
    
    class Meta:
        verbose_name_plural = 'Item Categories'
        ordering = ['name']