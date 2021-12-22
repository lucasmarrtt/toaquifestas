from django.db import models

from stdimage.models import StdImageField

# Create your models here.
class Categorias(models.Model):
    imagem = StdImageField('Imagem', upload_to='Categorias', variations={'thumb':{'width': 290, 'height': 174, 'crop': True }}) 
    nome = models.CharField('Nome da categoria', max_length=255)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural =  'Categorias'

    def __str__(self):
        return self.nome    


class Anuncios(models.Model):
    titulo = models.CharField('Título', max_length=255)
    endereco = models.CharField('Endereço', max_length=255)
    telefone = models.CharField('Telefone', max_length=255)

    class Meta:
        verbose_name = 'Anuncio'
        verbose_name_plural = 'Anuncios'

    def __str__(self):
        return self.titulo     
    
    