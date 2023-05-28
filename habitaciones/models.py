from django.db import models

# Create your models here.

class Habitaciones(models.Model):
    imagen = models.CharField( max_length=150)
    tipo =  models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=20, decimal_places=10)
    capacidad = models.IntegerField()
    caracteristicas = models.TextField(max_length=500)
    numero = models.IntegerField()
    disponibilidad = models.BooleanField(default=True)

    def __str__(self):
        return self.numero
