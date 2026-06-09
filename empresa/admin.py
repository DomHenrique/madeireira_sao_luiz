from django.contrib import admin
from .models import Unidade

@admin.register(Unidade)
class UnidadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'cidade', 'estado', 'is_active', 'ordem')
    list_editable = ('is_active', 'ordem')
    list_filter = ('tipo', 'is_active', 'estado')
    search_fields = ('nome', 'cidade', 'endereco')
    
    fieldsets = (
        ("Informações Básicas", {
            "fields": ('nome', 'tipo', 'is_active', 'ordem')
        }),
        ("Títulos (Seção Localização da Home)", {
            "description": "Estes textos aparecem apenas na aba desta unidade na Home.",
            "fields": ('title_eyebrow', 'title_main', 'card_title')
        }),
        ("Endereço e Horários", {
            "fields": ('endereco', 'cidade', 'estado', 'cep', 'business_hours')
        }),
        ("Contatos", {
            "fields": ('email', 'telefone', 'whatsapp')
        }),
        ("Mapas", {
            "fields": ('mapa_url', 'rota_url')
        }),
    )
