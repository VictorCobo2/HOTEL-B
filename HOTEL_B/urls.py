from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reservas/', include('reservas.urls')),
    path('habitaciones/', include('habitaciones.urls')),
    path('user/', include('user.urls')),
    path('docs/', include_docs_urls(title="HOTEL API"))
    
]
