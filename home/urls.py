from django.urls import path
from . views import index, cadastre_se, planos, contato, listaDeAnuncios, detalhesDoAnuncio, listaDeCategorias

urlpatterns = [
    path('', index, name='index'), 
    path('cadastre-se/', cadastre_se, name='cadastre-se'), 
    path('planos/', planos, name='planos'),
    path('contato/', contato, name='contato'),
    path('lista-de-anuncios/', listaDeAnuncios, name='lista-de-anuncios'), 
    #path('lista-de-anuncios-filter/', listaDeAnunciosFilter, name='lista-de-anuncios-filter'), 
    path('detalhes-do-anuncio/<int:pk>', detalhesDoAnuncio, name='detalhes-do-anuncio'),
    path('lista-de-categorias/<int:cats>', listaDeCategorias, name='lista-de-categorias'),
] 

