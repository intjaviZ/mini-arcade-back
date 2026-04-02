from rest_framework import serializers

class Sala_serializer(serializers.Serializer):
    id_sala = serializers.CharField(max_length=4)
    anfitrion = serializers.CharField(min_length=3, max_length=15)
    invitado = serializers.CharField(min_length=3, max_length=15, allow_null=True, required=False)
    tipo_juego = serializers.ChoiceField(choices=["gato", "conecta4", "ahorcado"])
    tablero = serializers.ListField()
    ganador = serializers.CharField(min_length=3, max_length=15)
    turno = serializers.CharField(min_length=3, max_length=15)
    estado = serializers.CharField()