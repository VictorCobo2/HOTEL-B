from rest_framework import viewsets
from .serializer import ReservasSerializer
from .models import Reservas
# Create your views here.

class ReservasView(viewsets.ModelViewSet):
    serializer_class = ReservasSerializer
    queryset = Reservas.objects.all()
