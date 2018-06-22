from django.shortcuts import render
from django.views.generic import ListView

from .models import Product, ProductImage


class ProductListView(ListView):
    model = Product

