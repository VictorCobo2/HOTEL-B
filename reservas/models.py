from django.db import models

# Create your models here.

class Reservas(models.Model):
    fecha = models.DateField()
    hora = models.CharField(max_length=5, default='00:00')
    estancia = models.IntegerField()
    metodo_pago = models.CharField(max_length=50)
    direccion_factura = models.CharField(max_length=120)
    habitacion = models.IntegerField()
    primer_nombre = models.CharField(max_length=50, null=False, default='None')
    segundo_nombre = models.CharField(max_length=50, null=False, default='None')
    identificacion = models.CharField(max_length=50, null=False, default='00')
    email = models.Case(max_length=150)
    estado = models.BooleanField(default=True)
    numero_contacto = models.IntegerField(default=123)


    def __str__(self):
        return self.primer_nombre
