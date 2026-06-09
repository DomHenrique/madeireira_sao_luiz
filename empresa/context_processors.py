from .models import Unidade

def empresa_context(request):
    """
    Injeta as unidades da empresa em todos os templates, 
    permitindo o uso dinâmico no cabeçalho e rodapé.
    """
    unidades_ativas = Unidade.objects.filter(is_active=True).order_by('ordem')
    
    # Busca a matriz, ou a primeira filial se não houver matriz
    matriz = unidades_ativas.filter(tipo='matriz').first()
    if not matriz:
        matriz = unidades_ativas.first()
        
    return {
        'matriz': matriz,
        'todas_unidades': unidades_ativas,
    }
