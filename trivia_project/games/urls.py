from django.urls import path, include  
from rest_framework.routers import DefaultRouter  
from . import views  
from . import api_views  

router = DefaultRouter()  
router.register(r'games', api_views.GameViewSet)  

urlpatterns = [  
   
    path('', views.home_view, name='home'),  
    path('game/', views.game_view, name='game'),  
    path('game/restart/', views.restart_game_view, name='restart_game'),  
    path('game/start/', views.start_game_view, name='start_game'),  
    path('game/result/', views.game_result_view, name='game_result'),  

    # URLs API  
    path('api/', include(router.urls)),  
]  