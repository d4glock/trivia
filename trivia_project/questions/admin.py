from django.contrib import admin  
from .models import Question  
  
@admin.register(Question)  
class QuestionAdmin(admin.ModelAdmin):  
    list_display = ('text', 'correct_answer', 'created_at')  
    search_fields = ('text', 'correct_answer')  
    list_filter = ('created_at',)  
    fieldsets = (  
        (None, {  
            'fields': ('text', 'correct_answer')  
        }),  
        ('Opciones', {  
            'fields': ('option_1', 'option_2', 'option_3', 'option_4')  
        }),  
    )  