from django.shortcuts import render, redirect  
from django.contrib.auth.decorators import login_required  
from questions.models import Question  
from games.models import Game  
from django.contrib import messages  
from rest_framework import viewsets  
from rest_framework.decorators import action  
from rest_framework.response import Response  
from api.serializers import GameSerializer


class GameViewSet(viewsets.ModelViewSet):  
    queryset = Game.objects.all()  
    serializer_class = GameSerializer  

    @action(detail=False, methods=['post'])  
    def start_game(self, request):  
         
        return Response({'status': 'Juego iniciado'})  

    @action(detail=False, methods=['post'])  
    def restart_game(self, request):  
        
        request.session['current_question_index'] = 0  
        request.user.player.total_score = 0  
        request.user.player.save()  
        return Response({'status': 'Juego reiniciado', 'score': request.user.player.total_score})  


def home_view(request):  
    
    return render(request, 'games/home.html', {  
        'total_questions': Question.objects.count(),  
    })  


@login_required    
def game_view(request):    
    
    if 'question_ids' not in request.session:  
        question_ids = list(Question.objects.values_list('id', flat=True))  
        from random import shuffle  
        shuffle(question_ids)   
        request.session['question_ids'] = question_ids  

    question_ids = request.session.get('question_ids', [])  
    current_question_index = request.session.get('current_question_index', 0)    

    if not question_ids or current_question_index >= len(question_ids):    
        return render(request, 'games/game.html', {    
            'message': '¡Juego terminado!',    
            'final_score': request.user.player.total_score    
        })    


    try:  
        current_question = Question.objects.get(id=question_ids[current_question_index])  
    except Question.DoesNotExist:  
        messages.error(request, 'Error al cargar la pregunta')  
        return redirect('home')  

    if request.method == 'POST':    
        selected_answer = request.POST.get('answer')  

        # Debug logging  
        print(f"Índice actual: {current_question_index}")  
        print(f"Pregunta actual: {current_question.text}")  
        print(f"Respuesta seleccionada: '{selected_answer}'")  
        print(f"Respuesta correcta: '{current_question.correct_answer}'")  

        if selected_answer:  
            if selected_answer == current_question.correct_answer:  
                request.user.player.total_score += 1    
                request.user.player.save()    
                messages.success(request, '¡Respuesta correcta! +1 punto')    
            else:    
                messages.error(request,   
                    f'Respuesta incorrecta. La respuesta correcta era: {current_question.correct_answer}')     

            request.session['current_question_index'] = current_question_index + 1    
            return redirect('game')    
        else:  
            messages.error(request, 'Por favor selecciona una respuesta')  

    
    context = {    
        'question': current_question,    
        'question_number': current_question_index + 1,    
        'total_questions': len(question_ids),  
        'messages': messages.get_messages(request)  
    }  

    return render(request, 'games/game.html', context)  

@login_required    
def restart_game_view(request):    
   
    if 'question_ids' in request.session:  
        del request.session['question_ids']  
    if 'current_question_index' in request.session:  
        del request.session['current_question_index']  

    request.user.player.total_score = 0  
    request.user.player.save()  

    messages.info(request, '¡Juego reiniciado!')    
    return redirect('game')  
@login_required    
def start_game_view(request):      

    if 'question_ids' in request.session:  
        del request.session['question_ids']  
    if 'current_question_index' in request.session:  
        del request.session['current_question_index']  

    request.user.player.total_score = 0  
    request.user.player.save()  

    messages.info(request, '¡Nuevo juego iniciado!')    
    return redirect('game')  


@login_required  
def game_result_view(request):  
     
    return render(request, 'games/result.html', {  
        'score': request.user.player.total_score,  
        'total_questions': Question.objects.count()  
    })  