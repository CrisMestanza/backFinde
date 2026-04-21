from django.urls import path
from api.views.categorias import *
from api.views.eventos import *
from api.views.proveedor import *

urlpatterns = [

    # Categorias
    path('getcategorias/', getCategorias),
    path('postcategorias/', postCategorias),
    
    # Proveedores
    path('getproveedores/', getProveedores),
    path('postproveedores/', postProveedores),
    
    # Eventos
    path('geteventos/', getEventos),
    path('posteventos/', postEventos),
    

]