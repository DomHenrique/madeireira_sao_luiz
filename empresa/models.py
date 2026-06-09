from django.db import models

class Unidade(models.Model):
    """
    Representa uma loja (matriz, filial) da empresa.
    Usado para exibir os locais no mapa e contatos no rodapé.
    """
    TIPO_CHOICES = (
        ('matriz', 'Matriz'),
        ('filial', 'Filial'),
    )

    nome = models.CharField("Nome da Unidade", max_length=100)
    tipo = models.CharField("Tipo", max_length=10, choices=TIPO_CHOICES, default='filial')
    
    # Textos de apresentação da UI (opcional para manter a coerência visual atual)
    title_eyebrow = models.CharField("Texto de Apoio (Eyebrow)", max_length=100, default="NOSSA LOCALIZAÇÃO", blank=True)
    title_main = models.CharField("Título Principal", max_length=150, default="ONDE NOS ENCONTRAR EM PORTO ALEGRE", blank=True)
    card_title = models.CharField("Título do Card", max_length=100, default="VENHA TOMAR UM CAFÉ COM A GENTE!", blank=True)
    
    # Dados de endereço e contato
    endereco = models.CharField("Endereço (Rua, Número, Bairro)", max_length=255)
    cidade = models.CharField("Cidade", max_length=100)
    estado = models.CharField("Estado (UF)", max_length=2, default="RS")
    cep = models.CharField("CEP", max_length=20, blank=True)
    
    email = models.EmailField("E-mail de Contato", blank=True)
    telefone = models.CharField("Telefone", max_length=20, blank=True)
    whatsapp = models.CharField("WhatsApp", max_length=20, blank=True)
    
    business_hours = models.TextField("Horários de Funcionamento", blank=True, help_text="Ex: Seg a Qui: 09h às 19:30h")
    
    # Mapas
    mapa_url = models.URLField("URL de Incorporação do Google Maps (Iframe)", max_length=500, blank=True)
    rota_url = models.URLField("URL de Rota do Google Maps", max_length=500, blank=True)
    
    # Ordenação e exibição
    ordem = models.IntegerField("Ordem de exibição", default=0)
    is_active = models.BooleanField("Ativa", default=True)

    class Meta:
        verbose_name = "Unidade"
        verbose_name_plural = "Unidades"
        ordering = ['ordem', 'nome']

    def __str__(self):
        return f"{self.nome} ({self.get_tipo_display()})"
