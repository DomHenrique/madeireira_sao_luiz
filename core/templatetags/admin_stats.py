from django import template
from core.models import Product, Category, Banner

register = template.Library()

@register.simple_tag
def get_dashboard_stats():
    return {
        'total_products': Product.objects.count(),
        'active_products': Product.objects.filter(active=True).count(),
        'promotions': Product.objects.filter(is_promotion=True).count(),
        'categories': Category.objects.count(),
        'banners': Banner.objects.count()
    }
