import random

from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, TemplateView, View, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from core.models import Ingredients, Tags, Recipe


@login_required
def create_recipe(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        tags = request.POST.getlist('tag')
        ingredients = request.POST.getlist('ingredient')
        image = request.FILES.get('image')

        form = Recipe.objects.create(title=title, description=description, user=request.user, image=image)
        form.save()
        if tags:
            for tag in tags:
                tg, created = Tags.objects.get_or_create(name=tag, user=request.user)
                form.tags.add(tg)
            
        if ingredients:
            for ingredient in ingredients:
                ing, created = Ingredients.objects.get_or_create(name=ingredient, user=request.user)
                form.ingredients.add(ing)
        form.save()
        return redirect('core:detail', form.id)
    return render(request, 'core/recipe_form.html')
            

class RecipeDetailView(DetailView):
    model = Recipe


class RecipeUpdateView(LoginRequiredMixin, UpdateView):
    model = Recipe
    fields = ('title', 'tags', 'ingredients', 'description', 'image')


class RecipeDeleteView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        obj = Recipe.objects.get(pk=self.kwargs['pk'])
        return render(request, 'core/recipe_confirm_delete.html', {'obj':obj})
    

    def post(self, request, *args, **kwargs):
        obj = Recipe.objects.get(pk=self.kwargs['pk'])
        if obj.user == request.user:
            obj.delete()
            return redirect('core:recipes')
        else:
            messages.error(request, 'You are not authorized to delete this post')
            return redirect('core:recipes')
        
   
class RecipeListView(View):
    def get(self, request, *args, **kwargs):
        queryset = Recipe.objects.all()
        random_obj = random.choices(queryset)[0]
        return render(request, 'core/recipe_list.html', {'queryset': queryset, 'random_obj': random_obj})
    





    




