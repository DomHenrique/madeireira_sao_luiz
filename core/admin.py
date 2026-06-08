"""
Admin — App Core
Configurado para django-jazzmin com ações e filtros otimizados.
"""

from django.contrib import admin
from django.utils.html import format_html

from .models import Banner, Category, Product, Testimonial


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ("title", "preview_image", "order", "active", "created_at")
    list_editable = ("order", "active")
    list_filter = ("active",)
    search_fields = ("title", "subtitle")
    ordering = ("order",)

    def preview_image(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="height:50px;border-radius:4px;object-fit:cover;" />',
                obj.image.url,
            )
        return "—"
    preview_image.short_description = "Preview"


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
    fieldsets = (
        ("Informações do Produto", {
            "fields": ("name", "category", "description", "image")
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
        return format_html('<em style="color:#888;">Consulte-nos</em>')
    price_display.short_description = "Preço"
