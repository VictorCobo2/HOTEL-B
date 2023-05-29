from rest_framework import viewsets
from .serializer import HabitacionesSerializer
from .models import Habitaciones
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
# Create your views here.

class HabitacionesView(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = HabitacionesSerializer
    queryset = Habitaciones.objects.all()