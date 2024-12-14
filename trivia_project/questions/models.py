from django.db import models  

class Question(models.Model):  
    text = models.CharField(max_length=500)  
    correct_answer = models.CharField(max_length=255)  
    option_1 = models.CharField(max_length=255)  
    option_2 = models.CharField(max_length=255)  
    option_3 = models.CharField(max_length=255)  
    option_4 = models.CharField(max_length=255)  
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):  
        return self.text  

    class Meta:  
        ordering = ['?']  # Esto ordenará las preguntas aleatoriamente  