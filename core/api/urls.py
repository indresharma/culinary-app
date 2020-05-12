from rest_framework.routers import DefaultRouter

from django.urls import include, path
from . import views


router = DefaultRouter()
router.register('tags', views.TagViewSet)
router.register('ingredients', views.IngredientViewSet)
router.register('recipes', views.RecipeViewSet)


urlpatterns = [
    path('', include(router.urls)),
]