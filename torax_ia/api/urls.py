from django.urls import path, include
from .views import ImagenListCreateView, ImagenDetailView, AnomaliaListCreateView, AnomaliaDetailView, PacienteListCreateView, PacienteDetailView, ProfesionalListCreateView, ProfesionalDetailView

urlpatterns = [
    # Rutas para imágenes
    path('imagenes/', ImagenListCreateView.as_view(), name='imagen-list-create'),
    path('imagenes/<int:pk>/', ImagenDetailView.as_view(), name='imagen-detail'),

    # Rutas para anomalías
    path('anomalias/', AnomaliaListCreateView.as_view(), name='anomalia-list-create'),
    path('anomalias/<int:pk>/', AnomaliaDetailView.as_view(), name='anomalia-detail'),

    # Rutas para pacientes
    path('pacientes/', PacienteListCreateView.as_view(), name='paciente-list-create'),
    path('pacientes/<int:pk>/', PacienteDetailView.as_view(), name='paciente-detail'),

    # Rutas para profesionales
    path('profesionales/', ProfesionalListCreateView.as_view(), name='profesional-list-create'),
    path('profesionales/<int:pk>/', ProfesionalDetailView.as_view(), name='profesional-detail'),
]