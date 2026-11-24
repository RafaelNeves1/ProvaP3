from django.contrib import admin
from .models import Lote, Produtor


@admin.register(Produtor)
class ProdutorAdmin(admin.ModelAdmin):
    list_display = ("nome", "cidade", "cpf_cnpj")
    search_fields = ("nome", "cidade", "cpf_cnpj")


@admin.register(Lote)
class LoteAdmin(admin.ModelAdmin):
    list_display = ("variedade", "produtor", "caixas", "preco_caixa", "data")
    list_filter = ("variedade", "data")
    search_fields = ("produtor__nome", "variedade")
