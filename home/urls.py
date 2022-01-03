from django.urls import path
from . views import index, cadastre_se, planos, contato, listaDeAnuncios, listaDeCategorias, basico, DetalhesDoAnuncioView, classico, classico_2, premium, premium_2, premium_3, premium_4


urlpatterns = [
    path('', index, name='index'), 
    path('cadastre-se/', cadastre_se, name='cadastre-se'), 
    path('planos/', planos, name='planos'),
    path('contato/', contato, name='contato'),
    path('lista-de-anuncios/', listaDeAnuncios, name='lista-de-anuncios'), 
    path('lista-de-anuncios/<slug:slug>', DetalhesDoAnuncioView.as_view(), name='detalhes-do-anuncio'), 
    path('lista-de-categorias/<int:cats>', listaDeCategorias, name='lista-de-categorias'),
    
    # Urls para submeter
    path('basico/', basico, name='basico'),
    path('classico/', classico, name='classico'),
    path('classico-2/', classico_2, name='classico-2'),
    path('premium/', premium, name='premium'),
    path('premium-2/', premium_2, name='premium-2'),
    path('premium-3/', premium_3, name='premium-3'),
    path('premium-4/', premium_4, name='premium-4'),
] 

