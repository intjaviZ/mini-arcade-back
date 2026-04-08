from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..utils.validators import validar_nombre, validar_juego, validar_id
from ..utils.generar_codigo import generar_ID
from ..state.state import state, Sala
from ..serializers.serializers import Sala_serializer
from ..services.room_services import ingresar_a_sala, cerrar_sala, obtener_sala

class AnfitrionSala(APIView):
    def get(self, request):
        raw = {}

        for id_sala, sala in state.salas.items():
            raw[id_sala] = sala.__dict__
            
        return Response(raw)
    
    def post(self, request):
        data = request.data
        nombre = data.get('nombre')
        juego = data.get('tipo_juego')
        
        if not nombre or not juego:
            return Response({"error": "Datos incompletos"}, status=status.HTTP_400_BAD_REQUEST)
    
        if not validar_nombre(nombre) or not validar_juego(juego):
            return Response( {"error": "Datos no válidos" }, status=status.HTTP_400_BAD_REQUEST)
            
        try:
            id_sala = generar_ID()
            
            nueva_sala = Sala(
                id_sala= id_sala,
                anfitrion=nombre,
                tipo_juego=juego
            )
            state.salas[id_sala] = nueva_sala
            
            response = Sala_serializer(state.salas[id_sala]).data
            return Response(response, status=status.HTTP_201_CREATED)
        
        except Exception as e:
            return Response({
                "mensaje": "Error en la creación de la sala, por favor intente más tarde",
                "error": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
    def delete(self, request):
        data = request.data
        nombre = data.get('nombre')
        id = data.get('id')
        
        if not nombre or not id:
            return Response({"error": "Datos incompletos"}, status=status.HTTP_400_BAD_REQUEST)
        
        if not validar_nombre(nombre) or not validar_id(id):
            return Response( {"error": "Datos no válidos" }, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            result = cerrar_sala(nombre, id)

            if isinstance(result, dict) and "error" in result:
                return Response(result , status=status.HTTP_400_BAD_REQUEST)

            response = Sala_serializer(result).data
            return Response(response, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                "mensaje": "Error inesperado",
                "error": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class StateSala(APIView):
    def get(self, request, id):
        sala = obtener_sala(id)
        
        if sala is None: return Response({"error": "Sala no existe"}, status=status.HTTP_404_NOT_FOUND)
        
        response = Sala_serializer(sala).data
        return Response(response, status=status.HTTP_200_OK)
        
class InvitadoSala(APIView):
    def post(self, request):
        data = request.data
        nombre = data.get('nombre')
        id = data.get('id')
        
        if not nombre or not id:
            return Response({"error": "Datos incompletos"}, status=status.HTTP_400_BAD_REQUEST)
        
        if not validar_nombre(nombre) or not validar_id(id):
            return Response( {"error": "Datos no válidos" }, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            result = ingresar_a_sala(nombre, id)
            
            if isinstance(result, dict) and "error" in result:
                return Response(result , status=status.HTTP_400_BAD_REQUEST)
            
            response = Sala_serializer(result).data
            return Response(response, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({
                "mensaje": "No logramos concretar la conexión a la sala, intenta en otro momento",
                "error": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)