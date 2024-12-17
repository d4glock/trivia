from rest_framework import serializers  
from questions.models import Question  
from players.models import Player  
from games.models import Game  
from django.contrib.auth.models import User  

 
class UserSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = User  
        fields = ['id', 'username', 'email']  

  
class PlayerSerializer(serializers.ModelSerializer):  
    user = UserSerializer(read_only=True)  

    class Meta:  
        model = Player  
        fields = ['id', 'user', 'total_score']  



class QuestionSerializer(serializers.ModelSerializer):
    options = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = ['id', 'text', 'options']

    def get_options(self, obj):
        options = [
            {'id': 1, 'text': obj.option_1},
            {'id': 2, 'text': obj.option_2},
            {'id': 3, 'text': obj.option_3},
            {'id': 4, 'text': obj.option_4},
        ]
        random.shuffle(options)
        return options

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'score', 'current_question', 'created_at']