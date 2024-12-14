# models.py  
from django.db import models  
from django.contrib.auth.models import User  
from django.db.models.signals import post_save  
from django.dispatch import receiver  

class Player(models.Model):  
    user = models.OneToOneField(User, on_delete=models.CASCADE)  
    total_score = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):  
        return f"Player: {self.user.username}"  

 
@receiver(post_save, sender=User)  
def create_user_player(sender, instance, created, **kwargs):  
    if created:  
        Player.objects.create(user=instance)  

@receiver(post_save, sender=User)  
def save_user_player(sender, instance, **kwargs):  
    instance.player.save()  