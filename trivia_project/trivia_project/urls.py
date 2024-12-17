# urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from api.views import GameViewSet, PlayerViewSet, QuestionViewSet  # Todos desde api.views
from players import views as player_views
from questions import views as question_views
from games import views as game_views
from django.contrib.auth import views as auth_views

# Configuración del router para la API
router = DefaultRouter()
router.register(r'questions', QuestionViewSet)
router.register(r'players', PlayerViewSet)
router.register(r'games', GameViewSet)

# URLs para la API
api_urlpatterns = [
    path('', include(router.urls)),
    path('token/', obtain_auth_token, name='api_token_auth'),
    path('auth/', include('rest_framework.urls')),
]

# URLs para el frontend
frontend_urlpatterns = [
    # Autenticación y perfil de usuario
    path('login/', player_views.login_view, name='login'),
    path('logout/', player_views.logout_view, name='logout'),
    path('register/', player_views.register_view, name='register'),
    path('redirect/', player_views.custom_redirect, name='custom_redirect'),
    path('profile/', player_views.profile_view, name='profile'),
    path('leaderboard/', player_views.leaderboard_view, name='leaderboard'),

    # Preguntas
    path('questions/', question_views.questions_list_view, name='questions_list'),
    path('questions/<int:pk>/', question_views.question_detail_view, name='question_detail'),

    # Juego
    path('', game_views.home_view, name='home'),
    path('game/', game_views.game_view, name='game'),
]

# URLs principales
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urlpatterns)),
    path('', include(frontend_urlpatterns)),
]