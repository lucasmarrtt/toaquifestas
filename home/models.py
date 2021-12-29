from django.db import models

from stdimage.models import StdImageField

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
    

class Anuncios(models.Model):
    criado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    nome = models.CharField('Nome', max_length=255)
    descricao = models.TextField('Descrição', )
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    endereco = models.CharField('Endereço', max_length=255)
    telefone = models.CharField('Telefone', max_length=255)
    email = models.EmailField('E-mail', max_length=255, null=True, blank=True)
    facebook = models.CharField('Facebook', max_length=255, null=True, blank=True)
    istagram = models.CharField('Instagram', max_length=255, null=True, blank=True)


    class Meta:
        verbose_name = 'Anuncio'
        verbose_name_plural = 'Anuncios'

    def __str__(self):
        return self.nome     
    
    

        


