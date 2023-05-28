from django.urls import include, path
from rest_framework import routers
from habitaciones import views

router = routers.DefaultRouter()
router.register(r'habitaciones', views.HabitacionesView, 'habitaciones')

urlpatterns = [
    path('api/', include(router.urls)),
]