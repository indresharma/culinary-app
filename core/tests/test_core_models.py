from django.test import TestCase
from django.contrib.auth import get_user_model
from core.models import Recipe, Ingredients, Tags


def sample_user(email='test@test.com', password='testpass'):
    return get_user_model().objects.create_user(email=email, password=password)


class TestModels(TestCase):

    def test_recipe_model(self):
        recipe = Recipe.objects.create(
            user=sample_user(),
            title='Biryani',
            description='Veg Biryani'
        )
        self.assertEqual(str(recipe), recipe.title)

    def test_ingredients_model(self):
        ingredient = Ingredients.objects.create(user=sample_user(), name='Rice')
        self.assertEqual(str(ingredient), ingredient.name)

    def test_tags_model(self):
        tag = Tags.objects.create(user=sample_user(), name='Veg')
        self.assertEqual(str(tag), tag.name)