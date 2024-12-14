from django.contrib import admin  
from .models import Player  

@admin.register(Player)  
class PlayerAdmin(admin.ModelAdmin):  
    list_display = ('user', 'total_score', 'created_at')  
    search_fields = ('user__username',)  