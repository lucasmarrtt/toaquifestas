from django.contrib import admin
from . models import Categorias, Estado, Cidade, Anuncios, Reclamacoes, Depoimentos, Solicitacao

# Register your models here.
@admin.register(Categorias)
class CategoriasAdmin(admin.ModelAdmin):
	list_display = ('nome', )


@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
	list_display = ('nome', )


@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
	list_display = ('nome', )


@admin.register(Anuncios)
class AnunciosAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'endereco', 'telefone', 'email', 'estado', 'categoria')


@admin.register(Reclamacoes)
class ReclamacoesAdmin(admin.ModelAdmin):
	list_display = ('nome', 'email', 'telefone', 'nome_do_parceiro', 'fatos',)	


@admin.register(Depoimentos)
class DepoimentosAdmin(admin.ModelAdmin):
	list_display = ('nome',)	


@admin.register(Solicitacao)
class SolicitacaoAdmin(admin.ModelAdmin):
	list_display = ('nomec', 'cpfc', 'telefonec', 'emailc',)	