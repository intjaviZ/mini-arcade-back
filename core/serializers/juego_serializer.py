from rest_framework import serializers

class GatoSerializer(serializers.Serializer):
    tablero = serializers.ListField(child=serializers.ListField(child=serializers.CharField()))
    jugadores = serializers.ListField(child=serializers.CharField())
    turno = serializers.CharField()
    ganador = serializers.CharField(allow_null=True)

class Conecta4Serializer(serializers.Serializer):
    tablero = serializers.ListField(child=serializers.ListField(child=serializers.CharField()))
    jugadores = serializers.ListField(child=serializers.CharField())
    turno = serializers.CharField()
    ganador = serializers.CharField(allow_null=True)
