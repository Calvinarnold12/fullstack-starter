from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import PlayerProfile

def hello_world(request):
    return render(request, "hello/hello_world.html")

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create the linked PlayerProfile for our stats
            PlayerProfile.objects.create(user=user)
            login(request, user)
            return redirect('hello') # Send them to the main page
    else:
        form = UserCreationForm()
    
    return render(request, "hello/register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('hello')
    else:
        form = AuthenticationForm()
        
    return render(request, "hello/login.html", {"form": form})