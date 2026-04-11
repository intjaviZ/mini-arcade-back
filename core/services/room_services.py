from ..state.state import state, Sala
from ..utils.generar_codigo import generar_ID

def crear_sala(nombre, tipo_juego):
    id_sala = generar_ID()
    
    sala = Sala(
        id_sala= id_sala,
        anfitrion = nombre,
        tipo_juego= tipo_juego
    )
    state.salas[id_sala] = sala
    return sala

def ingresar_a_sala(nombre, id):
    if id not in state.salas: return {"error": "La sala no existe"}

    sala = state.salas[id]

    if sala.anfitrion == nombre: return {"error": "Ya eres el anfitrión"}
    if sala.invitado is not None: return {"error": "Sala llena"}
    
    sala.invitado = nombre
    sala.estado = "ready"
    return sala

def cerrar_sala(nombre, id):
    if id not in state.salas: return {"error": "La sala no existe"}

    sala = state.salas[id]
    
    if sala.anfitrion != nombre: return {"error": "No eres el anfitrión"}
    
    sala.estado = "finished"
    del state.salas[id]
    return sala

def obtener_sala(id):
    if id not in state.salas: return None
    return state.salas[id]
    