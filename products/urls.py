from django.urls import path


from .views import *

app_name = 'products'

urlpatterns = [
    path('products/', ProductListView.as_view(), name="products"),
    path('products/add/', ProductCreateView.as_view(), name="add-products"),
    path('products/update/<int:pk>/', ProductUpdateView.as_view(), name="update-products"),

]