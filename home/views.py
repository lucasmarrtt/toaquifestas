from django.db.models import query
from django.shortcuts import render

from . models import Categorias, Anuncios, Depoimentos 

# Filtro e paginação
from . filters import AnuncioFilter
from django.core.paginator import Paginator 

# Create your views here.
def index(request):
    categoria = Categorias.objects.all().order_by('-criado')[0:16]
    depoimento = Depoimentos.objects.all().order_by('-criado')[0:5]
    context = {
        'lista_de_categorias': categoria,
        'lista_de_depoimentos': depoimento
    }
    return render(request, 'index.html', context)


def cadastre_se(request):
    return render(request, 'cadastre-se.html')


def planos(request):
    return render(request, 'planos.html')


def contato(request):
    return render(request, 'contato.html')    


def listaDeAnuncios(request):
    context = {}

    filtered_anuncios = AnuncioFilter(
        request.GET,
        queryset=Anuncios.objects.all()

    )

    context['filtered_anuncios'] = filtered_anuncios

    paginated_filtered_anuncios = Paginator(filtered_anuncios.qs, 1)

    page_number = request.GET.get('page')
    anuncio_page_obj = paginated_filtered_anuncios.get_page(page_number)

    context['anuncio_page_obj'] = anuncio_page_obj



    return render(request, 'lista-de-anuncios.html', context)

'''
def listaDeAnuncios(request):
    anuncio = Anuncios.objects.all()
    filtro_de_anuncios = AnuncioFilter(request.GET, queryset=anuncio)

    context = {
        'lista_de_anuncios': anuncio, 
        'filter': filtro_de_anuncios
    }
    return render(request, 'lista-de-anuncios.html', context)'''


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
