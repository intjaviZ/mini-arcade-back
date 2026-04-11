import string

def validar_nombre(nombre):
    if not isinstance(nombre, str): return False
    
    nombre_limpio = nombre.strip()
    if len(nombre_limpio) < 3 or len(nombre_limpio) > 15: return False
    if nombre_limpio.isdigit(): return False

    return True

def validar_juego(juego):
    if not isinstance(juego, str): return False
    if juego == "gato": return True
    elif juego == "conecta4": return True
    
    return False

def validar_id(id):
    if not isinstance(id, str): return False
    if len(id) != 4: return False

    caracteres_permitidos = string.ascii_uppercase + string.digits
    for caracter in id:
        if caracter not in caracteres_permitidos: return False

    return True