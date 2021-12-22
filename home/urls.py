from django.urls import path
from . views import index, listaDePostagens, anuncioDetalhes

urlpatterns = [
    path('', index, name='index'), 
    path('lista-de-postagens/', listaDePostagens, name='lista-de-postagens'), 
    path('anuncio-detalhes/', anuncioDetalhes, name='anuncio-detalhes'),

] 
