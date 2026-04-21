from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Categorias
from ..serializers import CategoriaSerializer


@api_view(["GET"])
def getCategorias(request):
    categorias = Categorias.objects.filter(estado=1)
    serializer = CategoriaSerializer(categorias, many=True)
    return Response(serializer.data)

@api_view(["POST"])
def postCategorias(request):
    serializer = CategoriaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)