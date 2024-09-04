import random

def crearTablero(dimension):
    return [["~" for _ in range(dimension)] for _ in range(dimension)]

def mostrarTableros(tableroDisparosJugador, tableroDisparosOponente):
    print("\nTu Tablero de disparos:")
    for fila in tableroDisparosJugador:
        print(" ".join(fila))
    print("\nTablero de disparos del oponente:")
    for fila in tableroDisparosOponente:
        print(" ".join(fila))

def colocarBarcos(tablero, barcos, jugador):
    for barco in barcos:
        colocado = False
        while not colocado:
            if jugador == "jugador":
                print(f"Colocando {barco['nombre']} de tamaño {barco['dimension']}")
                fila = int(input("Ingrese la fila (0-4): "))
                columna = int(input("Ingrese la columna (0-4): "))
                orientacion = input("Ingrese la orientación (h para horizontal, v para vertical): ").lower()
            else:
                fila = random.randint(0, len(tablero) - 1)
                columna = random.randint(0, len(tablero) - 1)
                orientacion = random.choice(['h', 'v'])
                
            if validarColocacion(tablero, fila, columna, barco['dimension'], orientacion):
                colocarBarco(tablero, fila, columna, barco['dimension'], orientacion)
                colocado = True
            elif jugador == "jugador":
                print("Colocación inválida. Intenta de nuevo.")

def validarColocacion(tablero, fila, columna, dimension, orientacion):
    if orientacion == 'h':
        if columna + dimension > len(tablero):
            return False
        for i in range(dimension):
            if tablero[fila][columna + i] != "~":
                return False
    else:  # orientación vertical
        if fila + dimension > len(tablero):
            return False
        for i in range(dimension):
            if tablero[fila + i][columna] != "~":
                return False
    return True

def colocarBarco(tablero, fila, columna, dimension, orientacion):
    if orientacion == 'h':
        for i in range(dimension):
            tablero[fila][columna + i] = "B"
    else:
        for i in range(dimension):
            tablero[fila + i][columna] = "B"

def realizarDisparo(tableroOculto, tableroDisparos, fila, columna):
    if tableroOculto[fila][columna] == "B":
        tableroDisparos[fila][columna] = "X"
        tableroOculto[fila][columna] = "H"
        return "Impacto!"
    elif tableroDisparos[fila][columna] == "~":
        tableroDisparos[fila][columna] = "O"
        return "Agua"
    return "Ya disparaste aquí."

def verificarVictoria(tableroOculto):
    for fila in tableroOculto:
        if "B" in fila:
            return False
    return True

def jugarContraComputadora():
    dimension = 5
    tableroJugador = crearTablero(dimension)
    tableroComputadora = crearTablero(dimension)
    tableroDisparosJugador = crearTablero(dimension)
    tableroDisparosComputadora = crearTablero(dimension)
    barcos = [
        {"nombre": "Portaviones", "dimension": 3},
        {"nombre": "Submarino", "dimension": 2}
    ]
    print("Coloca tus barcos:")
    colocarBarcos(tableroJugador, barcos, "jugador")
    colocarBarcos(tableroComputadora, barcos, "computadora")
    turnoJugador = True
    
    while True:
        if turnoJugador:
            print("\nTu turno")
            mostrarTableros(tableroDisparosJugador, tableroDisparosComputadora)
            fila = int(input("Ingresa la fila del disparo (0-4): "))
            columna = int(input("Ingresa la columna del disparo (0-4): "))
            resultado = realizarDisparo(tableroComputadora, tableroDisparosJugador, fila, columna)
            print(resultado)
            if verificarVictoria(tableroComputadora):
                print("¡Ganaste!")
                return "jugador"
        else:
            print("\nTurno de la computadora")
            fila = random.randint(0, dimension - 1)
            columna = random.randint(0, dimension - 1)
            resultado = realizarDisparo(tableroJugador, tableroDisparosComputadora, fila, columna)
            print(f"La computadora disparó en ({fila}, {columna}): {resultado}")
            if verificarVictoria(tableroJugador):
                print("La computadora ganó.")
                return "computadora"
        turnoJugador = not turnoJugador

def jugarDosJugadores():
    dimension = 5
    tableroJugador1 = crearTablero(dimension)
    tableroJugador2 = crearTablero(dimension)
    tableroDisparosJugador1 = crearTablero(dimension)
    tableroDisparosJugador2 = crearTablero(dimension)
    barcos = [
        {"nombre": "Portaviones", "dimension": 3},
        {"nombre": "Submarino", "dimension": 2}
    ]
    print("Jugador 1 coloca tus barcos:")
    colocarBarcos(tableroJugador1, barcos, "jugador")
    print("Jugador 2 coloca tus barcos:")
    colocarBarcos(tableroJugador2, barcos, "jugador")
    turnoJugador1 = True
    
    while True:
        if turnoJugador1:
            print("\nTurno del Jugador 1")
            mostrarTableros(tableroDisparosJugador1, tableroDisparosJugador2)
            fila = int(input("Ingresa la fila del disparo (0-4): "))
            columna = int(input("Ingresa la columna del disparo (0-4): "))
            resultado = realizarDisparo(tableroJugador2, tableroDisparosJugador1, fila, columna)
            print(resultado)
            if verificarVictoria(tableroJugador2):
                print("¡Jugador 1 ganó!")
                return "jugador 1"
        else:
            print("\nTurno del Jugador 2")
            mostrarTableros(tableroDisparosJugador2, tableroDisparosJugador1)
            fila = int(input("Ingresa la fila del disparo (0-4): "))
            columna = int(input("Ingresa la columna del disparo (0-4): "))
            resultado = realizarDisparo(tableroJugador1, tableroDisparosJugador2, fila, columna)
            print(resultado)
            if verificarVictoria(tableroJugador1):
                print("¡Jugador 2 ganó!")
                return "jugador 2"
        turnoJugador1 = not turnoJugador1

def main():
    print("¡Bienvenido a Batalla Naval!")
    modo = input("Elige el modo de juego (1: Contra la computadora, 2: Dos jugadores): ")
    if modo == "1":
        jugarContraComputadora()
    elif modo == "2":
        jugarDosJugadores()
    else:
        print("Modo inválido. Intenta de nuevo.")

if __name__ == "__main__":
    main()   
        