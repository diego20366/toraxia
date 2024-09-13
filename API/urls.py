from django.contrib import admin
from django.urls import path, include
from deteccion import views  # Importa las vistas de la app deteccion

urlpatterns = [
    path('', views.home, name='home'),  # Ruta para la página de inicio
    path('admin/', admin.site.urls),
    path('api/', include('deteccion.urls')),  # Incluye las rutas de la app deteccion
]