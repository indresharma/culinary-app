from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication
from rest_framework import generics
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404


from .serializers import (
    TagSerializer, 
    IngredientSerializer, 
    RecipeSerializer, 
    RecipeDetailSerializer, 
    WishlistSerializer,
    WishlistDetailSerializer,
    CommentSerializer)
from ..models import Tags, Ingredients, Recipe, RecipeCollection, Comments
from .permissions import IsOwnerOrReadOnly


class BaseAttrViewSet(ListModelMixin, CreateModelMixin, GenericViewSet):
    authentication_classes = [SessionAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        if serializer.is_valid():
            obj = serializer.validated_data.get('name')
            qs = self.queryset.filter(name=obj)
            if obj:
                if not qs.exists():
                    serializer.save(user=self.request.user)
                    return Response(serializer.data)
                else:
                    return Response(serializer.data)
            else:
                return Response(data={'message': 'Empty product_name'},
                                status=status.HTTP_400_BAD_REQUEST)


class TagViewSet(BaseAttrViewSet):
    queryset = Tags.objects.all()
    serializer_class = TagSerializer


class IngredientViewSet(BaseAttrViewSet):
    queryset = Ingredients.objects.all()
    serializer_class = IngredientSerializer


class RecipeViewSet(ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return RecipeDetailSerializer
        return self.serializer_class


class WishListView(generics.ListAPIView):
    queryset = RecipeCollection.objects.all()
    serializer_class = WishlistSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class CreateOrUpdateWishList(generics.CreateAPIView):
    queryset = RecipeCollection.objects.all()
    serializer_class = WishlistSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class WishListItemsView(generics.RetrieveAPIView):
    serializer_class = WishlistDetailSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_object(self):
        obj = get_object_or_404(RecipeCollection, user=self.request.user)
        return obj


class WishListToggleView(APIView):
    authentication_classes = [SessionAuthentication, ]
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get(self, request, **kwargs):
        recipe_obj = get_object_or_404(Recipe, pk=self.kwargs.get('pk'))
        wishlist, created = RecipeCollection.objects.get_or_create(user=self.request.user)
        updated = False
        in_wishlist = False
        if recipe_obj in wishlist.recipe.all():
            wishlist.recipe.remove(recipe_obj)
            in_wishlist = False
        else:
            wishlist.recipe.add(recipe_obj)
            in_wishlist = True
        updated = True
        data = {
            "recipe": recipe_obj.pk,
            "updated": updated,
            "in_wishlist": in_wishlist,
        }
        return Response(data)


class CommentsViewSet(ListModelMixin, CreateModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_queryset(self):
        return self.queryset.filter(recipe=self.kwargs.get('pk'))    

    

class CommentsCreateAPIView(generics.ListCreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_queryset(self):
        return self.queryset.filter(recipe=self.kwargs.get('pk'))  

    def perform_create(self, serializer):
        recipe = get_object_or_404(Recipe, pk=self.kwargs.get('pk'))
        serializer.save(user=self.request.user, recipe=recipe)


class CommentsDestroyAPIView(generics.DestroyAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_object(self):
        obj = get_object_or_404(Comments, pk=self.kwargs.get('comment_pk'))
        return obj

 





    



    
            
        



    