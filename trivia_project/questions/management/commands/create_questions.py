from django.core.management.base import BaseCommand   
from models import Question


def create_questions():  
    questions_data =[
    {
        "text": "¿Cuál es el río más largo del mundo?",
        "correct_answer": "Río Amazonas",
        "option_1": "Río Nilo",
        "option_2": "Río Amazonas",
        "option_3": "Río Yangtsé",
        "option_4": "Río Misisipi"
    },
    {
        "text": "¿Quién pintó la Mona Lisa?",
        "correct_answer": "Leonardo da Vinci",
        "option_1": "Miguel Ángel",
        "option_2": "Leonardo da Vinci",
        "option_3": "Vincent van Gogh",
        "option_4": "Pablo Picasso"
    },
    {
        "text": "¿En qué año comenzó la Primera Guerra Mundial?",
        "correct_answer": "1914",
        "option_1": "1918",
        "option_2": "1914",
        "option_3": "1916",
        "option_4": "1912"
    },
    {
        "text": "¿Cuál es el elemento químico más abundante en el universo?",
        "correct_answer": "Hidrógeno",
        "option_1": "Helio",
        "option_2": "Hidrógeno",
        "option_3": "Oxígeno",
        "option_4": "Carbono"
    },
    {
        "text": "¿Cuál es el planeta más grande del sistema solar?",
        "correct_answer": "Júpiter",
        "option_1": "Neptuno",
        "option_2": "Urano",
        "option_3": "Saturno",
        "option_4": "Júpiter"
    },
    {
        "text": "¿Quién escribió 'Don Quijote de la Mancha'?",
        "correct_answer": "Miguel de Cervantes",
        "option_1": "Gabriel García Márquez",
        "option_2": "Miguel de Cervantes",
        "option_3": "Pablo Neruda",
        "option_4": "Federico García Lorca"
    },
    {
        "text": "¿Cuál es la capital de Australia?",
        "correct_answer": "Canberra",
        "option_1": "Sídney",
        "option_2": "Melbourne",
        "option_3": "Brisbane",
        "option_4": "Canberra"
    },
    {
        "text": "¿En qué año se descubrió América?",
        "correct_answer": "1492",
        "option_1": "1495",
        "option_2": "1489",
        "option_3": "1500",
        "option_4": "1492"
    },
    {
        "text": "¿Cuál es el hueso más largo del cuerpo humano?",
        "correct_answer": "Fémur",
        "option_1": "Tibia",
        "option_2": "Radio",
        "option_3": "Fémur",
        "option_4": "Húmero"
    },
    {
        "text": "¿Quién fue el primer hombre en pisar la Luna?",
        "correct_answer": "Neil Armstrong",
        "option_1": "Buzz Aldrin",
        "option_2": "Neil Armstrong",
        "option_3": "Alan Shepard",
        "option_4": "Yuri Gagarin"
    },
    {
        "text": "¿Cuál es el océano más grande?",
        "correct_answer": "Océano Pacífico",
        "option_1": "Océano Índico",
        "option_2": "Océano Atlántico",
        "option_3": "Océano Ártico",
        "option_4": "Océano Pacífico"
    },
    {
        "text": "¿Quién inventó la bombilla eléctrica?",
        "correct_answer": "Thomas Edison",
        "option_1": "Nikola Tesla",
        "option_2": "Thomas Edison",
        "option_3": "Benjamin Franklin",
        "option_4": "Alexander Graham Bell"
    },
    {
        "text": "¿Cuál es el metal más precioso?",
        "correct_answer": "Rodio",
        "option_1": "Paladio",
        "option_2": "Oro",
        "option_3": "Rodio",
        "option_4": "Platino"
    },
    {
        "text": "¿En qué país se encuentra la Torre Eiffel?",
        "correct_answer": "Francia",
        "option_1": "Alemania",
        "option_2": "España",
        "option_3": "Italia",
        "option_4": "Francia"
    },
    {
        "text": "¿Cuál es el animal terrestre más grande?",
        "correct_answer": "Elefante africano",
        "option_1": "Rinoceronte",
        "option_2": "Elefante africano",
        "option_3": "Jirafa",
        "option_4": "Ballena azul"
    },
    {
        "text": "¿Quién escribió 'Romeo y Julieta'?",
        "correct_answer": "William Shakespeare",
        "option_1": "Mark Twain",
        "option_2": "Charles Dickens",
        "option_3": "William Shakespeare",
        "option_4": "Jane Austen"
    },
    {
        "text": "¿Cuál es la montaña más alta del mundo?",
        "correct_answer": "Monte Everest",
        "option_1": "Monte Aconcagua",
        "option_2": "Monte Kilimanjaro",
        "option_3": "Monte Everest",
        "option_4": "K2"
    },
    {
        "text": "¿En qué año terminó la Segunda Guerra Mundial?",
        "correct_answer": "1945",
        "option_1": "1944",
        "option_2": "1946",
        "option_3": "1945",
        "option_4": "1943"
    },
    {
        "text": "¿Cuál es el órgano más grande del cuerpo humano?",
        "correct_answer": "La piel",
        "option_1": "El hígado",
        "option_2": "La piel",
        "option_3": "El intestino",
        "option_4": "Los pulmones"
    }
]


    for question_data in questions_data:  
        Question.objects.create(  
            text=question_data["text"],  
            correct_answer=question_data["correct_answer"],  
            option_1=question_data["option_1"],  
            option_2=question_data["option_2"],  
            option_3=question_data["option_3"],  
            option_4=question_data["option_4"]  
        )  
        print(f"Pregunta creada: {question_data['text']}")  

class Command(BaseCommand):  
    help = 'Crea preguntas de cultura general para el juego de trivia'  

    def handle(self, *args, **kwargs):  
        self.stdout.write('Creando preguntas...')  
        create_questions()  
        self.stdout.write(self.style.SUCCESS('Preguntas creadas exitosamente'))  