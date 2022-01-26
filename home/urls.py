from django.urls import path
from . views import (index, cadastre_se, depoimentos, planos, contato, 
listaDeAnuncios, listaDeCategorias, basico, DetalhesDoAnuncioView, DetalhesDaPromocaoView,
classico, classico_2, premium, premium_2, premium_3, premium_4, listaDePromocoes, renovacao, 
politicaDePrivacidade, termosDeUso, filter_list, cities_ajax, districts_ajax, cities_choices_ajax, districts_choices_ajax)


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
    path('politica-de-privacidade/', politicaDePrivacidade, name='politica-de-privacidade'),
    path('termos-de-uso/', termosDeUso, name='termos-de-uso'),
    
    # Urls para submeter
    path('basico/', basico, name='basico'),
    path('classico/', classico, name='classico'),
    path('classico-2/', classico_2, name='classico-2'),
    path('premium/', premium, name='premium'),
    path('premium-2/', premium_2, name='premium-2'),
    path('premium-3/', premium_3, name='premium-3'),
    path('premium-4/', premium_4, name='premium-4'),





    # Filtrando lista 
    path('filter-list/', filter_list, name='filter-list'), 
    path('cities/ajax/', cities_ajax, name='cities_ajax'),

    path('districts/ajax/', districts_ajax, name='districts_ajax'),


    path('cities/choices/ajax/', cities_choices_ajax, name='cities_choices_ajax'),

    path('districts/choices/ajax/', districts_choices_ajax, name='districts_choices_ajax'),
    


    






    

    


] 

