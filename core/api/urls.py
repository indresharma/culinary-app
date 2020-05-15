from rest_framework.routers import DefaultRouter

from django.urls import include, path
from . import views


router = DefaultRouter()
router.register('tags', views.TagViewSet)
router.register('ingredients', views.IngredientViewSet)
router.register('recipes', views.RecipeViewSet)
router.register('comments', views.CommentsViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('wishlist/', views.WishListView.as_view(), name='wishlist-api'),
    path('wishlist/create/', views.CreateOrUpdateWishList.as_view(),
         name='wishlist-create-api'),
    path('wishlist/items/', views.WishListItemsView.as_view(),
         name='wishlist-items-api'),
    path('recipes/<int:pk>/wishlist-toggle/',
         views.WishListToggleView.as_view(), name='wishlist-toggle-api'),
    path('recipes/<int:pk>/add-comment/',
         views.CommentsCreateAPIView.as_view(), name='add-comment-api'),
    path('recipes/<int:recipe_pk>/remove-comment/<int:comment_pk>/',
         views.CommentsDestroyAPIView.as_view(), name='remove-comment-api'),
]
