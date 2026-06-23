"""
Admin — App Core
Configurado para django-jazzmin com ações e filtros otimizados.
"""

from django.contrib import admin
from django.utils.html import format_html, mark_safe

from .models import Banner, Category, Product, Testimonial, Campaign

from django.forms.widgets import TextInput

from django.contrib.admin.actions import delete_selected
from django.urls import reverse

@admin.action(description="Excluir itens selecionados")
def custom_delete_selected(modeladmin, request, queryset):
    return delete_selected(modeladmin, request, queryset)

custom_delete_selected.icon = "fas fa-trash"
custom_delete_selected.classes = "btn-danger"

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ("title", "preview_image", "campaign", "order", "active", "created_at", "actions_row")
    list_editable = ("order", "active")
    list_filter = ("active", "campaign")
    search_fields = ("title", "subtitle")
    ordering = ("order",)
    actions = [custom_delete_selected]

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def actions_row(self, obj):
        edit_url = reverse('admin:core_banner_change', args=[obj.pk])
        delete_url = reverse('admin:core_banner_delete', args=[obj.pk])
        return format_html(
            '<a class="btn btn-sm btn-info" style="width: 32px !important; height: 32px !important; min-height: 32px !important; padding: 0 !important; display: inline-flex !important; align-items: center; justify-content: center; border-radius: 6px; margin-right: 4px;" href="{}" title="Editar">'
            '<i class="fas fa-pencil-alt"></i>'
            '</a>'
            '<a class="btn btn-sm btn-danger" style="width: 32px !important; height: 32px !important; min-height: 32px !important; padding: 0 !important; display: inline-flex !important; align-items: center; justify-content: center; border-radius: 6px;" href="{}" title="Excluir">'
            '<i class="fas fa-trash"></i>'
            '</a>',
            edit_url, delete_url
        )
    actions_row.short_description = "Ações"

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name == 'text_color':
            kwargs['widget'] = TextInput(attrs={'type': 'color', 'style': 'height: 40px; width: 60px; padding: 0; cursor: pointer;'})
        return super().formfield_for_dbfield(db_field, request, **kwargs)

    fieldsets = (
        ("📝 Conteúdo do Banner", {
            "description": (
                "Selecione uma campanha se este banner for exclusivo. O título e o subtítulo serão sobrepostos à imagem no lado esquerdo. "
                "Caso não haja título, a imagem inteira se torna o link."
            ),
            "fields": ("campaign", "title", "subtitle", "text_color"),
        }),
        ("🖼️ Imagens do Hero", {
            "description": mark_safe(
                '<div style="display: flex; gap: 20px; flex-wrap: wrap; margin-bottom: 12px;">'
                
                '<!-- DESKTOP BOX -->'
                '<div style="flex: 1; min-width: 300px; background: rgba(217, 119, 6, 0.1); '
                'border: 1px solid #D97706; border-radius: 8px; padding: 16px 20px; font-size: 13px; line-height: 1.7;">'
                '<strong style="font-size:14px; color:#D97706;">💻 Imagem Principal (Desktop)</strong><br>'
                '<table style="margin-top:10px; border-collapse:collapse; width:100%;">'
                '<tr><td style="padding:4px 12px 4px 0; font-weight:600; width:100px;">Tamanho</td><td>1920 × 580 px</td></tr>'
                '<tr><td style="padding:4px 12px 4px 0; font-weight:600;">Proporção</td><td>16:5 (horizontal larga)</td></tr>'
                '</table>'
                '<hr style="border:none; border-top:1px solid rgba(217, 119, 6, 0.3); margin: 12px 0;">'
                '<strong style="color:#D97706;">⚠️ Zona de Texto</strong><br>'
                '<div style="margin-top:8px; position:relative; background:rgba(0,0,0,0.1); border-radius:6px; height:60px; overflow:hidden; border:1px solid rgba(217, 119, 6, 0.3);">'
                '<div style="position:absolute; left:0; top:0; width:55%; height:100%; background:rgba(217, 119, 6, 0.7); display:flex; align-items:center; justify-content:center; flex-direction:column; gap:4px;">'
                '<span style="color:#fff; font-size:11px; font-weight:700; letter-spacing:1px; text-shadow: 1px 1px 2px rgba(0,0,0,0.4);">TEXTO (ESQUERDA)</span>'
                '</div>'
                '<div style="position:absolute; right:0; top:0; width:45%; height:100%; display:flex; align-items:center; justify-content:center;">'
                '<span style="font-size:11px; font-weight:600; text-align:center;">✅ IMAGEM (DIREITA)</span>'
                '</div>'
                '</div>'
                '</div>'

                '<!-- MOBILE BOX -->'
                '<div style="flex: 1; min-width: 300px; background: rgba(2, 132, 199, 0.1); '
                'border: 1px solid #0284C7; border-radius: 8px; padding: 16px 20px; font-size: 13px; line-height: 1.7;">'
                '<strong style="font-size:14px; color:#0284C7;">📱 Imagem Específica (Mobile)</strong><br>'
                '<table style="margin-top:10px; border-collapse:collapse; width:100%;">'
                '<tr><td style="padding:4px 12px 4px 0; font-weight:600; width:100px;">Tamanho</td><td>800 × 1000 px</td></tr>'
                '<tr><td style="padding:4px 12px 4px 0; font-weight:600;">Proporção</td><td>4:5 (vertical / retrato)</td></tr>'
                '</table>'
                '<hr style="border:none; border-top:1px solid rgba(2, 132, 199, 0.3); margin: 12px 0;">'
                '<strong style="color:#0284C7;">⚠️ Zona de Texto</strong><br>'
                '<div style="margin-top:8px; position:relative; background:rgba(0,0,0,0.1); border-radius:6px; height:60px; overflow:hidden; border:1px solid rgba(2, 132, 199, 0.3);">'
                '<div style="position:absolute; left:0; top:0; width:100%; height:100%; background:rgba(2, 132, 199, 0.7); display:flex; align-items:center; justify-content:center; flex-direction:column; gap:4px;">'
                '<span style="color:#fff; font-size:11px; font-weight:700; letter-spacing:1px; text-shadow: 1px 1px 2px rgba(0,0,0,0.4);">TEXTO CENTRALIZADO</span>'
                '<span style="color:rgba(255,255,255,0.9); font-size:10px; text-shadow: 1px 1px 2px rgba(0,0,0,0.4);">Cobre a imagem. Garanta contraste.</span>'
                '</div>'
                '</div>'
                '</div>'

                '</div>'
            ),
            "fields": ("image", "mobile_image"),
        }),
        ("🔗 Botão de Ação (CTA)", {
            "description": "Configure o link e o texto do botão que aparece sobre o banner. Deixe em branco para omitir o botão.",
            "fields": ("link", "link_text"),
        }),
        ("⚙️ Configurações de Exibição", {
            "fields": ("active", "order"),
        }),
    )

    def preview_image(self, obj):
        if obj.image:
            return format_html(
                '<div style="position:relative; display:inline-block;">'
                '<img src="{}" style="height:120px; width:200px; border-radius:6px; '
                'object-fit:cover; display:block;" />'
                '<div style="position:absolute; left:0; top:0; width:55%; height:100%; '
                'background:rgba(17,17,24,0.65); border-radius:6px 0 0 6px; '
                'display:flex; align-items:center; justify-content:center;">'
                '<span style="color:#F5A623; font-size:9px; font-weight:700; '
                'letter-spacing:0.5px; text-align:center; padding:4px;">TEXTO<br>AQUI</span>'
                '</div>'
                '</div>',
                obj.image.url,
            )
        return mark_safe(
            '<span style="color:#9CA3AF; font-style:italic;">Sem imagem</span>'
        )
    preview_image.short_description = "Preview (zona de texto)"


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "city", "rating_stars", "active", "created_at")
    list_editable = ("active",)
    list_filter = ("active", "rating")
    search_fields = ("name", "text")

    def rating_stars(self, obj):
        stars = "⭐" * obj.rating
        return format_html("<span>{}</span>", stars)
    rating_stars.short_description = "Avaliação"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "icon", "order")
    list_editable = ("order",)
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)
    fieldsets = (
        ("Informações Básicas", {
            "fields": ("name", "slug", "icon", "order")
        }),
        ("SEO (Otimização de Busca)", {
            "fields": ("meta_title", "meta_description"),
            "classes": ("collapse",),
            "description": "Preencha para personalizar como esta categoria aparece nos resultados do Google."
        }),
    )


from .models import Banner, Category, Product, Testimonial, ProductImage, Marca

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    max_num = 5
    fields = ('image', 'order')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name", "category", "price_display", "is_featured",
        "is_promotion", "active", "updated_at"
    )
    list_editable = ("is_featured", "is_promotion", "active")
    list_filter = ("active", "is_featured", "is_promotion", "category")
    search_fields = ("name", "description")
    autocomplete_fields = ("category",)
    prepopulated_fields = {"slug": ("name",)}
    inlines = [ProductImageInline]
    fieldsets = (
        ("Informações do Produto", {
            "fields": ("name", "slug", "category", "description", "image")
        }),
        ("Preços", {
            "fields": ("price", "promotional_price", "unit"),
        }),
        ("Configurações de Exibição", {
            "fields": ("is_featured", "is_promotion", "active"),
            "classes": ("collapse",),
        }),
    )

    def price_display(self, obj):
        if obj.promotional_price:
            return format_html(
                '<span style="text-decoration:line-through;color:#888;">R$ {}</span> '
                '<strong style="color:#f59e0b;">R$ {}</strong>',
                obj.price or "—",
                obj.promotional_price,
            )
        if obj.price:
            return format_html("R$ {}", obj.price)
        return mark_safe('<em style="color:#888;">Consulte-nos</em>')
    price_display.short_description = "Preço"

class BannerInline(admin.TabularInline):
    model = Banner
    extra = 1
    fields = ('image', 'mobile_image', 'title', 'link', 'order', 'active')
    show_change_link = True

@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ("name", "active", "featured_title", "created_at")
    list_editable = ("active",)
    list_filter = ("active",)
    search_fields = ("name", "featured_title")
    filter_horizontal = ("products",)
    inlines = [BannerInline]
    fieldsets = (
        ("Configurações Gerais", {
            "fields": ("name", "active")
        }),
        ("Textos da Área de Destaque", {
            "fields": ("featured_title", "featured_subtitle"),
            "description": "Estes textos substituirão os textos padrão da área de produtos em destaque na Home."
        }),
        ("Produtos em Destaque", {
            "fields": ("products",),
            "description": "Selecione os produtos que devem aparecer em destaque para esta campanha. (Se nenhum produto for selecionado, a área ficará vazia)."
        }),
    )

@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ("name", "logo_preview", "active", "order")
    list_editable = ("active", "order")
    list_filter = ("active",)
    search_fields = ("name",)
    
    def logo_preview(self, obj):
        if obj.logo:
            return format_html('<img src="{}" style="height:40px; border-radius:4px;" />', obj.logo.url)
        return "-"
    logo_preview.short_description = "Preview"
