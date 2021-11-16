from abc import abstractmethod
from django.db import models

from django.contrib.auth.models import User

class ClaseModelo(models.Model):
    estado = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    modified_date = models.DateTimeField(auto_now=True)
    modified_by = models.IntegerField(blank=True, null=True)
    
    class Meta:
        abstract =True

class Idioma(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Idiomas"

    def __str__(self):
        return self.nombre
# Create your models here.
