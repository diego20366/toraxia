from django.contrib import admin
from .models import Imagen, Anomalia, Paciente, Profesional

admin.site.register(Imagen)
admin.site.register(Anomalia)
admin.site.register(Paciente)
admin.site.register(Profesional)