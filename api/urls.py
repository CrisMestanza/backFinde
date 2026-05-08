from django.urls import path
from api.views.categorias import *
from api.views.eventos import *
from api.views.proveedor import *
from api.views.ejemplo import *

urlpatterns = [

    # Categorias
    path('getcategorias/', getCategorias),
    path('postcategorias/', postCategorias),

    path('orlando/', getOrlando),    
    path('deletecategorias/', deleteCategorias),

    # Proveedores
    path('getproveedores/', getProveedores),
    path('postproveedores/', postProveedores),
    
    # Eventos
    path('geteventos/', getEventos),
    path('posteventos/', postEventos),
    
     
    path('deleteeventos/', deleteEventos),
    path('validar/', validar),
]