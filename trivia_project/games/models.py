from django.db import models  
from players.models import Player  
from questions.models import Question  

class Game(models.Model):  
    player = models.ForeignKey(Player, on_delete=models.CASCADE)  
    score = models.IntegerField(default=0)  
    current_question = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True, blank=True)  
    is_finished = models.BooleanField(default=False)  
    created_at = models.DateTimeField(auto_now_add=True)  # Aseguramos que este campo exista  

    def __str__(self):  
        return f"Juego de {self.player.user.username} - Puntaje: {self.score}"  

    class Meta:  
        ordering = ['-created_at']  