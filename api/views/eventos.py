from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from api.models import Evento, Imagenes
from api.serializers import EventoSerializer

@api_view(["GET"])
def getEventos(request):
    # Filtramos solo eventos activos para el mapa y la lista
    eventos = Evento.objects.filter(estado=1)
    serializer = EventoSerializer(eventos, many=True)
    return Response(serializer.data)

@api_view(["POST"])
def postEventos(request):
    # 1. Copiamos los datos para poder modificarlos
    data = request.data.copy()
    
    # 2. Forzamos valores por defecto si no vienen del front
    data['estado'] = 1 
    if 'idproveedor' not in data:
        data['idproveedor'] = 1 # Valor por defecto para evitar errores de integridad

    # 3. Pasamos la COPIA (data) al serializador, no request.data
    serializer = EventoSerializer(data=data)

    if serializer.is_valid():
        evento = serializer.save()  

        # 4. Manejo de múltiples imágenes
        imagenes = request.FILES.getlist('imagenes')
        for img in imagenes:
            Imagenes.objects.create(
                url=img,
                nombre=img.name,
                idevento=evento
            )

        return Response({
            "id": evento.idevento,
            "evento": serializer.data,
            "imagenes_guardadas": len(imagenes)
        }, status=status.HTTP_201_CREATED)

    # Si hay error, devolvemos los detalles para debugear en React
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def deleteEventos(request):
    id_ev = request.data.get("idevento")
    try:
        evento = Evento.objects.get(idevento=id_ev)
        # Borrado lógico: cambiamos estado a 0 en lugar de eliminar la fila
        evento.estado = 0
        evento.save()
        return Response({"message": "Evento desactivado correctamente."}, status=200)
    except Evento.DoesNotExist:
        return Response({"error": "Evento no encontrado."}, status=404)
    
@api_view(["POST"])
def validar(request):
    nombre = request.data.get("nombre")
    descripcion = request.data.get("descripcion")

    try:
        evento = Evento.objects.get(nombre=nombre, descripcion=descripcion)
        serializer = EventoSerializer(evento)
        return Response(serializer.data, status=200)

    except Evento.DoesNotExist:
        return Response({"error": "Evento no encontrado."}, status=404)
    except Evento.MultipleObjectsReturned:
        return Response({"error": "Existen duplicados con estos datos."}, status=400)