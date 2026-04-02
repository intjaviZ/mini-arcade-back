import string
import secrets
from ..state.state import state

def generar_ID():
    longitud_id = 4
    caracteres = string.ascii_uppercase + string.digits
    while True:
        nuevo_id = ''.join(secrets.choice(caracteres) for _ in range(longitud_id))
        if nuevo_id not in state.salas:
            return nuevo_id