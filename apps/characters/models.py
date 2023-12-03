from django.db import models

from magics.models import Magic

# Create your models here.

class Character(models.Model):
    name = models.CharField(max_length=100)
    level = models.IntegerField()
    magics = models.ManyToManyField(Magic)

    def __str__(self):
        return f"{self.name} - {self.level}"
    
    class Meta:
        verbose_name_plural = 'Characters'
        ordering = ['name']
