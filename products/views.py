from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from .models import *
from .forms import *

class ProductListView(ListView):
    model = Product
    template_name = 'products/list_product.html'
    paginate_by = 10


class ProductCreateView(CreateView):
    form_class = ProductForm
    template_name = 'products/add_product.html'
    success_url = 'products'

class ProductUpdateView(UpdateView):
    form_class = ProductForm
    template_name = 'products/add_product.html'
    success_url = 'products'



