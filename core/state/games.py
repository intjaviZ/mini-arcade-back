class Gato:
    def __init__(self, jugador1, jugador2):
        self.tablero = [ ["", "", ""], ["", "", ""], ["", "", ""] ]
        self.jugadores = [jugador1, jugador2]
        self.turno = jugador1
        self.ganador = None
        
    def jugar(self, jugador, x, y):
        resultado = self.validar(jugador, x, y)        
        if  "error" in resultado: return resultado
        
        self._mover(jugador, x, y)
        self.verificar_partida()
        if self.ganador is None: self.cambiar_turno()
        
        return { "ok": True }
    
    def _mover(self, jugador, x, y):
        simbolo = "X" if jugador == self.jugadores[0] else "O"
        self.tablero[x][y] = simbolo
            
    def verificar_partida(self):
        if self.ganador is not None: return

        if self._verificar_victoria(): return
        if self._verificar_empate(): self.ganador = "empate"
            
    def _verificar_empate(self):
        for fila in self.tablero:
            for celda in fila:
                if celda == "": return False
        return True
    
    def _verificar_victoria(self):
        t = self.tablero
        lineas = []
        lineas.extend(t)

        for i in range(3):
            lineas.append([t[0][i], t[1][i], t[2][i]])
            
        lineas.append([t[0][0], t[1][1], t[2][2]])
        lineas.append([t[0][2], t[1][1], t[2][0]])

        for linea in lineas:
            if linea[0] != "" and linea[0] == linea[1] == linea[2]:
                simbolo_ganador = linea[0]
                if simbolo_ganador == "X":
                    self.ganador = self.jugadores[0]
                else:
                    self.ganador = self.jugadores[1]
                
                return True
        return False
        
            
    def cambiar_turno(self):
        self.turno = (
            self.jugadores[1]
            if self.turno == self.jugadores[0]
            else self.jugadores[0]
        )
                
    def validar(self, jugador, x, y):
        if self.ganador is not None:
            return { "error": "La partida terminó"}
        if jugador != self.turno:
            return { "error": "No es tu turno" }
        if not (0 <= x < 3 and 0 <= y < 3):
            return { "error": "Posición no válida" }
        if self.tablero[x][y] != "":
            return { "error": "Casilla llena" }
        return { "ok": True }
        
class Conecta4:
    def __init__(self, jugador1, jugador2):
        self.tablero = [ ["", "", "", "", "", "", ""], ["", "", "", "", "", "", ""], ["", "", "", "", "", "", ""],
                         ["", "", "", "", "", "", ""], ["", "", "", "", "", "", ""], ["", "", "", "", "", "", ""] ]
        self.jugadores = [jugador1, jugador2]
        self.turno = jugador1
        self.ganador = None
        
    def jugar(self, jugador, x, y):
        resultado = self.validar(jugador, y)
        if "error" in resultado: return resultado
        
        simbolo = self._obtener_simbolo(jugador)
        movimiento = self._gravedad(y, simbolo)
        if "error" in movimiento: return movimiento
        self.verificar_partida()
        
        if self.ganador is None: self.cambiar_turno()
        return {"ok": True}
        
    def _gravedad(self, columna, simbolo):
        fila = self._obtener_fila_disponible(columna)

        if fila is None: return {"error": "Columna llena"}

        self.tablero[fila][columna] = simbolo
        return {"ok": True}
    
    def _obtener_fila_disponible(self, columna):
        for fila in range(len(self.tablero) - 1, -1, -1):
            if self.tablero[fila][columna] == "":
                return fila
        return None
        
    def _obtener_simbolo(self, jugador):
        return "R" if jugador == self.jugadores[0] else "A"
        
    def cambiar_turno(self):
        self.turno = (
            self.jugadores[1]
            if self.turno == self.jugadores[0]
            else self.jugadores[0]
        )
        
    def verificar_partida(self):
        tablero = self.tablero
        filas = len(tablero)
        columnas = len(tablero[0])

        for f in range(filas):
            for c in range(columnas):
                simbolo = tablero[f][c]
                if simbolo == "": continue

                # Direcciones a comprobar: (delta_fila, delta_columna)
                direcciones = [
                    (0, 1),  # Horizontal derecha
                    (1, 0),  # Vertical abajo
                    (1, 1),  # Diagonal abajo-derecha
                    (1, -1)  # Diagonal abajo-izquierda
                ]

                for df, dc in direcciones:
                    if self._comprobar_linea(f, c, df, dc, simbolo):
                        self.ganador = self.jugadores[0] if simbolo == "R" else self.jugadores[1]
                        return

        # Verificar Empate (si no hay espacios vacíos)
        if all(casilla != "" for fila in tablero for casilla in fila):
            self.ganador = "empate"

    def _comprobar_linea(self, fila, col, df, dc, simbolo):
        """Comprueba si hay 4 en raya en una dirección específica."""
        for i in range(1, 4):
            n_fila = fila + (df * i)
            n_col = col + (dc * i)
            
            # Verificar límites del tablero
            if not (0 <= n_fila < len(self.tablero) and 0 <= n_col < len(self.tablero[0])):
                return False
            if self.tablero[n_fila][n_col] != simbolo:
                return False
        return True
    
    def validar(self, jugador, y):
        if self.ganador is not None:
            return { "error": "La partida terminó"}
        if jugador != self.turno:
            return { "error": "No es tu turno" }
        if self.tablero[0][y] != "":
            return {"error": "Columna llena"}
        if not (0 <= y < 7):
            return { "error": "Posición no válida" }
        return { "ok": True }