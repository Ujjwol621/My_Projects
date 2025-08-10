from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib import messages

from . import models
from . models import Recipe
from datetime import datetime
# Create your views here. 

def home(request):
    recipes = models.Recipe.objects.all()
    current_hour = datetime.now().hour
    if 5 <= current_hour < 12:
        greeting = "Good morning! "
    elif 12 <= current_hour < 18:
        greeting = "Good afternoon !"
    elif 18 <= current_hour < 22:
        greeting = "Good evening !"
    else:
        greeting = "Hello! "

    context={
            'recipes':recipes,
            'greeting':greeting,
            }
    return render(request,"my_receipe/home.html",context)

class RecipeListView(ListView):
    model = models.Recipe
    template_name = "my_receipe/home.html"
    context_object_name = 'recipes'

class RecipeDetailView(DetailView):
    model = models.Recipe
    template_name= "my_receipe/recipe_detail.html"

class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = models.Recipe
    template_name= "my_receipe/recipe_form.html"
    fields = ['title','ingredients','description','photo']

    def form_valid(self,form):
        form.instance.author = self.request.user
        form.instance.photo = self.request.FILES.get('photo')
        return super().form_valid(form)
    
class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Recipe
    template_name= "my_receipe/recipe_form.html"
    fields = ['title','ingredients','description','photo']

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author or self.request.user.is_superuser
    
    def form_valid(self, form):
        # Set the author of the recipe to the current user
        form.instance.author = self.request.user

        # Get the current instance being updated
        recipe_instance = self.get_object()

        # Check if a new photo is uploaded
        if 'photo' in self.request.FILES:
            form.instance.photo = self.request.FILES['photo']
        else:
            # Retain the existing photo if no new photo is uploaded
            form.instance.photo = recipe_instance.photo
    
        messages.success(self.request, 'Recipe updated successfully!')
        return super().form_valid(form)
    
class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Recipe
    template_name= "my_receipe/recipe_confirm_delete.html"
    success_url = reverse_lazy('receipe-home')

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author or self.request.user.is_superuser
    
def recipe_search(request):
    # Get the search query from the request GET parameters
    query = request.GET.get('q')

    # If the query is not empty, perform the search
    if query:
        # Filter recipes based on the search query
        recipes = Recipe.objects.filter(title__icontains=query)
    else:
        # If the query is empty, return all recipes
        recipes = Recipe.objects.all()

    # Render the template with the search results
    return render(request, 'my_receipe/search_recipe.html', {'recipes': recipes, 'query': query})

def about(request):
    return render(request,"my_receipe/about.html",{'title':'about us page'})
