from django.core.management.base import BaseCommand  
from questions.models import Question  

def create_questions():  
    questions_data = [  
        {  
            "text": "¿Cuál es el río más largo del mundo?",  
            "correct_answer": "Río Amazonas",  
            "option_1": "Río Amazonas",  
            "option_2": "Río Nilo",  
            "option_3": "Río Misisipi",  
            "option_4": "Río Yangtsé"  
        },  
        {  
            "text": "¿Quién pintó la Mona Lisa?",  
            "correct_answer": "Leonardo da Vinci",  
            "option_1": "Leonardo da Vinci",  
            "option_2": "Miguel Ángel",  
            "option_3": "Pablo Picasso",  
            "option_4": "Vincent van Gogh"  
        },  
        {  
            "text": "¿En qué año comenzó la Primera Guerra Mundial?",  
            "correct_answer": "1914",  
            "option_1": "1914",  
            "option_2": "1916",  
            "option_3": "1918",  
            "option_4": "1912"  
        },  
        {  
            "text": "¿Cuál es el elemento químico más abundante en el universo?",  
            "correct_answer": "Hidrógeno",  
            "option_1": "Hidrógeno",  
            "option_2": "Helio",  
            "option_3": "Oxígeno",  
            "option_4": "Carbono"  
        },  
        {  
            "text": "¿Cuál es el planeta más grande del sistema solar?",  
            "correct_answer": "Júpiter",  
            "option_1": "Júpiter",  
            "option_2": "Saturno",  
            "option_3": "Urano",  
            "option_4": "Neptuno"  
        },  
        {  
            "text": "¿Quién escribió 'Don Quijote de la Mancha'?",  
            "correct_answer": "Miguel de Cervantes",  
            "option_1": "Miguel de Cervantes",  
            "option_2": "Federico García Lorca",  
            "option_3": "Gabriel García Márquez",  
            "option_4": "Pablo Neruda"  
        },  
        {  
            "text": "¿Cuál es la capital de Australia?",  
            "correct_answer": "Canberra",  
            "option_1": "Canberra",  
            "option_2": "Sídney",  
            "option_3": "Melbourne",  
            "option_4": "Brisbane"  
        },  
        {  
            "text": "¿En qué año se descubrió América?",  
            "correct_answer": "1492",  
            "option_1": "1492",  
            "option_2": "1489",  
            "option_3": "1495",  
            "option_4": "1500"  
        },  
        {  
            "text": "¿Cuál es el hueso más largo del cuerpo humano?",  
            "correct_answer": "Fémur",  
            "option_1": "Fémur",  
            "option_2": "Húmero",  
            "option_3": "Tibia",  
            "option_4": "Radio"  
        },  
        {  
            "text": "¿Quién fue el primer hombre en pisar la Luna?",  
            "correct_answer": "Neil Armstrong",  
            "option_1": "Neil Armstrong",  
            "option_2": "Buzz Aldrin",  
            "option_3": "Yuri Gagarin",  
            "option_4": "Alan Shepard"  
        },  
        {  
            "text": "¿Cuál es el océano más grande?",  
            "correct_answer": "Océano Pacífico",  
            "option_1": "Océano Pacífico",  
            "option_2": "Océano Atlántico",  
            "option_3": "Océano Índico",  
            "option_4": "Océano Ártico"  
        },  
        {  
            "text": "¿Quién inventó la bombilla eléctrica?",  
            "correct_answer": "Thomas Edison",  
            "option_1": "Thomas Edison",  
            "option_2": "Nikola Tesla",  
            "option_3": "Alexander Graham Bell",  
            "option_4": "Benjamin Franklin"  
        },  
        {  
            "text": "¿Cuál es el metal más precioso?",  
            "correct_answer": "Rodio",  
            "option_1": "Rodio",  
            "option_2": "Oro",  
            "option_3": "Platino",  
            "option_4": "Paladio"  
        },  
        {  
            "text": "¿En qué país se encuentra la Torre Eiffel?",  
            "correct_answer": "Francia",  
            "option_1": "Francia",  
            "option_2": "Italia",  
            "option_3": "España",  
            "option_4": "Alemania"  
        },  
        {  
            "text": "¿Cuál es el animal terrestre más grande?",  
            "correct_answer": "Elefante africano",  
            "option_1": "Elefante africano",  
            "option_2": "Ballena azul",  
            "option_3": "Jirafa",  
            "option_4": "Rinoceronte"  
        },  
        {  
            "text": "¿Quién escribió 'Romeo y Julieta'?",  
            "correct_answer": "William Shakespeare",  
            "option_1": "William Shakespeare",  
            "option_2": "Charles Dickens",  
            "option_3": "Jane Austen",  
            "option_4": "Mark Twain"  
        },  
        {  
            "text": "¿Cuál es la montaña más alta del mundo?",  
            "correct_answer": "Monte Everest",  
            "option_1": "Monte Everest",  
            "option_2": "K2",  
            "option_3": "Monte Kilimanjaro",  
            "option_4": "Monte Aconcagua"  
        },  
        {  
            "text": "¿En qué año terminó la Segunda Guerra Mundial?",  
            "correct_answer": "1945",  
            "option_1": "1945",  
            "option_2": "1944",  
            "option_3": "1946",  
            "option_4": "1943"  
        },  
        {  
            "text": "¿Cuál es el órgano más grande del cuerpo humano?",  
            "correct_answer": "La piel",  
            "option_1": "La piel",  
            "option_2": "El hígado",  
            "option_3": "Los pulmones",  
            "option_4": "El intestino"  
        },  
        {  
            "text": "¿Quién pintó 'La noche estrellada'?",  
            "correct_answer": "Vincent van Gogh",  
            "option_1": "Vincent van Gogh",  
            "option_2": "Claude Monet",  
            "option_3": "Salvador Dalí",  
            "option_4": "Pablo Picasso"  
        },  
        {  
            "text": "¿Cuál es el país más poblado del mundo?",  
            "correct_answer": "India",  
            "option_1": "India",  
            "option_2": "China",  
            "option_3": "Estados Unidos",  
            "option_4": "Indonesia"  
        },  
        {  
            "text": "¿Quién fue el primer presidente de Estados Unidos?",  
            "correct_answer": "George Washington",  
            "option_1": "George Washington",  
            "option_2": "Thomas Jefferson",  
            "option_3": "Abraham Lincoln",  
            "option_4": "John Adams"  
        },  
        {  
            "text": "¿Cuál es el elemento más pesado de la tabla periódica?",  
            "correct_answer": "Oganesón",  
            "option_1": "Oganesón",  
            "option_2": "Uranio",  
            "option_3": "Plutonio",  
            "option_4": "Californio"  
        },  
        {  
            "text": "¿En qué año se fundó la ONU?",  
            "correct_answer": "1945",  
            "option_1": "1945",  
            "option_2": "1944",  
            "option_3": "1946",  
            "option_4": "1947"  
        },  
        {  
            "text": "¿Cuál es la capital de Canadá?",  
            "correct_answer": "Ottawa",  
            "option_1": "Ottawa",  
            "option_2": "Toronto",  
            "option_3": "Vancouver",  
            "option_4": "Montreal"  
        },  
        {  
            "text": "¿Quién escribió '1984'?",  
            "correct_answer": "George Orwell",  
            "option_1": "George Orwell",  
            "option_2": "Aldous Huxley",  
            "option_3": "Ray Bradbury",  
            "option_4": "H.G. Wells"  
        },  
        {  
            "text": "¿Cuál es el instrumento musical más antiguo?",  
            "correct_answer": "Flauta",  
            "option_1": "Flauta",  
            "option_2": "Tambor",  
            "option_3": "Arpa",  
            "option_4": "Lira"  
        },  
        {  
            "text": "¿En qué año cayó el Muro de Berlín?",  
            "correct_answer": "1989",  
            "option_1": "1989",  
            "option_2": "1991",  
            "option_3": "1988",  
            "option_4": "1990"  
        },  
        {  
            "text": "¿Cuál es el idioma más hablado del mundo?",  
            "correct_answer": "Mandarín",  
            "option_1": "Mandarín",  
            "option_2": "Español",  
            "option_3": "Inglés",  
            "option_4": "Hindi"  
        },  
        {  
            "text": "¿Quién descubrió la penicilina?",  
            "correct_answer": "Alexander Fleming",  
            "option_1": "Alexander Fleming",  
            "option_2": "Louis Pasteur",  
            "option_3": "Marie Curie",  
            "option_4": "Robert Koch"  
        },  
        {  
            "text": "¿Cuál es el desierto más grande del mundo?",  
            "correct_answer": "Antártida",  
            "option_1": "Antártida",  
            "option_2": "Sahara",  
            "option_3": "Gobi",  
            "option_4": "Atacama"  
        },  
        {  
            "text": "¿En qué año se inventó Internet?",  
            "correct_answer": "1969",  
            "option_1": "1969",  
            "option_2": "1989",  
            "option_3": "1975",  
            "option_4": "1982"  
        },  
        {  
            "text": "¿Cuál es la velocidad de la luz?",  
            "correct_answer": "299,792 km/s",  
            "option_1": "299,792 km/s",  
            "option_2": "300,000 km/s",  
            "option_3": "299,000 km/s",  
            "option_4": "298,000 km/s"  
        },  
        {  
            "text": "¿Quién fue el primer emperador de China?",  
            "correct_answer": "Qin Shi Huang",  
            "option_1": "Qin Shi Huang",  
            "option_2": "Sun Yat-sen",  
            "option_3": "Mao Zedong",  
            "option_4": "Wu Zetian"  
        },  
        {  
            "text": "¿Cuál es el país más pequeño del mundo?",  
            "correct_answer": "Ciudad del Vaticano",  
            "option_1": "Ciudad del Vaticano",  
            "option_2": "Mónaco",  
            "option_3": "San Marino",  
            "option_4": "Nauru"  
        },  
        {  
            "text": "¿Quién inventó el teléfono?",  
            "correct_answer": "Alexander Graham Bell",  
            "option_1": "Alexander Graham Bell",  
            "option_2": "Thomas Edison",  
            "option_3": "Nikola Tesla",  
            "option_4": "Guglielmo Marconi"  
        },  
        {  
            "text": "¿Cuál es la capital de Japón?",  
            "correct_answer": "Tokio",  
            "option_1": "Tokio",  
            "option_2": "Kioto",  
            "option_3": "Osaka",  
            "option_4": "Yokohama"  
        },  
        {  
            "text": "¿En qué año se proclamó la Declaración Universal de los Derechos Humanos?",  
            "correct_answer": "1948",  
            "option_1": "1948",  
            "option_2": "1945",  
            "option_3": "1950",  
            "option_4": "1947"  
        },  
        {  
            "text": "¿Cuál es el metal más abundante en la corteza terrestre?",  
            "correct_answer": "Aluminio",  
            "option_1": "Aluminio",  
            "option_2": "Hierro",  
            "option_3": "Cobre",  
            "option_4": "Zinc"  
        },  
        {  
            "text": "¿Quién escribió 'Cien años de soledad'?",  
            "correct_answer": "Gabriel García Márquez",  
            "option_1": "Gabriel García Márquez",  
            "option_2": "Mario Vargas Llosa",  
            "option_3": "Julio Cortázar",  
            "option_4": "Isabel Allende"  
        },  
        {  
            "text": "¿Cuál es el continente más grande?",  
            "correct_answer": "Asia",  
            "option_1": "Asia",  
            "option_2": "América",  
            "option_3": "África",  
            "option_4": "Europa"  
        },  
        {  
            "text": "¿En qué año se fundó la UNESCO?",  
            "correct_answer": "1945",  
            "option_1": "1945",  
            "option_2": "1946",  
            "option_3": "1944",  
            "option_4": "1947"  
        },  
        {  
            "text": "¿Cuál es la moneda de Japón?",  
            "correct_answer": "Yen",  
            "option_1": "Yen",  
            "option_2": "Won",  
            "option_3": "Yuan",  
            "option_4": "Ringgit"  
        },  
        {  
            "text": "¿Quién fue el primer ser vivo en orbitar la Tierra?",  
            "correct_answer": "Laika",  
            "option_1": "Laika",  
            "option_2": "Yuri Gagarin",  
            "option_3": "Ham",  
            "option_4": "Albert II"  
        },  
        {  
            "text": "¿Cuál es la capital de Egipto?",  
            "correct_answer": "El Cairo",  
            "option_1": "El Cairo",  
            "option_2": "Alejandría",  
            "option_3": "Luxor" 
          },
        {  
            "text": "¿Cuál es la capital de Egipto?",  
            "correct_answer": "El Cairo",  
            "option_1": "El Cairo",  
            "option_2": "Alejandría",  
            "option_3": "Luxor",  
            "option_4": "Guiza"  
        },  
        {  
            "text": "¿Cuál es el principal gas que causa el efecto invernadero?",  
            "correct_answer": "Dióxido de carbono",  
            "option_1": "Dióxido de carbono",  
            "option_2": "Metano",  
            "option_3": "Ozono",  
            "option_4": "Óxido nitroso"  
        },  
        {  
            "text": "¿Quién desarrolló la teoría de la relatividad?",  
            "correct_answer": "Albert Einstein",  
            "option_1": "Albert Einstein",  
            "option_2": "Isaac Newton",  
            "option_3": "Stephen Hawking",  
            "option_4": "Niels Bohr"  
        },  
        {  
            "text": "¿Cuál es el lago más profundo del mundo?",  
            "correct_answer": "Lago Baikal",  
            "option_1": "Lago Baikal",  
            "option_2": "Lago Victoria",  
            "option_3": "Lago Superior",  
            "option_4": "Lago Tanganica"  
        },  
        {  
            "text": "¿En qué año se fundó Microsoft?",  
            "correct_answer": "1975",  
            "option_1": "1975",  
            "option_2": "1976",  
            "option_3": "1974",  
            "option_4": "1977"  
        },  
        {  
            "text": "¿Cuál es el hueso más pequeño del cuerpo humano?",  
            "correct_answer": "Estribo",  
            "option_1": "Estribo",  
            "option_2": "Martillo",  
            "option_3": "Yunque",  
            "option_4": "Falange"  
        },  
        {  
            "text": "¿Quién pintó 'El Grito'?",  
            "correct_answer": "Edvard Munch",  
            "option_1": "Edvard Munch",  
            "option_2": "Vincent van Gogh",  
            "option_3": "Pablo Picasso",  
            "option_4": "Salvador Dalí"  
        },  
        {  
            "text": "¿Cuál es la capital de Sudáfrica?",  
            "correct_answer": "Pretoria",  
            "option_1": "Pretoria",  
            "option_2": "Ciudad del Cabo",  
            "option_3": "Johannesburgo",  
            "option_4": "Bloemfontein"  
        },  
        {  
            "text": "¿En qué año se inventó la World Wide Web?",  
            "correct_answer": "1989",  
            "option_1": "1989",  
            "option_2": "1991",  
            "option_3": "1987",  
            "option_4": "1993"  
        },  
        {  
            "text": "¿Cuál es el elemento químico más electronegativo?",  
            "correct_answer": "Flúor",  
            "option_1": "Flúor",  
            "option_2": "Oxígeno",  
            "option_3": "Cloro",  
            "option_4": "Nitrógeno"  
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