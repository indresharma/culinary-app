from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from core.models import Ingredients, Tags, Recipe

def sample_user(user='test@test.com', password='testpass'):
    user = get_user_model().objects.create_user(email=email, password=password)

class RecipeTests(TestCase):
    pass
