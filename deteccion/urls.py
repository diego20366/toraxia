from django.urls import path
from .views import RadiographyView, upload_image_view

urlpatterns = [
    path('process/', RadiographyView.as_view(), name='process_radiography'),  # Endpoint para procesar radiografía
    path('upload/', upload_image_view, name='upload_image'),  # Ruta para el formulario de carga de imágenes
]