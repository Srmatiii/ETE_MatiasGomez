from django.urls import path
from .views import Inicio, Catalogo, Acercade, formulario, actualizar, form_colaboradores, VerColaboradores, modColaborador, delColaborador

urlpatterns = [
    path('',Inicio,name="Inicio"),
    path('Catalogo',Catalogo,name="Catalogo"),
    path('Acercade',Acercade,name="Acercade"),
    path('formulario',formulario,name="formulario"),
    path('actualizar',actualizar,name="actualizar"),
    path('form_colaboradores',form_colaboradores,name="form_colaboradores"),
    path('VerColaboradores',VerColaboradores,name="VerColaboradores"),
    path('modColaborador',modColaborador,name="modColaborador"),
    path('delColaborador',delColaborador,name="delColaborador"),

]

