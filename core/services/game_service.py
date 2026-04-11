from ..state.state import state
from ..utils.crear_juego import crear_juego

def iniciar_juego(id, jugador):
    if id not in state.salas: return {"error": "La sala no existe"}
    sala = state.salas[id]
    
    if jugador != sala.anfitrion: return {"error": "No eres el anfitrion"}
    if sala.estado != "ready": return {"error": "La sala no está lista"}
    if sala.juego is not None: return {"error": "El juego ya inició"}
    
    sala.juego = crear_juego(sala.tipo_juego, sala.anfitrion, sala.invitado)
    sala.estado = "playing"
    return sala

def reiniciar_juego(id, jugador):
    if id not in state.salas: return {"error": "La sala no existe"}
    sala = state.salas[id]
    
    if sala.estado == "playing": return sala
    if jugador != sala.anfitrion: return {"error": "No eres el anfitrion"}
    if sala.juego is None: return {"error": "No hay juego activo"}
    if sala.estado != "finished": return {"error": "No ha terminado su partida"}
    if not sala.invitado: return {"error": "No hay un invitado"}
    
    sala.juego = crear_juego(sala.tipo_juego, sala.anfitrion, sala.invitado)
    sala.estado = "playing"
    return sala

def hacer_movimiento(id, jugador, x, y):
    if id not in state.salas: return {"error": "La sala no existe"}
    sala = state.salas[id]
    
    if jugador != sala.anfitrion and jugador != sala.invitado: return {"error": "Jugador no pertenece a la sala"}
    if sala.juego is None: return {"error": "No hay juego activo"}
    if sala.estado != "playing": return {"error": "La partida no ha iniciado"}
    
    resultado = sala.juego.jugar(jugador, x, y)
    
    if "error" in resultado: return resultado
    
    if sala.juego.ganador is not None:
        sala.estado = "finished"
    print(f"Estado: {sala.estado}, Ganador: {sala.juego.ganador}")
    return sala