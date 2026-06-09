from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Category, Product

class StaticViewSitemap(Sitemap):
    priority = 1.0
    changefreq = 'daily'

    def items(self):
        return ['core:home', 'core:products']

    def location(self, item):
        return reverse(item)

class CategorySitemap(Sitemap):
    priority = 0.8
    changefreq = 'weekly'

    def items(self):
        return Category.objects.all()

    # location() is inferred from get_absolute_url() on Category model
