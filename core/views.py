"""Views — App Core"""

from django.shortcuts import get_object_or_404, render

from empresa.models import Unidade
from .models import Banner, Category, Product, Testimonial, Campaign, Marca


def home(request):
    """Página inicial com banners, produtos em destaque e depoimentos."""
    active_campaign = Campaign.objects.filter(active=True).first()

    if active_campaign:
        banners = active_campaign.banners.filter(active=True).order_by("order")
        featured_products = active_campaign.products.filter(active=True)
        featured_title = active_campaign.featured_title
        featured_subtitle = active_campaign.featured_subtitle
    else:
        banners = Banner.objects.filter(active=True, campaign__isnull=True).order_by("order")
        featured_products = Product.objects.filter(active=True, is_featured=True).select_related("category")[:6]
        featured_title = "Produtos em Destaque para Sua Obra"
        featured_subtitle = "Seleção especial de materiais de construção com preços exclusivos na Matcon."

    testimonials = Testimonial.objects.filter(active=True)[:6]
    categories = Category.objects.all()
    unidades = Unidade.objects.filter(is_active=True).order_by("ordem")
    marcas_destaque = Marca.objects.filter(active=True).order_by("order")

    context = {
        "banners": banners,
        "featured_products": featured_products,
        "featured_title": featured_title,
        "featured_subtitle": featured_subtitle,
        "testimonials": testimonials,
        "categories": categories,
        "unidades": unidades,
        "marcas_destaque": marcas_destaque,
    }
    return render(request, "core/home.html", context)


def products(request, slug=None):
    """Listagem completa de produtos com filtro por categoria."""
    category_slug = slug or request.GET.get("categoria")
    all_categories = Category.objects.all()

    qs = Product.objects.filter(active=True).select_related("category")
    active_category = None

    if category_slug:
        active_category = get_object_or_404(Category, slug=category_slug)
        qs = qs.filter(category=active_category)

    context = {
        "products": qs,
        "categories": all_categories,
        "active_category": active_category,
    }
    return render(request, "core/products.html", context)


def product_detail(request, slug):
    """Página de detalhes de um único produto, com galeria de imagens."""
    product = get_object_or_404(Product.objects.select_related("category").prefetch_related("gallery_images"), slug=slug, active=True)
    
    # Produtos relacionados da mesma categoria (excluindo o atual)
    related_products = []
    if product.category:
        related_products = Product.objects.filter(
            category=product.category, 
            active=True
        ).exclude(id=product.id)[:4]

    context = {
        "product": product,
        "related_products": related_products,
    }
    return render(request, "core/product_detail.html", context)


def about_us(request):
    """Página institucional Sobre Nós, com mapa e contatos."""
    return render(request, "core/about_us.html")
