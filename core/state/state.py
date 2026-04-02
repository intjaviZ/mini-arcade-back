class State:
    def __init__(self):
        self.salas = {}
        # self.espera = []
        # self.activas = {}

class Sala:
    def __init__(self, id_sala, anfitrion, tipo_juego):
        self.id_sala = id_sala
        self.anfitrion = anfitrion
        self.invitado = None
        self.tipo_juego = tipo_juego
        self.tablero = []
        self.turno = anfitrion
        self.ganador = None
        self.estado = "waiting"
        
state = State()