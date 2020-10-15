from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from .models import *
from .forms import *

class CustomAuthMixin(LoginRequiredMixin, PermissionRequiredMixin):
    permission_required = []

class ProductListView(ListView):
    model = Product
    template_name = 'products/list_product.html'
    paginate_by = 10

    def get_queryset(self):
        return Product.objects.all().order_by('-id')


class ProductCreateView(CustomAuthMixin, CreateView):
    permission_required = ['products.add_product']
    form_class = ProductForm
    template_name = 'products/add_product.html'
    success_url = reverse_lazy('products:products')

class ProductUpdateView(CustomAuthMixin, UpdateView):
    permission_required = ['products.change_product']
    model = Product
    form_class = ProductForm
    template_name = 'products/add_product.html'
    success_url = reverse_lazy('products:products')


#################### Dashboard Views #################################
class DashboardView(TemplateView):
    template_name = 'products/dashboard.html'

class DashboardProductListView(ProductListView):
    template_name = 'products/dashboard_products_list.html'
    paginate_by = 10







