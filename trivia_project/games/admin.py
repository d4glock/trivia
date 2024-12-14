from django.contrib import admin  
from .models import Game  

@admin.register(Game)  
class GameAdmin(admin.ModelAdmin):  
    list_display = ('id', 'player', 'created_at', 'score', 'is_finished') 
    search_fields = ('player__user__username',)  
    list_filter = ('is_finished', 'created_at') 