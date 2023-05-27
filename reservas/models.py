from django.db import models

# Create your models here.

class Reservas(models.Model):
    fecha = models.DateField()
    estancia = models.IntegerField()
    metodo_pago = models.CharField(max_length=50)
    direccion_factura = models.CharField(max_length=120)
    habitacion = models.IntegerField()

    def __str__(self):
        return self.fecha
