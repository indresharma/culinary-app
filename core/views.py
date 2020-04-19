import random
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView, View, UpdateView, DeleteView, CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from core.models import Ingredients, Tags, Recipe
from core.forms import RecipeForm


class OwnerOnlyMixin:
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user == request.user:
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponse('Unauthorized', status=401)


class CreateRecipeView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = RecipeForm()
        return render(request, 'core/recipe_form.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = RecipeForm(request.POST)
        if form.is_valid():
            tags = request.POST.getlist('tag')
            ingredients = request.POST.getlist('ingredient')
            recipe = form.save(commit=False)
            recipe.user = request.user
            recipe.save()
            if tags:
                for tag in tags:
                    tg, created = Tags.objects.get_or_create(name=tag, user=request.user)
                    recipe.tags.add(tg)
                
            if ingredients:
                for ingredient in ingredients:
                    ing, created = Ingredients.objects.get_or_create(name=ingredient, user=request.user)
                    recipe.ingredients.add(ing)
            recipe.save()
            return redirect('core:detail', recipe.id)
        return redirect('core:create-recipe')
            

class RecipeDetailView(DetailView):
    model = Recipe


class RecipeUpdateView(LoginRequiredMixin, OwnerOnlyMixin, UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'core/recipe_update_form.html'


class RecipeDeleteView(LoginRequiredMixin, OwnerOnlyMixin, DeleteView):
    model = Recipe
        
   
class RecipeListView(View):
    def get(self, request, *args, **kwargs):
        queryset = Recipe.objects.all()
        random_obj = random.choices(queryset)[0]
        return render(request, 'core/recipe_list.html', {'queryset': queryset, 'random_obj': random_obj})
    
# class UpdateTagView(View):
#     def post(self, request, *args, **kwargs):
#         recipe = get_object_or_404(Recipe, pk=self.pk)
#         tag = 






    




