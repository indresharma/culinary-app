from rest_framework import serializers
from django.core.exceptions import ObjectDoesNotExist

from core.models import Recipe, Tags, RecipeCollection, Ingredients, Comments


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


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'
        read_only_fields = ('id', 'user', 'created', 'recipe')


class RecipeSerializer(serializers.ModelSerializer):
    tags = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Tags.objects.all())
    ingredients = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Ingredients.objects.all())
    image = serializers.SerializerMethodField()

    class Meta:
        model = Recipe
        fields = '__all__'
        read_only_fields = ('id', 'user', 'data_created', 'likes')

    def get_image(self, obj):
        return obj.get_image_url()


class RecipeListSerializer(serializers.ModelSerializer):
    summary = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()
    class Meta:
        model = Recipe
        fields = ('id', 'title', 'user', 'summary', 'data_created', 'image')
        read_only_fields = ('id', 'data_created')

    def get_summary(self, obj):
        return obj.get_summary()

    def get_image(self, obj):
        return obj.get_image_url()


class RecipeDetailSerializer(RecipeSerializer):
    tags = TagSerializer(many=True, read_only=True)
    ingredients = IngredientSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True)

class RecipeImageSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ('id', 'image')
        read_only_fields = ('id',)

        
class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeCollection
        fields = ('id', 'user',)
        read_only_fields = ('id','user')
    
    def create(self, validated_data):
        wishlist, created = RecipeCollection.objects.update_or_create(user=validated_data.get('user'))
        return wishlist


class WishlistDetailSerializer(serializers.ModelSerializer):
    recipe = RecipeListSerializer(many=True)

    class Meta:
        model = RecipeCollection
        fields = ('id', 'recipe',)
        read_only_fields = ('id','recipe')
        




    






