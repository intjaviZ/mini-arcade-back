from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers.serializers import Sala_serializer
from ..services.game_service import hacer_movimiento, iniciar_juego, reiniciar_juego

class Iniciar_Juego(APIView):
    def post(self, request):
        data = request.data
        id_sala = data.get("id")
        jugador = data.get("jugador")
        
        if not id_sala or not jugador: 
            return Response({ "error": "Datos incompletos." }, status=status.HTTP_400_BAD_REQUEST)
        
        result = iniciar_juego(id_sala, jugador)
        if isinstance(result, dict) and "error" in result:
            return Response(result, status=status.HTTP_400_BAD_REQUEST)
        
        response = Sala_serializer(result).data
        return Response(response, status=status.HTTP_200_OK)
    
class Reiniciar_Juego(APIView):
    def post(self, request):
        data = request.data
        id_sala = data.get("id")
        jugador = data.get("jugador")
        
        if not id_sala and not jugador: 
            return Response({ "error": "Datos incompletos." }, status=status.HTTP_400_BAD_REQUEST)
        
        result = reiniciar_juego(id_sala, jugador)
        if isinstance(result, dict) and "error" in result:
            return Response(result, status=status.HTTP_400_BAD_REQUEST)
        
        response = Sala_serializer(result).data
        return Response(response, status=status.HTTP_200_OK)
        

class Play_Gato(APIView):
    def post(self, request):
        data = request.data

        id_sala = data.get("id")
        jugador = data.get("jugador")
        x = data.get("x")
        y = data.get("y")

        if id_sala is None or jugador is None or x is None or y is None:
            return Response({ "error": "Datos incompletos" },status=status.HTTP_400_BAD_REQUEST)

        try:
            x = int(x)
            y = int(y)
        except ValueError:
            return Response({ "error": "Coordenadas inválidas" },status=status.HTTP_400_BAD_REQUEST)

        result = hacer_movimiento(id_sala, jugador, x, y)

        if isinstance(result, dict) and "error" in result:
            return Response(result, status=status.HTTP_400_BAD_REQUEST)

        response = Sala_serializer(result).data
        return Response(response, status=status.HTTP_200_OK)
    
class Play_Conecta4(APIView):
    def post(self, request):
        data = request.data

        id_sala = data.get("id")
        jugador = data.get("jugador")
        columna = data.get("columna")

        if id_sala is None or jugador is None or columna is None:
            return Response({ "error": "Datos incompletos" },status=status.HTTP_400_BAD_REQUEST)

        try:
            columna = int(columna)
        except (ValueError, TypeError):
            return Response({ "error": "Columna inválida" },status=status.HTTP_400_BAD_REQUEST)

        result = hacer_movimiento(id_sala, jugador, x=0, y=columna)

        if isinstance(result, dict) and "error" in result:
            return Response(result, status=status.HTTP_400_BAD_REQUEST)

        response = Sala_serializer(result).data
        return Response(response, status=status.HTTP_200_OK)