from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Ingredients, Recipe, Tags, RecipeCollection, Comments

# Register your models here.

class RecipeAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)

admin.site.register(Ingredients)
admin.site.register(Tags)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeCollection)
admin.site.register(Comments)

