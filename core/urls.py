from django.urls import path
from core import views

app_name = 'core'

urlpatterns = [
    path('', views.TemplateView.as_view(template_name='core/home.html'), name='home'),
    path('create-recipe/', views.create_recipe, name='create-recipe'),
    path('recipe/<int:pk>/', views.RecipeDetailView.as_view(), name='detail'),
    path('update-recipe/<int:pk>/', views.RecipeUpdateView.as_view(), name='update-recipe'),
    path('recipes/', views.RecipeListView.as_view(), name='recipes'),
    path('delete-recipe/<int:pk>/', views.RecipeDeleteView.as_view(), name='delete-recipe'),
    
]