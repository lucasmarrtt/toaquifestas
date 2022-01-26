from django.db import models
from django.db.models.aggregates import Max

from stdimage.models import StdImageField

# Local Flavor
from localflavor.br.br_states import STATE_CHOICES

# Slug na url 
from django.utils.text import slugify 
from django.urls import reverse 

# Create your models here.
class Categorias(models.Model):
    criado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    imagem = StdImageField('Imagem', upload_to='Categorias', variations={'thumb': {'width': 351, 'height': 215, 'crop': True }}) 
    nome = models.CharField('Nome da categoria', max_length=255)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nome


class City(models.Model):
    name = models.CharField('cidade', max_length=100)
    uf = models.CharField('UF', max_length=2, choices=STATE_CHOICES)

    def __str__(self):
        return f'{self.name}, {self.uf}'

    class Meta:
        ordering = ('name',)
        verbose_name = 'cidade'
        verbose_name_plural = 'cidades'


class District(models.Model):
    name = models.CharField('distrito', max_length=100)
    city = models.ForeignKey(
        'City',
        verbose_name='cidade',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.name}, {self.city}'

    class Meta:
        ordering = ('name',)
        verbose_name = 'distrito'
        verbose_name_plural = 'distritos'


class Anuncios(models.Model):
    criado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    imagem = StdImageField('Imagem', upload_to='Anuncios', null=True, blank=True, variations={'thumb': {'width': 351, 'height': 215, 'crop': True }}) 
    titulo = models.CharField('Nome do anúncio', max_length=255)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    descricao = models.TextField('Descrição', max_length=255)
    endereco = models.CharField('Endereço', max_length=255)
    cep = models.CharField('CEP', max_length=255)
    estado = models.CharField('Estado', max_length=55, choices=STATE_CHOICES)
    cidade = models.ForeignKey(City, on_delete=models.CASCADE)
    bairro = models.ForeignKey(District, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    telefone = models.CharField('Telefone', max_length=255)
    email = models.EmailField('E-mail', max_length=255, null=True, blank=True)
    facebook = models.CharField('Facebook', max_length=255, null=True, blank=True)
    istagram = models.CharField('Instagram', max_length=255, null=True, blank=True)
    google_maps = models.TextField('Google maps', null=True, blank=True)
    # Observação 
    publicado = models.BooleanField(default=True)
    promocao = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Anuncio'
        verbose_name_plural = 'Anuncios'

    def __str__(self):
        return self.titulo  

    def get_absolute_url(self):
        return reverse('detalhes-do-anuncio', kwargs={'slug': self.slug})    

    def save(self, *args, **kwargs):
        value = self.titulo 
        self.slug = slugify(value, allow_unicode=False)    
        super().save(*args, **kwargs)


class Solicitacao(models.Model):
    criado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    nomec = models.CharField('Nome do cliente', max_length=255)
    cpfc = models.CharField('CPF', max_length=20)
    telefonec = models.CharField('Telefone', max_length=20)
    emailc = models.EmailField('E-mail do cliente',)
    imagem = StdImageField('Imagem', upload_to='Solicitacoes', null=True, blank=True, variations={'thumb': {'width': 351, 'height': 215, 'crop': True }}) 
    titulo = models.CharField('Título do anúncio', max_length=255)
    CATEGORIA_CHOICES = (
        ('salgados', 'Salgados'),
        ('doces', 'Doces'), 
        ('bolos', 'Bolos'), 
        ('bolos_fake', 'Bolos Fake'),
        ('estacao_de_festas', 'Estação De Festas'),
        ('bebidas_e_drinks', 'Bebidas e Drinks'),
        ('garcons', 'Garçons'),
        ('temas_e_decoracoes', 'Temas e Decorações'),
        ('lembrancinhas_personalizadas', 'Lembrancinhas Personalizadas'),
        ('topo_de_bolo', 'Topo de Bolo'),
        ('mesas_e_cadeiras', 'Mesas e Cadeiras'),
        ('convites', 'Convites'),
        ('recreacao_infantil', 'Recreação Infantil'), 
        ('roupas_tematicas', 'Roupas Tematicas/Fantasias'),
        ('musica', 'Músicos/Djs'),
        ('fotos_e_filmagens', 'Fotos e Filmagens'),
        ('artigos_para_festas', 'Artigos Para Festas'),
        ('casa_de_festas', 'Casa de Festas'),
    )
    categoria = models.CharField('Categorias', max_length=55, choices=CATEGORIA_CHOICES)
    descricao = models.TextField('Descrição', max_length=255)
    endereco = models.CharField('Endereço', max_length=255)
    cep = models.CharField('CEP', max_length=20)
    estado = models.TextField('Descrição', max_length=255)
    cidade = models.CharField('Endereço', max_length=255)
    bairro = models.CharField('Bairro', max_length=255)
    telefone = models.CharField('Telefone', max_length=20)
    email = models.EmailField('E-mail', max_length=255, null=True, blank=True)
    facebook = models.CharField('Facebook', max_length=255, null=True, blank=True)
    istagram = models.CharField('Instagram', max_length=255, null=True, blank=True)
    google_maps = models.TextField('Google maps', null=True, blank=True)

    class Meta:
        verbose_name = 'Solicitação'
        verbose_name_plural = 'Solicitações'

    def __str__(self):
        return self.nomec


class Renovacao(models.Model):
    nome = models.CharField('Nome', max_length=255)
    cpf = models.CharField('CPF', max_length=20)
    telefone = models.CharField('Telefone', max_length=20)
    email = models.EmailField('Telefone', )

    class Meta:
        verbose_name = 'Renovação'
        verbose_name_plural = 'Renovações'

    def __str__(self):
        return self.nome    

    
class Reclamacoes(models.Model):
    nome = models.CharField('Nome', max_length=255)
    email = models.EmailField('Email', max_length=255)
    telefone = models.CharField('Telefone', max_length=20)
    assunto = models.CharField('Assunto', max_length=255)
    nome_do_parceiro = models.CharField('Nome do parceiro', max_length=255)
    arquivo = models.FileField('Arquivos', upload_to='Arquivos')
    fatos = models.TextField('Fatos', )

    class Meta:
        verbose_name = 'Reclamação'
        verbose_name_plural = 'Reclamações'

    def __str__(self):
        return self.nome    

        
class Depoimentos(models.Model):
    criado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    imagem = StdImageField('Imagem', upload_to='Depoimentos', variations={'thumb': {'width': 351, 'height': 215, 'crop': True }}) 
    nome = models.CharField('Nome', max_length=55)
    depoimento = models.TextField('Depoimento', max_length=255)
    empresa = models.CharField('Empresa', max_length=55)

    class Meta:
        verbose_name = 'Depoimento'
        verbose_name_plural = 'Depoimentos'

    def __str__(self):
        return self.nome  

    

