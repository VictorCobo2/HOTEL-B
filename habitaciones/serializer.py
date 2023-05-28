from rest_framework import serializers
from .models import Habitaciones

class HabitacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habitaciones
        # fields = ('id','fecha', 'estancia', 'metodo_pago', 'direccion_factura', 'habitacion')
        fields = '__all__'