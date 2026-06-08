"""Views — App Core"""

from django.shortcuts import get_object_or_404, render

from .models import Banner, Category, Product, Testimonial


def home(request):
    """Página inicial com banners, produtos em destaque e depoimentos."""
    banners = Banner.objects.filter(active=True).order_by("order")
    featured_products = Product.objects.filter(active=True, is_featured=True).select_related("category")[:6]
    testimonials = Testimonial.objects.filter(active=True)[:6]
    categories = Category.objects.all()

    context = {
        "banners": banners,
        "featured_products": featured_products,
        "testimonials": testimonials,
        "categories": categories,
    }
    return render(request, "core/home.html", context)


def products(request):
    """Listagem completa de produtos com filtro por categoria."""
    category_slug = request.GET.get("categoria")
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
