from django.urls import path
from . views import index, listaDePostagens

urlpatterns = [
    path('', index, name='index'), 
    path('lista-de-postagens/', listaDePostagens, name='lista-de-postagens'), 
] 
