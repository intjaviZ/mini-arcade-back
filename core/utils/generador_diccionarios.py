def to_dict(obj):
    # Si el objeto tiene __dict__, lo convertimos y procesamos sus hijos
    if hasattr(obj, "__dict__"):
        data = dict(obj.__dict__)
        for key, value in data.items():
            data[key] = to_dict(value) # Llamada recursiva
        return data
    # Si es una lista (como el tablero), procesamos cada elemento
    elif isinstance(obj, list):
        return [to_dict(item) for item in obj]
    # Si es un tipo básico, lo devolvemos tal cual
    else:
        return obj