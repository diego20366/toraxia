from rest_framework import serializers
from .models import Imagen, Anomalia, Paciente, Profesional

class ImagenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagen
        fields = '__all__'

class AnomaliaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anomalia
        fields = '__all__'

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'

class ProfesionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesional
        fields = '__all__'