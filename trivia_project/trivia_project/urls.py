# urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from api.views import (
    GameViewSet, 
    PlayerViewSet, 
    QuestionViewSet,
    SubmitAnswerView
)
from players import views as player_views
from questions import views as question_views
from games import views as game_views
from django.contrib.auth import views as auth_views
from api.views import SubmitAnswerView

# Configuración del router para la API
router = DefaultRouter()
router.register(r'questions', QuestionViewSet)
router.register(r'players', PlayerViewSet)
router.register(r'games', GameViewSet)

# URLs para la API
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/games/submit-answer/', SubmitAnswerView.as_view(), name='submit_answer'),

    # API URLs
    path('api/', include([
        path('', include(router.urls)),
        path('token/', obtain_auth_token, name='api_token_auth'),
        path('auth/', include('rest_framework.urls')),
        path('api/games/submit-answer/', SubmitAnswerView.as_view(), name='submit_answer'),
    ])),

    # Frontend URLs
    path('login/', player_views.login_view, name='login'),
    path('logout/', player_views.logout_view, name='logout'),
    path('register/', player_views.register_view, name='register'),
    path('redirect/', player_views.custom_redirect, name='custom_redirect'),
    path('profile/', player_views.profile_view, name='profile'),
    path('leaderboard/', player_views.leaderboard_view, name='leaderboard'),
    path('questions/', question_views.questions_list_view, name='questions_list'),
    path('questions/<int:pk>/', question_views.question_detail_view, name='question_detail'),
    path('', game_views.home_view, name='home'),
    path('game/', game_views.game_view, name='game'),
]