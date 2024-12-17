# games/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def game_view(request):
    return render(request, 'games/game.html')

@login_required
def leaderboard_view(request):
    return render(request, 'games/leaderboard.html')

def home_view(request):
    return render(request, 'games/home.html')  