from django.contrib import admin
from . models import Categorias, Anuncios 

# Register your models here.
@admin.register(Categorias)
class CategoriasAdmin(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(Anuncios)
class AnunciosAdmmin(admin.ModelAdmin):
    list_display = ('titulo', )

