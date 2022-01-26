from django.db.models import query
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import DetailView
from django.views.generic.base import ContextMixin

from . models import Categorias, Anuncios, Depoimentos, Renovacao, City, District

# Local Flavor
from localflavor.br.br_states import STATE_CHOICES

# Filtro e paginação
from . filters import AnuncioFilter
from django.core.paginator import Paginator 

# Form solicitação de anúncio 
from . forms import SolicitacaoForm, ReclamacoesForm, RenovacaoForm, StateForm

# Envio de E-mail
from django.core.mail import send_mail

from django.http import JsonResponse

# Create your views here.
def index(request):
    categoria = Categorias.objects.all().order_by('-criado')[0:19]
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
    if request.method == 'POST':
        name = request.POST.get('nome')
        email = request.POST.get('email')
        subject = request.POST.get('assunto')
        message = request.POST.get('mensagem')

        data = {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message, 
        }
        message = '''
        Nova mensagem: {}

        De: {}
        
        '''.format(data['message'], data['email'])

        send_mail(data['subject'], message, '', ['contato@toaquifestas.com.br'])

        return redirect('/')

    return render(request, 'contato.html', {})   


def depoimentos(request):
    depoimento = Depoimentos.objects.all().order_by('-criado')[0:20]
    context = {
        'lista_de_depoimentos': depoimento,
    }
    return render(request, 'depoimentos.html', context)   


def politicaDePrivacidade(request):
    return render(request, 'politica-de-privacidade.html')  


def termosDeUso(request):
    return render(request, 'termos-de-uso.html')          


def listaDeAnuncios(request):
    context = {}
    context['form'] = StateForm 

    anuncio = Anuncios.objects.all()
    

    '''
    q = request.GET.get('bairro')
    if q:
        anuncio = Anuncios.objects.filter(bairro=q)
        context['anuncio'] = anuncio    '''


    anuncio_list = AnuncioFilter(
        request.GET,
        queryset = Anuncios.objects.all()
    )    

    context['anuncio_list'] = anuncio_list


    paginated_filtered_persons = Paginator(anuncio_list.qs, 10)

    page_number = request.GET.get('page')
    person_page_obj = paginated_filtered_persons.get_page(page_number)

    context['person_page_obj'] = person_page_obj


    

    return render(request, 'lista-de-anuncios.html', context)






def filter_list(request):
    context = {}
    cities = City.objects.all()
    districts = District.objects.all()
    context['states'] = STATE_CHOICES
    context['cities'] = cities
    context['districts'] = districts

    return render(request, 'filter-list.html', context)

def cities_ajax(request):
    uf = request.GET.get('uf')    
    cities = City.objects.filter(uf=uf)
    context = {'cities': cities}

    return render(request, 'includes/__cities.html', context)


def cities_choices_ajax(request):
    uf = request.GET.get('uf')    
    cities = City.objects.filter(uf=uf)
    context = {'cities': cities}

    return render(request, 'includes/__cities-choices.html', context)    


def districts_choices_ajax(request):
    city = request.GET.get('city')    
    districts = District.objects.filter(city=city)
    context = {'districts': districts}

    return render(request, 'includes/__districts-choices.html', context)


def districts_ajax(request):
    city = request.GET.get('city')    
    districts = District.objects.filter(city=city)
    context = {'districts': districts}

    return render(request, 'includes/__districts.html', context)    



class DetalhesDoAnuncioView(DetailView):
    model = Anuncios
    template_name = 'detalhes-do-anuncio.html'


def listaDeCategorias(request, cats):
    context = {}

    context['form'] = StateForm 
    
    filtered_categorias = AnuncioFilter(
        request.GET, 
        queryset=Anuncios.objects.filter(categoria=cats, publicado=True)
    )

    context['filtered_categorias'] = filtered_categorias

    paginated_filter_categorias = Paginator(filtered_categorias.qs, 10)

    page_number = request.GET.get('page')
    categorias_page_obj = paginated_filter_categorias.get_page(page_number)

    context['categoria_page_obj'] = categorias_page_obj

    
    return render(request, 'lista-de-categorias.html', context)


def listaDePromocoes(request):
    context = {}

    context['form'] = StateForm 

    filtered_promocoes = AnuncioFilter(
        request.GET,
        queryset=Anuncios.objects.all().filter(publicado=True, promocao=True)

    )

    context['filtered_promocoes'] = filtered_promocoes

    paginated_filtered_promocoes = Paginator(filtered_promocoes.qs, 10)

    page_number = request.GET.get('page')
    promocoes_page_obj = paginated_filtered_promocoes.get_page(page_number)

    context['promocoes_page_obj'] = promocoes_page_obj



    return render(request, 'lista-de-promocoes.html', context)



class DetalhesDaPromocaoView(DetailView):
    model = Anuncios
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


def get_json_car_data(request):
    qs_val = list(Car.objects.values())
    return JsonResponse({'data': qs_val})


def get_json_model_data(request, *args, **kwargs):
    selected_car = kwargs.get('car')
    obj_models = list(Model.objects.filter(car__name=selected_car).values())
    return JsonResponse({'data':obj_models})    

