from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import *
from ..serializers import *


@api_view(["GET"])
def getProveedores(request):
    proveedores = Proveedor.objects.filter(estado=1)
    serializer = ProveedorSerializer(proveedores, many=True)
    return Response(serializer.data)

@api_view(["POST"])
def postProveedores(request):
    serializer = ProveedorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)