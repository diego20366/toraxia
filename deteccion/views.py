from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from .models import process_radiography_image  # Función para procesar la radiografía
from rest_framework.exceptions import APIException
from django.http import HttpResponse
from django.shortcuts import render

def upload_image_view(request):
    return render(request, 'upload_image.html')

def home(request):
    return HttpResponse("Bienvenido a la API de Detección de Anomalias de Torax")

class RadiographyView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        try:
            file = request.FILES.get('file')
            if not file:
                return Response({'error': 'No hay archivo'}, status=status.HTTP_400_BAD_REQUEST)
            
            # Procesar la imagen
            result = process_radiography_image(file)
            
            return Response({'result': result}, status=status.HTTP_200_OK)
        except APIException as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
