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

@api_view(["POST"])
def deleteCategorias(request):
    print("Solicitud recibida para eliminar categoría.")
    id = request.data.get("idcategorias")
    print(" ID recibido:", id)  # Agrega esta línea para verificar el ID recibido
    try:
        categoria = Categorias.objects.get(idcategorias=id)
        print(categoria)
        categoria.estado = 0
        categoria.save()
        return Response({"message": "Categoria eliminada correctamente."}, status=200)
    except Categorias.DoesNotExist:
        return Response({"error": "Categoria no encontrada."}, status=404)
