"""
Modelos de dados — App Core
Madereira São Luiz
"""

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse


from django.core.exceptions import ValidationError

class Banner(models.Model):
    """
    Carrossel rotativo da página inicial.
    As imagens são armazenadas no Supabase Storage (em produção)
    ou localmente em media/ (em desenvolvimento).
    """
    title = models.CharField(
        "Título",
        max_length=200,
        blank=True,
        null=True,
        help_text=(
            "Opcional. Se não for preenchido, o link do banner será obrigatório, "
            "e toda a imagem será clicável."
        ),
    )
    subtitle = models.CharField(
        "Subtítulo",
        max_length=300,
        blank=True,
        help_text=(
            "Texto complementar ao título — máximo 2 linhas. "
            "Será exibido abaixo do título, ainda sobre a imagem."
        ),
    )
    text_color = models.CharField(
        "Cor do Texto",
        max_length=7,
        default="#FFFFFF",
        help_text="Código HEX da cor do texto (ex: #FFFFFF para branco, #000000 para preto, #FF0000 para vermelho).",
    )
    image = models.ImageField(
        "Imagem do Banner",
        upload_to="banners/",
        help_text=(
            "📐 TAMANHO RECOMENDADO: 1920 × 580 px (proporção 16:5 — paisagem bem larga). "
            "📏 MÍNIMO ACEITÁVEL: 1280 × 400 px. "
            "🗂️ FORMATOS: JPG ou WebP (PNG aceito, mas gera arquivo maior). "
            "⚠️ ZONA SEGURA DE TEXTO: os textos (Título, Subtítulo e Botão) "
            "aparecem na metade ESQUERDA da imagem, com overlay escuro. "
            "Evite colocar elementos importantes (rosto, logotipo, produto) "
            "nos primeiros 55% da largura a partir da esquerda — "
            "eles ficarão cobertos pelo texto. "
            "Prefira imagens com o assunto principal centralizado ou no lado DIREITO. "
            "Em mobile, o texto é centralizado e cobre maior parte da tela, "
            "então garanta contraste em toda a imagem."
        ),
    )
    link = models.URLField("Link (CTA)", blank=True, help_text="URL para onde o banner levará. Obrigatório se não houver Título.")
    link_text = models.CharField("Texto do Botão", max_length=80, default="Saiba Mais", blank=True, help_text="Se o título estiver vazio, este botão será ignorado e toda a imagem será clicável.")
    active = models.BooleanField("Ativo", default=True)
    order = models.PositiveIntegerField("Ordem", default=0, help_text="Banners com menor número aparecem primeiro")
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        super().clean()
        if not self.title and not self.link:
            raise ValidationError({
                'link': 'O link é OBRIGATÓRIO quando o banner não possui um título.'
            })

    class Meta:
        verbose_name = "Banner"
        verbose_name_plural = "Banners"
        ordering = ["order", "-created_at"]

    def __str__(self):
        return self.title if self.title else f"Banner Clicável (Sem Título) #{self.pk}"


class Testimonial(models.Model):
    """Depoimentos de clientes exibidos na página inicial."""

    RATING_CHOICES = [(i, f"{i} estrela{'s' if i > 1 else ''}") for i in range(1, 6)]

    name = models.CharField("Nome do Cliente", max_length=150)
    city = models.CharField("Cidade", max_length=100, blank=True)
    text = models.TextField("Depoimento")
    rating = models.PositiveSmallIntegerField(
        "Avaliação",
        choices=RATING_CHOICES,
        default=5,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
    )
    photo = models.ImageField("Foto do Cliente", upload_to="testimonials/", blank=True)
    active = models.BooleanField("Ativo", default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Depoimento"
        verbose_name_plural = "Depoimentos"
        ordering = ["-rating", "-created_at"]

    def __str__(self):
        return f"{self.name} ({self.get_rating_display()})"

    @property
    def stars_filled(self):
        """Retorna range para renderizar estrelas preenchidas no template."""
        return range(self.rating)

    @property
    def stars_empty(self):
        """Retorna range para renderizar estrelas vazias no template."""
        return range(5 - self.rating)


class Category(models.Model):
    """Categorias de produtos (ex.: Madeira Bruta, Beneficiada, Acessórios)."""

    name = models.CharField("Nome", max_length=100)
    slug = models.SlugField("Slug", unique=True)
    icon = models.CharField(
        "Ícone Bootstrap", max_length=60, blank=True,
        help_text="Ex.: bi-tree-fill (Bootstrap Icons)"
    )
    order = models.PositiveIntegerField("Ordem", default=0)
    meta_title = models.CharField("Meta Title (SEO)", max_length=150, blank=True, help_text="Título para o Google. Se vazio, usará o nome da categoria.")
    meta_description = models.TextField("Meta Description (SEO)", blank=True, help_text="Resumo para o Google (recomendado ~150 caracteres).")

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ["order", "name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("core:category_products", kwargs={"slug": self.slug})


class Product(models.Model):
    """
    Produtos da madereira.
    is_featured = True → aparece na seção de Destaques/Promoções da Home.
    As imagens são gerenciadas pelo Supabase Storage em produção.
    """

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="products",
        verbose_name="Categoria",
    )
    name = models.CharField("Nome do Produto", max_length=200)
    slug = models.SlugField("Slug", unique=True, null=True, blank=True)
    description = models.TextField("Descrição")
    price = models.DecimalField(
        "Preço (R$)", max_digits=10, decimal_places=2,
        null=True, blank=True, help_text="Deixe em branco para 'Consulte-nos'"
    )
    promotional_price = models.DecimalField(
        "Preço Promocional (R$)", max_digits=10, decimal_places=2,
        null=True, blank=True,
    )
    image = models.ImageField("Imagem Principal", upload_to="products/")
    unit = models.CharField(
        "Unidade de Medida", max_length=30, default="m²",
        help_text="Ex.: m², m³, un, dúzia"
    )
    is_featured = models.BooleanField(
        "Produto em Destaque",
        default=False,
        help_text="Marque para exibir na seção de destaques/promoções da Home"
    )
    is_promotion = models.BooleanField(
        "Em Promoção",
        default=False,
        help_text="Exibe badge de PROMOÇÃO no card do produto"
    )
    active = models.BooleanField("Ativo", default=True)
    meta_title = models.CharField("Meta Title (SEO)", max_length=150, blank=True, help_text="Título para o Google (caso tenha página própria no futuro).")
    meta_description = models.TextField("Meta Description (SEO)", blank=True, help_text="Resumo para o Google.")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ["-is_featured", "-created_at"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse
        if self.slug:
            return reverse('core:product_detail', kwargs={'slug': self.slug})
        return "#"

    @property
    def display_price(self):
        """Retorna o preço formatado para exibição."""
        if self.promotional_price:
            return self.promotional_price
        return self.price

    @property
    def has_discount(self):
        return bool(self.price and self.promotional_price and self.promotional_price < self.price)

    @property
    def discount_percentage(self):
        if self.has_discount:
            return int((1 - self.promotional_price / self.price) * 100)
        return 0


class ProductImage(models.Model):
    """
    Imagens adicionais do produto (Galeria).
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="gallery_images", verbose_name="Produto")
    image = models.ImageField("Imagem Extra", upload_to="products/gallery/")
    order = models.PositiveIntegerField("Ordem", default=0)

    class Meta:
        verbose_name = "Imagem da Galeria"
        verbose_name_plural = "Imagens da Galeria"
        ordering = ["order"]

    def __str__(self):
        return f"Imagem Extra de {self.product.name}"
