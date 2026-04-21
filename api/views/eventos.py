from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import *
from ..serializers import *


@api_view(["GET"])
def getEventos(request):
    eventos = Evento.objects.filter(estado=1)
    serializer = EventoSerializer(eventos, many=True)
    return Response(serializer.data)

@api_view(["POST"])
def postEventos(request):
    serializer = EventoSerializer(data=request.data)

    if serializer.is_valid():
        evento = serializer.save()  

        imagenes = request.FILES.getlist('imagenes')

        for img in imagenes:
            Imagenes.objects.create(
                url=img,
                nombre=img.name,
                idevento=evento
            )

        return Response({
            "evento": serializer.data,
            "imagenes_guardadas": len(imagenes)
        }, status=201)

    return Response(serializer.errors, status=400)