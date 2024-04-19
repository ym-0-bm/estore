from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView


# Create your views here.


def index(request):
    return render(request, 'base.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirige vers la page de connexion après l'inscription réussie
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
