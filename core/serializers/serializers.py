from rest_framework import serializers
from ..state.games import Gato, Conecta4
from .juego_serializer import GatoSerializer, Conecta4Serializer

class Sala_serializer(serializers.Serializer):
    id_sala = serializers.CharField(max_length=4)
    anfitrion = serializers.CharField(min_length=3, max_length=15)
    invitado = serializers.CharField(min_length=3, max_length=15, allow_null=True, required=False)
    tipo_juego = serializers.ChoiceField(choices=["gato", "conecta4"])
    juego = serializers.SerializerMethodField()
    estado = serializers.CharField()
    
    def get_juego(self, obj):
        if obj.juego is None:
            return None
            
        if isinstance(obj.juego, Gato):
            return GatoSerializer(obj.juego).data
        if isinstance(obj.juego, Conecta4):
            return Conecta4Serializer(obj.juego).data
            
        return None