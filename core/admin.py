from django.contrib import admin
from core.models import Ingredients, Recipe, Tags

# Register your models here.

admin.site.register(Ingredients)
admin.site.register(Tags)
admin.site.register(Recipe)

