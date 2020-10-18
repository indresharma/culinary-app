from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView, View
from django.views.generic.edit import ModelFormMixin
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

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


class ProductCreateView(CustomAuthMixin, SuccessMessageMixin, CreateView):
    permission_required = ['products.add_product']
    form_class = ProductForm
    template_name = 'products/add_product.html'
    success_url = reverse_lazy('products:add-products')
    success_message = 'Product added Successfully'


class ProductUpdateView(CustomAuthMixin, SuccessMessageMixin, UpdateView):
    permission_required = ['products.change_product']
    model = Product
    form_class = ProductForm
    template_name = 'products/add_product.html'
    success_url = reverse_lazy('products:dashboard-products-list')
    success_message = 'Product updated Successfully'


class ProductDeleteView(CustomAuthMixin, DeleteView):
    permission_required = ['products.change_product']
    model = Product
    success_message = 'Product deleted Successfully'

    def delete(self, request, *args, **kwargs):
        self.get_object().delete()
        messages.success(request, self.success_message)
        payload = {'status': True, 'message': 'Deleted'}
        return JsonResponse(payload)


#################### Dashboard Views #################################
class DashboardView(TemplateView):
    template_name = 'products/dashboard.html'


class DashboardProductListView(ProductListView):
    template_name = 'products/dashboard_products_list.html'
    paginate_by = 10


