from rest_framework import serializers
from api.models import Evento, Categorias, Imagenes, Proveedor


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorias
        fields = '__all__'


class ImagenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagenes
        fields = ['url', 'nombre']


class EventoSerializer(serializers.ModelSerializer):
    categoria_nombre = serializers.ReadOnlyField(source='idcategoria.nombre')
    imagenes = ImagenSerializer(many=True, read_only=True, source='imagenes_set')
    class Meta:
        model = Evento
        fields = '__all__'
        
class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'