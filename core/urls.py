from django.urls import path
from core import views

app_name = 'core'

urlpatterns = [
    path('', views.RecipeListView.as_view(), name='recipes'),
    path('create-recipe/', views.CreateRecipeView.as_view(), name='create-recipe'),
    path('recipe/<int:pk>/', views.RecipeDetailView.as_view(), name='detail'),
    path('update-recipe/<int:pk>/', views.RecipeUpdateView.as_view(), name='update-recipe'),
    path('delete-recipe/<int:pk>/', views.RecipeDeleteView.as_view(), name='delete-recipe'),
    path('add/<int:pk>/', views.UpdateIngredient.as_view(), name='add-ingredients'),
    path('add-collections/<int:pk>', views.RecipeCollectionsView.as_view(), name='add-to-collections'),
    path('recipe-collection/', views.RecipeCollectionListView.as_view(), name='recipe-collection-list'),
    
]