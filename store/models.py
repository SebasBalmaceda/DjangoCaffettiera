# Create your models here.
from django.db import models

# Create your models here.
# Create your models here.
class Store(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    dia = models.CharField(max_length=200)
    horario =models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    localidad = models.CharField(max_length=200)
    despedida = models.CharField(max_length=200)
    tel = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    update = models.DateTimeField(auto_now=True, verbose_name="Fecha de Actualizacion")

class Meta:
    verbose_name = "Store"
    verbose_name_plural = "Stores"
    ordering =['-created']
    
    def __str__(self):
        return self.title
