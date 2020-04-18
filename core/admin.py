from django.contrib import admin
from core.models import Ingredients, Recipe, Tags
from user.models import UserModel, Profile

# Register your models here.

admin.site.register(UserModel)
admin.site.register(Ingredients)
admin.site.register(Tags)
admin.site.register(Recipe)
admin.site.register(Profile)
