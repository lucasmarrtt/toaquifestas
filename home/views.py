from django.shortcuts import render

from . models import Categorias, Anuncios

# Create your views here.
def index(request):
    categoria = Categorias.objects.all().order_by('-criado')[0:16]
    context = {
        'lista_de_categorias': categoria
    }
    return render(request, 'index.html', context)


def listaDeAnuncios(request):
    anuncio = Anuncios.objects.all()
    context = {
        'lista_de_anuncios': anuncio
    }
    return render(request, 'lista-de-anuncios.html', context)


def detalhesDoAnuncio(request, pk):
    anuncio = Anuncios.objects.get(id=pk)

    context = {
        'detalhes_do_anuncio': anuncio, 
    }

    return render(request, 'detalhes-do-anuncio.html', context)    


def listaDeCategorias(request, cats):
    categoria = Anuncios.objects.filter(categoria=cats)
    context = {
        'lista_de_categorias': categoria
    }
    return render(request, 'lista-de-categorias.html', context)
