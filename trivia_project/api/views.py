from rest_framework import viewsets  
from rest_framework.permissions import IsAuthenticated  
from rest_framework.response import Response  
from rest_framework.decorators import action  
from .serializers import PlayerSerializer, QuestionSerializer, GameSerializer  
from players.models import Player  
from questions.models import Question  
from games.models import Game  

class PlayerViewSet(viewsets.ModelViewSet):  
    queryset = Player.objects.all()  
    serializer_class = PlayerSerializer  
    permission_classes = [IsAuthenticated]  

    def get_queryset(self):  
        return Player.objects.filter(user=self.request.user)  

class QuestionViewSet(viewsets.ReadOnlyModelViewSet):  
    queryset = Question.objects.all()  
    serializer_class = QuestionSerializer  
    permission_classes = [IsAuthenticated]  

class GameViewSet(viewsets.ModelViewSet):  
    queryset = Game.objects.all()  
    serializer_class = GameSerializer  
    permission_classes = [IsAuthenticated]  

    def get_queryset(self):  
        return Game.objects.filter(player__user=self.request.user)  

@action(detail=True, methods=['post'])  
def answer(self, request, pk=None):  
    game = self.get_object()  
    answer = request.data.get('answer')  

    if not answer:  
        return Response({'error': 'No se proporcionó una respuesta'}, status=400)  

    if game.is_finished:  
        return Response({'error': 'El juego ya ha terminado'}, status=400)  

    if not game.current_question:  
        return Response({'error': 'No hay pregunta actual'}, status=400)  

   
    correct_answer = str(game.current_question.correct_answer).strip().lower()  
    user_answer = str(answer).strip().lower()  
    is_correct = user_answer == correct_answer  

    if is_correct:  
        game.score += 4  
        game.save()  

  
    all_questions = list(Question.objects.all())  
    try:  
        current_index = all_questions.index(game.current_question)  
        next_question = all_questions[current_index + 1] if current_index + 1 < len(all_questions) else None  
    except ValueError:  
        next_question = None  

    if next_question:  
        game.current_question = next_question  
        game.save()  
    else:  
        game.is_finished = True  
        game.save()  

    return Response({  
        'correct': is_correct,  
        'score': game.score,  
        'is_finished': game.is_finished  
    })  
@action(detail=False, methods=['post'])  
def start_new(self, request):  
    player = Player.objects.get(user=request.user)  
    first_question = Question.objects.first()  

    if not first_question:  
            return Response({'error': 'No hay preguntas disponibles'}, status=400)  

    game = Game.objects.create(  
            player=player,  
            current_question=first_question  
        )  

    serializer = self.get_serializer(game)  
    return Response(serializer.data)  