from rest_framework import viewsets  
from .models import Question  
from api.serializers import QuestionSerializer  
from django.shortcuts import render, get_object_or_404  
from django.contrib.auth.decorators import login_required  

class QuestionViewSet(viewsets.ModelViewSet):  
    queryset = Question.objects.all()  
    serializer_class = QuestionSerializer  

@login_required    
def questions_list_view(request):    
    questions = Question.objects.all()    
    return render(request, 'questions/questions_list.html', {'questions': questions})    

@login_required    
def question_detail_view(request, pk):    
    question = get_object_or_404(Question, pk=pk)    
    return render(request, 'questions/question_detail.html', {'question': question})  