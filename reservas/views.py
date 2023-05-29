from rest_framework import viewsets
from .serializer import ReservasSerializer
from .models import Reservas
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class ReservasView(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ReservasSerializer
    queryset = Reservas.objects.all()

class ReservasAPIView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = ReservasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)