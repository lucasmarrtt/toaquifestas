import django_filters 
from . models import Anuncios

class AnuncioFilter(django_filters.FilterSet):
    class Meta:
        model = Anuncios
        '''fields = [
            'titulo',
            'estado', 
            'cidade',
            'categoria', 

        ]'''

        fields = {
            'titulo': ['exact', 'contains'],
            'estado': ['exact'],
            'cidade': ['exact'],
            'categoria': ['exact'],
            
        }

