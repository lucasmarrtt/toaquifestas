from django.urls import path
from . views import (index, cadastre_se, depoimentos, planos, contato, listaDeAnuncios, listaDeCategorias, basico, DetalhesDoAnuncioView, DetalhesDaPromocaoView,
classico, classico_2, premium, premium_2, premium_3, premium_4, listaDePromocoes, renovacao)


urlpatterns = [
    path('', index, name='index'), 
    path('cadastre-se/', cadastre_se, name='cadastre-se'),
    path('depoimentos/', depoimentos, name='depoimentos'),  
    path('planos/', planos, name='planos'),
    path('contato/', contato, name='contato'),
    path('lista-de-anuncios/', listaDeAnuncios, name='lista-de-anuncios'),
    path('lista-de-promocoes/', listaDePromocoes, name='lista-de-promocoes'), 
    path('lista-de-anuncios/<slug:slug>', DetalhesDoAnuncioView.as_view(), name='detalhes-do-anuncio'), 
    path('lista-de-promocoes/<slug:slug>', DetalhesDaPromocaoView.as_view(), name='detalhes-da-promocao'), 
    path('lista-de-categorias/<int:cats>', listaDeCategorias, name='lista-de-categorias'),
    path('renovacao/', renovacao, name='renovacao'),
    
    # Urls para submeter
    path('basico/', basico, name='basico'),
    path('classico/', classico, name='classico'),
    path('classico-2/', classico_2, name='classico-2'),
    path('premium/', premium, name='premium'),
    path('premium-2/', premium_2, name='premium-2'),
    path('premium-3/', premium_3, name='premium-3'),
    path('premium-4/', premium_4, name='premium-4'),
] 

