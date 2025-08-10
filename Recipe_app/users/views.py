from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from recipes.models import Recipe

from . import forms
# Create your views here.
def register(request):
    if request.method == "POST":
        form = forms.UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"{username},Your account has been created!, Please login!")
            return redirect('user-login')
    else:
        form = forms.UserRegisterForm()
    return render(request, 'users/register.html',{'form':form})

def logout_user(request):
    logout(request)
    messages.success(request,("You are logged out!"))
    return redirect('receipe-home')

@login_required()
def profile(request):
    user=request.user
    user_recipes = Recipe.objects.filter(author=user)
    return render(request,'users/profile.html',{'user_recipes':user_recipes})