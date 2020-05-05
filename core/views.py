import random
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView, View, UpdateView, DeleteView, CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist

from core.models import Ingredients, Tags, Recipe
from core.forms import RecipeForm
from users.views import OwnerOnlyMixin

def add_ingredient_to_recipe(user, recipe, ingredient_list):
    """Helper function to add ingredients to recipe"""
    for ingredient in ingredient_list:
        if ingredient:
            try: 
                ing = Ingredients.objects.get(name=ingredient)
            except ObjectDoesNotExist:
                ing = Ingredients.objects.create(name=ingredient, user=user)
            recipe.ingredients.add(ing)
            recipe.save()
    return recipe

def add_tag_to_recipe(user, recipe, tag_list):
    """Helper function to add tags to recipe"""
    for tag in tag_list:
        if tag:
            try:
                tg = Tags.objects.get(name=tag)
            except ObjectDoesNotExist:
                tg = Tags.objects.create(name=tag, user=user)
            recipe.tags.add(tg)
            recipe.save()
    return recipe

class CreateRecipeView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = RecipeForm()
        return render(request, 'core/recipe_form.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = RecipeForm(request.POST)
        if form.is_valid():
            tag_list = request.POST.getlist('tag')
            ingredient_list = request.POST.getlist('ingredient')
            recipe = form.save(commit=False)
            recipe.user = request.user
            recipe.save()
            # if tags:
            add_tag_to_recipe(request.user, recipe, tag_list)

            # if ingredients:
            add_ingredient_to_recipe(request.user, recipe, ingredient_list)
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
        if queryset:
            random_obj = random.choices(queryset)[0]
            query = request.GET.get('search')
            if query:
                queryset = queryset.filter(
                    Q(tags__name__icontains=query) | Q(ingredients__name__icontains=query) | Q(title__icontains=query)
                ).distinct()
            return render(request, 'core/recipe_list.html', {'queryset': queryset, 'random_obj': random_obj})
        else:
            return HttpResponse('No Items Found', status=404)


class UpdateIngredient(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, 'core/add.html')

    def post(self, request, *args, **kwargs):
        recipe = get_object_or_404(Recipe, pk=kwargs['pk'])
        if recipe.user==self.request.user:
            ingredient_list = request.POST.getlist('ingredient')
            add_ingredient_to_recipe(request.user, recipe, ingredient_list)
        return redirect('core:detail', pk=recipe.pk)


    
