from django.shortcuts import render, redirect    
from django.contrib.auth.decorators import login_required    
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm    
from django.contrib.auth import login, authenticate    
from django.contrib import messages    
from .models import Player    
from rest_framework import viewsets    
from api.serializers import PlayerSerializer
from django.contrib.auth import logout



def register_view(request):    
    if request.method == 'POST':    
        form = UserCreationForm(request.POST)    
        if form.is_valid():    
            # Crea el usuario
            user = form.save()    
            if not Player.objects.filter(user=user).exists():
                Player.objects.create(user=user)    
               
            username = form.cleaned_data.get('username')    
            raw_password = form.cleaned_data.get('password1')    
            user = authenticate(username=username, password=raw_password)    
            login(request, user)    
            messages.success(request, '¡Cuenta creada exitosamente!')    
            return redirect('home')    
        else:    
            messages.error(request, 'Error en el formulario. Por favor, corrige los errores.')    
    else:    
        form = UserCreationForm()    
    return render(request, 'players/register.html', {'form': form})

@login_required
def custom_redirect(request):
    if request.user.is_superuser:
        return redirect('/admin/')  # URL del Django Admin
    else:
        return redirect('/')  # URL para usuarios normales
    
def logout_view(request):
    logout(request)
    messages.success(request, '¡Has cerrado sesión exitosamente!')
    return redirect('login')  

def login_view(request):    
    if request.method == 'POST':    
        form = AuthenticationForm(request, data=request.POST)    
        if form.is_valid():    
            username = form.cleaned_data.get('username')    
            password = form.cleaned_data.get('password')    
            user = authenticate(username=username, password=password)    
            if user is not None:    
                login(request, user)
                messages.success(request, f'Bienvenido {username}!')
                return redirect('custom_redirect')  # Redirige al custom_redirect
                
        else:    
            messages.error(request, 'Usuario o contraseña incorrectos.')    
    else:    
        form = AuthenticationForm()    
    return render(request, 'players/login.html', {'form': form})    

@login_required    
def profile_view(request):    
    return render(request, 'players/profile.html', {'player': request.user.player})    

@login_required    
def leaderboard_view(request):    
    players = Player.objects.all().order_by('-total_score')    
    return render(request, 'players/leaderboard.html', {'players': players})    


class PlayerViewSet(viewsets.ModelViewSet):    
    queryset = Player.objects.all()    
    serializer_class = PlayerSerializer  