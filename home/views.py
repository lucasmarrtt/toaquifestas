from django.shortcuts import render

from . models import Categorias, Anuncios

# Create your views here.
def index(request):
    categorias = Categorias.objects.all()
    context = {
        'lista_de_categorias': categorias
    }
    return render(request, 'index.html', context)

def listaDePostagens(request):
    anuncio = Anuncios.objects.all()
    context = {
        'lista_de_anuncios': anuncio
    }
    return render(request, 'lista-de-postagens.html', context)