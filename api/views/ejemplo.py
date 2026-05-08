from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Categorias
from ..serializers import CategoriaSerializer


@api_view(["GET"])
def getOrlando(request):
    catoregorias = Categorias.objects.filter(estado=0)
    serializer = CategoriaSerializer(catoregorias, many=True)
    return Response(serializer.data)

