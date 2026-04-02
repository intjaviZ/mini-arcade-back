from django.urls import path
from ..views.room_views import AnfitrionSala, InvitadoSala

urlpatterns = [
    path('anfitrionSala/', AnfitrionSala.as_view()),
    path('invitadoSala/', InvitadoSala.as_view())
]