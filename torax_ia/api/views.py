from rest_framework import generics
from .models import Imagen, Anomalia, Paciente, Profesional
from .serializers import ImagenSerializer, AnomaliaSerializer, PacienteSerializer, ProfesionalSerializer
from django.http import HttpResponse

def inicio(request):
    return HttpResponse("Bienvenido a la API de Tórax IA")

# Vista para listar y crear imágenes
class ImagenListCreateView(generics.ListCreateAPIView):
    queryset = Imagen.objects.all()
    serializer_class = ImagenSerializer

# Vista para obtener, actualizar o eliminar una imagen en particular
class ImagenDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Imagen.objects.all()
    serializer_class = ImagenSerializer

class ImagenDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Imagen.objects.all()
    serializer_class = ImagenSerializer


# Vista para listar y crear anomalías
class AnomaliaListCreateView(generics.ListCreateAPIView):
    queryset = Anomalia.objects.all()
    serializer_class = AnomaliaSerializer

# Vista para obtener, actualizar o eliminar una anomalía en particular
class AnomaliaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Anomalia.objects.all()
    serializer_class = AnomaliaSerializer

class AnomaliaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Anomalia.objects.all()
    serializer_class = AnomaliaSerializer

# Vista para listar y crear pacientes
class PacienteListCreateView(generics.ListCreateAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

# Vista para obtener, actualizar o eliminar un paciente en particular
class PacienteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class PacienteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

# Vista para listar y crear profesionales
class ProfesionalListCreateView(generics.ListCreateAPIView):
    queryset = Profesional.objects.all()
    serializer_class = ProfesionalSerializer

# Vista para obtener, actualizar o eliminar un profesional en particular
class ProfesionalDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profesional.objects.all()
    serializer_class = ProfesionalSerializer

class ProfesionalDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profesional.objects.all()
    serializer_class = ProfesionalSerializer