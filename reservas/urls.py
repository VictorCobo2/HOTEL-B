from django.urls import include, path
from rest_framework import routers
from reservas import views

router = routers.DefaultRouter()
router.register(r'reservas', views.ReservasView, 'reservas')

urlpatterns = [
    path('api/', include(router.urls)),
]