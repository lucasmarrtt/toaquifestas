from django.db import models
from django.db.models.aggregates import Max

from stdimage.models import StdImageField

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


class Estado(models.Model):
    nome = models.CharField('Estado', max_length=255)

    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'

    def __str__(self):
        return self.nome   


class Cidade(models.Model):
    nome = models.CharField('Nome da cidade', max_length=255)     

    class Meta:
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'    

    def __str__(self):
        return self.nome     
    

class Anuncios(models.Model):
    criado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    imagem = StdImageField('Imagem', upload_to='Anuncios', variations={'thumb': {'width': 351, 'height': 215, 'crop': True }}) 
    titulo = models.CharField('Nome do anúncio', max_length=255)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    descricao = models.TextField('Descrição', max_length=255)
    endereco = models.CharField('Endereço', max_length=255)
    cep = models.IntegerField('CEP', )
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    telefone = models.IntegerField('Telefone', )
    email = models.EmailField('E-mail', max_length=255, null=True, blank=True)
    facebook = models.CharField('Facebook', max_length=255, null=True, blank=True)
    istagram = models.CharField('Instagram', max_length=255, null=True, blank=True)
    produtos = models.TextField('Produtos que vendem', )
    google_maps = models.TextField('Google maps', null=True, blank=True)

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
    nomec = models.CharField('Nome do cliente', max_length=255)
    cpfc = models.IntegerField('CPF',)
    telefonec = models.IntegerField('Telefone',)
    emailc = models.EmailField('E-mail do cliente',)
    imagem = StdImageField('Imagem', upload_to='Anuncios', variations={'thumb': {'width': 351, 'height': 215, 'crop': True }}) 
    titulo = models.CharField('Título do anúncio', max_length=255)
    descricao = models.TextField('Descrição', max_length=255)
    endereco = models.CharField('Endereço', max_length=255)
    cep = models.IntegerField('CEP', )
    estado = models.TextField('Descrição', max_length=255)
    cidade = models.CharField('Endereço', max_length=255)
    telefone = models.IntegerField('Telefone', )
    email = models.EmailField('E-mail', max_length=255, null=True, blank=True)
    facebook = models.CharField('Facebook', max_length=255, null=True, blank=True)
    istagram = models.CharField('Instagram', max_length=255, null=True, blank=True)
    produtos = models.TextField('Produtos que vendem', )
    google_maps = models.TextField('Google maps', null=True, blank=True)

    class Meta:
        verbose_name = 'Solicitação'
        verbose_name_plural = 'Solicitações'

    def __str__(self):
        return self.nomec


class Renovacao(models.Model):
    nome = models.CharField('Nome', max_length=255)
    cpf = models.IntegerField('CPF')
    telefone = models.IntegerField('Telefone')
    email = models.EmailField('Telefone', )

    class Meta:
        verbose_name = 'Renovação'
        verbose_name_plural = 'Renovações'

    def __str__(self):
        return self.nome    

    
class Reclamacoes(models.Model):
    nome = models.CharField('Nome', max_length=255)
    email = models.EmailField('Email', max_length=255)
    telefone = models.IntegerField('Telefone', )
    assunto = models.CharField('Assunto', max_length=255)
    nome_do_parceiro = models.CharField('Nome do parceiro', max_length=255)
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
    nome = models.CharField('Nome', max_length=255)
    depoimento = models.TextField('Depoimento', max_length=255)
    empresa = models.CharField('Empresa', max_length=255)

    class Meta:
        verbose_name = 'Depoimento'
        verbose_name_plural = 'Depoimentos'

    def __str__(self):
        return self.nome  

    