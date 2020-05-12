from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication


from .serializers import TagSerializer, IngredientSerializer, RecipeSerializer, RecipeDetailSerializer
from ..models import Tags, Ingredients, Recipe
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

