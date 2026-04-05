from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import PlayerProfile

# --- NEW: Serve the root index.html ---
def index_view(request):
    return render(request, "hello/index.html", {"message": "Welcome to our CS 408 Project!"})

# --- Existing Views ---
def hello_world(request):
    return render(request, "hello/hello_world.html")

def register_view(request):
    # ... (Keep your existing register code here)
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            PlayerProfile.objects.create(user=user)
            login(request, user)
            return redirect('hello')
    else:
        form = UserCreationForm()
    return render(request, "hello/register.html", {"form": form})

def login_view(request):
    # ... (Keep your existing login code here)
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('hello')
    else:
        form = AuthenticationForm()
    return render(request, "hello/login.html", {"form": form})
def logout_view(request):
    logout(request) # This destroys the session
    return redirect('home')