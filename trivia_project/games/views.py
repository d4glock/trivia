# games/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Game
from questions.models import Question
from api.serializers import QuestionSerializer
from players.models import Player

@login_required
def game_view(request):
    return render(request, 'games/game.html')

@login_required
def leaderboard_view(request):
    return render(request, 'games/leaderboard.html')

def home_view(request):
    return render(request, 'games/home.html')

class SubmitAnswerView(APIView):
    def post(self, request):
        # Obtener los datos enviados en la solicitud
        game_id = request.data.get('game_id')
        answer_text = request.data.get('answer_text')

        # Validar que los datos requeridos estén presentes
        if not game_id or not answer_text:
            return Response(
                {'error': 'Faltan datos: game_id y answer_text son requeridos.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            # Obtener el juego correspondiente
            game = Game.objects.get(id=game_id)

            # Verificar que el juego pertenece al usuario autenticado
            if game.player.user != request.user:
                return Response(
                    {'error': 'No tienes permiso para responder en este juego.'},
                    status=status.HTTP_403_FORBIDDEN
                )

            # Obtener la pregunta actual del juego
            current_question = game.current_question

            # Verificar si la respuesta es correcta
            is_correct = (answer_text.strip().lower() == current_question.correct_answer.strip().lower())

            # Actualizar el puntaje si la respuesta es correcta
            if is_correct:
                game.score += 1

            # Verificar si el juego ha terminado
            next_question = Question.objects.order_by('?').exclude(id=current_question.id).first()
            if not next_question:
                game_over = True
            else:
                game_over = False
                game.current_question = next_question

            # Guardar los cambios en el juego
            game.save()

            # Responder con los resultados
            response_data = {
                'is_correct': is_correct,
                'score': game.score,
                'game_over': game_over,
            }

            if not game_over:
                response_data['next_question'] = QuestionSerializer(next_question).data

            return Response(response_data)

        except Game.DoesNotExist:
            return Response(
                {'error': 'El juego no existe.'},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {'error': f'Error interno: {str(e)}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )