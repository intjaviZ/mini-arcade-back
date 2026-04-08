from ..state.state import state

def ingresar_a_sala(nombre, id):
    if id not in state.salas: return {"error": "La sala no existe"}

    sala = state.salas[id]

    if sala.invitado is not None: return {"error": "Sala llena"}

    # 3. Evitar que el anfitrión se una como invitado
    if sala.anfitrion == nombre: return {"error": "Ya eres el anfitrión"}

    # 4. Asignar invitado
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
    