from rest_framework import viewsets
from .serializer import HabitacionesSerializer
from .models import Habitaciones
# Create your views here.

class HabitacionesView(viewsets.ModelViewSet):
    serializer_class = HabitacionesSerializer
    queryset = Habitaciones.objects.all()