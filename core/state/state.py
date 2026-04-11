class State:
    def __init__(self):
        self.salas = {}

class Sala:
    def __init__(self, id_sala, anfitrion, tipo_juego):
        self.id_sala = id_sala
        self.anfitrion = anfitrion
        self.invitado = None
        self.tipo_juego = tipo_juego
        self.juego  = None
        self.estado = "waiting"
        
state = State()