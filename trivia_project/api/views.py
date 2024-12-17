# api/views.py
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import PlayerSerializer, QuestionSerializer, GameSerializer
from players.models import Player
from questions.models import Question
from games.models import Game
import random

class QuestionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]


class GameViewSet(viewsets.ModelViewSet):
    serializer_class = GameSerializer
    permission_classes = [IsAuthenticated]
    queryset = Game.objects.all()  # Añadimos esta línea

    def get_queryset(self):
        # Filtramos para que cada usuario solo vea sus juegos
        return Game.objects.filter(player=self.request.user)

    @action(detail=False, methods=['post'], permission_classes=[IsAuthenticated])
    def start_game(self, request):
        try:
            # Crear nuevo juego
            game = Game.objects.create(
                player=request.user,
                score=0,
                current_question=1
            )

            # Obtener primera pregunta aleatoria
            question = Question.objects.order_by('?').first()

            return Response({
                'game_id': game.id,
                'question': QuestionSerializer(question).data
            })
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
        
    @action(detail=False, methods=['post'])
    def submit_answer(self, request):
        try:
            game_id = request.data.get('game_id')
            answer_text = request.data.get('answer_text')

            game = Game.objects.get(id=game_id, player=request.user)
            current_question = Question.objects.get(id=game.current_question)

            # Verificar respuesta
            is_correct = current_question.correct_answer == answer_text
            if is_correct:
                game.score += 10

            game.current_question += 1
            game.save()

            # Verificar si el juego terminó
            game_over = game.current_question > 10

            response_data = {
                'is_correct': is_correct,
                'score': game.score,
                'game_over': game_over
            }

            if not game_over:
                next_question = Question.objects.order_by('?').first()
                response_data['next_question'] = QuestionSerializer(next_question).data

            return Response(response_data)
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Player.objects.filter(user=self.request.user)

    @action(detail=False, methods=['GET'])
    def leaderboard(self, request):
        players = Player.objects.all().order_by('-total_score')[:10]
        return Response(PlayerSerializer(players, many=True).data)
    
