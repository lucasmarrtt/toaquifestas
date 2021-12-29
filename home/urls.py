from django.urls import path
from . views import index, listaDeAnuncios, detalhesDoAnuncio, listaDeCategorias

urlpatterns = [
    path('', index, name='index'), 
    path('lista-de-anuncios/', listaDeAnuncios, name='lista-de-anuncios'), 
    path('detalhes-do-anuncio/<int:pk>', detalhesDoAnuncio, name='detalhes-do-anuncio'),
    path('lista-de-categorias/<int:cats>', listaDeCategorias, name='lista-de-categorias'),
] 

