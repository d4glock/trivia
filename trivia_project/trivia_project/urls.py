from django.contrib import admin  
from django.urls import path, include  
from rest_framework.routers import DefaultRouter  
from questions.views import QuestionViewSet  
from players.views import PlayerViewSet  
from games.views import GameViewSet  
from rest_framework.authtoken.views import obtain_auth_token  
from players import views as player_views  
from questions import views as question_views  
from games import views as game_views  
from django.contrib.auth import views as auth_views  
from players.views import custom_redirect


router = DefaultRouter()  
router.register(r'questions', QuestionViewSet)  
router.register(r'players', PlayerViewSet)  
router.register(r'games', GameViewSet)  

api_urlpatterns = [  
    path('', include(router.urls)),  
    path('api/', include(router.urls)),  
    path('token/', obtain_auth_token, name='api_token_auth'),  
    path('auth/', include('rest_framework.urls')),  
]  

 
frontend_urlpatterns = [  
    
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
    path('game/start/', game_views.start_game_view, name='start_game'),  
    path('game/result/', game_views.game_result_view, name='game_result'),  
    path('game/restart/', game_views.restart_game_view, name='restart_game'),  
]  

urlpatterns = [  
    path('admin/', admin.site.urls),  
    path('api/', include(api_urlpatterns)),  
    path('', include(frontend_urlpatterns)),
      
]  