from django.db import models
from characters.models import Character
# Create your models here.

class Player(models.Model):
    first_name = models.CharField("Primeiro nome", max_length=50)
    last_name = models.CharField("Último nome", max_length=100)
    email = models.EmailField("E-mail")
    character = models.OneToOneField(Character, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name_plural = 'Players'
        ordering = ['first_name']