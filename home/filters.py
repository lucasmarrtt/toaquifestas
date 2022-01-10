import django_filters 
from . models import Anuncios, Promocoes

class AnuncioFilter(django_filters.FilterSet):
    class Meta:
        model = Anuncios
        fields = [
            'titulo',
            'estado', 
            'cidade',
            'categoria', 
            'bairro',

        ]

class PromocoesFilter(django_filters.FilterSet):
    class Meta:
        
        model = Promocoes
        fields = [
            'titulo',
            'estado', 
            'cidade',
            'categoria',
            'bairro',
        ]

     