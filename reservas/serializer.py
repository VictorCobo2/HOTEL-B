from rest_framework import serializers
from .models import Reservas

class ReservasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservas
        # fields = ('id','fecha', 'estancia', 'metodo_pago', 'direccion_factura', 'habitacion')
        fields = '__all__'