from .models import Category

def global_categories(request):
    """
    Disponibiliza as categorias no contexto de todos os templates,
    útil para montagem dinâmica de rodapés e menus de navegação.
    """
    return {
        'footer_categories': Category.objects.all().order_by('order')[:6]
    }
