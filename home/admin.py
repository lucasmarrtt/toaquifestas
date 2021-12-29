from django.contrib import admin
from . models import Categorias, Anuncios, Estado 

# Register your models here.
@admin.register(Categorias)
class CategoriasAdmin(admin.ModelAdmin):
	list_display = ('nome', )


@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
	list_display = ('nome', )


@admin.register(Anuncios)
class AnunciosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco', 'telefone', 'email', 'estado', 'categoria')

