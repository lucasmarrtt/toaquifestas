from django.contrib import admin
from . models import Categorias, Anuncios, Reclamacoes, Depoimentos, Solicitacao, Renovacao, City, District 

# Register your models here.
@admin.register(Categorias)
class CategoriasAdmin(admin.ModelAdmin):
	list_display = ('nome', )


admin.site.register(City)
admin.site.register(District)


@admin.register(Anuncios)
class AnunciosAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'endereco', 'telefone', 'email', 'estado', 'categoria', 'criado', 'publicado', 'promocao')


@admin.register(Reclamacoes)
class ReclamacoesAdmin(admin.ModelAdmin):
	list_display = ('nome', 'email', 'telefone', 'nome_do_parceiro', 'fatos',)	


@admin.register(Depoimentos)
class DepoimentosAdmin(admin.ModelAdmin):
	list_display = ('nome',)	


@admin.register(Solicitacao)
class SolicitacaoAdmin(admin.ModelAdmin):
	list_display = ('nomec', 'cpfc', 'telefonec', 'emailc', 'criado')	


@admin.register(Renovacao)
class RenovacaoAdmin(admin.ModelAdmin):
	list_display = ('nome', 'cpf', 'telefone', 'email',)	

