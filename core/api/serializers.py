from rest_framework import serializers

from core.models import Recipe, Tags, RecipeCollection, Ingredients


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ('id', 'name')
        read_only_fields = ('id',)


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        fields = ('id', 'name')
        read_only_fields = ('id',)


class RecipeSerializer(serializers.ModelSerializer):
    tags = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Tags.objects.all())
    ingredients = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Ingredients.objects.all())

    class Meta:
        model = Recipe
        fields = ('id', 'title', 'user', 'tags', 'ingredients', 'description', 'preparation_time', 'calories')
        read_only_fields = ('id',)


class RecipeDetailSerializer(RecipeSerializer):
    tags = TagSerializer(many=True, read_only=True)
    ingredients = IngredientSerializer(many=True, read_only=True)




