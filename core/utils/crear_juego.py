from ..state.games import Gato, Conecta4

def crear_juego(juego, j1, j2):
    if juego == "gato":
        return Gato(jugador1=j1, jugador2=j2)
    elif juego == "conecta4":
        return Conecta4(jugador1=j1, jugador2=j2)