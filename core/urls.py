"""URLs — App Core"""

from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path("produtos/", views.products, name="products"),
    path("produtos/categoria/<slug:slug>/", views.products, name="category_products"),
]
