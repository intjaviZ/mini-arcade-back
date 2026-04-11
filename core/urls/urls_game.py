from django.urls import path
from ..views.game_views import Play_Gato, Play_Conecta4, Iniciar_Juego, Reiniciar_Juego

urlpatterns = [
    path('iniciarJuego/', Iniciar_Juego.as_view()),
    path('reiniciarJuego/', Reiniciar_Juego.as_view()),
    path('playGato/', Play_Gato.as_view()),
    path('playConecta4/', Play_Conecta4.as_view()),
]