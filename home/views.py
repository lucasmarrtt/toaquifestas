from django.db.models import query
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import DetailView
from django.views.generic.base import ContextMixin

from . models import Categorias, Anuncios, Depoimentos, Promocoes, Renovacao

# Filtro e paginação
from . filters import AnuncioFilter, PromocoesFilter
from django.core.paginator import Paginator 

# Form solicitação de anúncio 
from . forms import SolicitacaoForm, ReclamacoesForm, RenovacaoForm

# Create your views here.
def index(request):
    categoria = Categorias.objects.all().order_by('-criado')[0:16]
    depoimento = Depoimentos.objects.all().order_by('-criado')[0:5]

    form = ReclamacoesForm()

    if request.method == 'POST':
        form = ReclamacoesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

        return redirect('/')
    
    context = {
        'lista_de_categorias': categoria,
        'lista_de_depoimentos': depoimento, 
        'form': form, 
    }
    return render(request, 'index.html', context)


def cadastre_se(request):
    return render(request, 'cadastre-se.html')


def planos(request):
    return render(request, 'planos.html')


def contato(request):
    return render(request, 'contato.html')   


def depoimentos(request):
    depoimento = Depoimentos.objects.all().order_by('-criado')[0:20]
    context = {
        'lista_de_depoimentos': depoimento,
    }
    return render(request, 'depoimentos.html', context)      


def listaDeAnuncios(request):
    context = {}

    filtered_anuncios = AnuncioFilter(
        request.GET,
        queryset=Anuncios.objects.all()

    )

    context['filtered_anuncios'] = filtered_anuncios

    paginated_filtered_anuncios = Paginator(filtered_anuncios.qs, 10)

    page_number = request.GET.get('page')
    anuncio_page_obj = paginated_filtered_anuncios.get_page(page_number)

    context['anuncio_page_obj'] = anuncio_page_obj



    return render(request, 'lista-de-anuncios.html', context)


class DetalhesDoAnuncioView(DetailView):
    model = Anuncios
    template_name = 'detalhes-do-anuncio.html'


def listaDeCategorias(request, cats):
    context = {}
    filtered_categorias = AnuncioFilter(
        request.GET, queryset=Anuncios.objects.filter(categoria=cats)
    )

    context['filtered_categorias'] = filtered_categorias

    paginated_filter_categorias = Paginator(filtered_categorias.qs, 10)

    page_number = request.GET.get('page')
    categorias_page_obj = paginated_filter_categorias.get_page(page_number)

    context['categoria_page_obj'] = categorias_page_obj

    
    return render(request, 'lista-de-categorias.html', context)


def listaDePromocoes(request):
    context = {}

    filtered_promocoes = PromocoesFilter(
        request.GET,
        queryset=Promocoes.objects.all()

    )

    context['filtered_promocoes'] = filtered_promocoes

    paginated_filtered_promocoes = Paginator(filtered_promocoes.qs, 1)

    page_number = request.GET.get('page')
    promocoes_page_obj = paginated_filtered_promocoes.get_page(page_number)

    context['promocoes_page_obj'] = promocoes_page_obj



    return render(request, 'lista-de-promocoes.html', context)



class DetalhesDaPromocaoView(DetailView):
    model = Promocoes
    template_name = 'detalhes-da-promocao.html'


# Páginas de submeter anúncios 
def basico(request):
    form = SolicitacaoForm()
    if request.method == 'POST':
        # Quando for enviar imagem, colocar request.FILES
        form = SolicitacaoForm(request.POST, request.FILES)
        if form.is_valid(): 
            form.save()
        return redirect('https://mpago.la/1Z6bUAA')    
    context = {
        'form': form, 
    }
    return render(request, 'forms/basico.html', context)


def classico(request):
    form = SolicitacaoForm()
    if request.method == 'POST':
        # Quando for enviar imagem, colocar request.FILES
        form = SolicitacaoForm(request.POST, request.FILES)
        if form.is_valid(): 
            form.save()
        return redirect('/classico-2')    
    context = {
        'form': form, 
    }
    return render(request, 'forms/classico.html', context)


def classico_2(request):
    form = SolicitacaoForm()
    if request.method == 'POST':
        # Quando for enviar imagem, colocar request.FILES
        form = SolicitacaoForm(request.POST, request.FILES)
        if form.is_valid(): 
            form.save()
        return redirect('https://mpago.la/2GiCCaH')    
    context = {
        'form': form, 
    }
    return render(request, 'forms/classico-2.html', context)


def premium(request):
    form = SolicitacaoForm()
    if request.method == 'POST':
        # Quando for enviar imagem, colocar request.FILES
        form = SolicitacaoForm(request.POST, request.FILES)
        if form.is_valid(): 
            form.save()
        return redirect('/premium-2')    
    context = {
        'form': form, 
    }
    return render(request, 'forms/premium.html', context)


def premium_2(request):
    form = SolicitacaoForm()
    if request.method == 'POST':
        # Quando for enviar imagem, colocar request.FILES
        form = SolicitacaoForm(request.POST, request.FILES)
        if form.is_valid(): 
            form.save()
        return redirect('/premium-3')    
    context = {
        'form': form, 
    }
    return render(request, 'forms/premium.html', context)


def premium_3(request):
    form = SolicitacaoForm()
    if request.method == 'POST':
        # Quando for enviar imagem, colocar request.FILES
        form = SolicitacaoForm(request.POST, request.FILES)
        if form.is_valid(): 
            form.save()
        return redirect('/premium-4')    
    context = {
        'form': form, 
    }
    return render(request, 'forms/premium.html', context)


def premium_4(request):
    form = SolicitacaoForm()
    if request.method == 'POST':
        # Quando for enviar imagem, colocar request.FILES
        form = SolicitacaoForm(request.POST, request.FILES)
        if form.is_valid(): 
            form.save()
        return redirect('https://mpago.la/1ZRy6KZ')    
    context = {
        'form': form, 

    }
    return render(request, 'forms/premium-4.html', context)


def renovacao(request):
    form = RenovacaoForm()
    if request.method == 'POST':
        # Quando for enviar imagem, colocar request.FILES
        form = RenovacaoForm(request.POST)
        if form.is_valid(): 
            form.save()
        return redirect('/')    
    context = {
        'form': form, 

    }
    return render(request, 'renovacao.html', context)