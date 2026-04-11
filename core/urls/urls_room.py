from django.urls import path
from ..views.room_views import AnfitrionSala, InvitadoSala, StateSala
from ..views.game_views import Play_Gato

urlpatterns = [
    path('anfitrionSala/', AnfitrionSala.as_view()),
    path('invitadoSala/', InvitadoSala.as_view()),
    path('estadoSala/<slug:id>/', StateSala.as_view()),
    path('playGato/', Play_Gato.as_view()),
]