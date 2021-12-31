import django_filters 
from . models import Anuncios

class AnuncioFilter(django_filters.FilterSet):
    class Meta:
        model = Anuncios
        fields = [
            'nome',
            'estado', 
            'cidade',
            'categoria', 

        ]

