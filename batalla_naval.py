"""
BLACKOUT — Escape Room Virtual
Sala 2 — Escaneo de la Red Eléctrica (Mini Batalla Naval)
Integrantes: Leguizamón José Ignacio, Molinari Matias, Martino Tiago, Nuñez Felipe

Resuelve el subproblema de la segunda sala. jugar_batalla_naval() es el
punto de entrada, pensado para importarse desde main.py e integrarse al
flujo completo (Login -> Menú -> Sala 1: Ahorcado -> Sala 2: Batalla Naval).

"""

import random

FILAS = 5
COLUMNAS = 5
CANTIDAD_BARCOS = 3
DISPAROS_MAXIMOS = 8  # cantidad de intentos de escaneo definida por el equipo

AGUA = "~"      # posición todavía no escaneada
IMPACTO = "X"   # posición escaneada donde había un generador
FALLO = "O"     # posición escaneada sin generador


def crear_tablero_visible(filas, columnas):
    """Crea la grilla que ve el jugador, completamente sin escanear.

    Parámetros:
        filas (int): Cantidad de filas del tablero.
        columnas (int): Cantidad de columnas del tablero.

    Retorna:
        list: Matriz (lista de listas) de filas x columnas, con todas
            las posiciones inicializadas en AGUA.
    """
    tablero = []
    for f in range(filas):
        tablero.append([])
        for c in range(columnas):
            tablero[f].append(AGUA)
    return tablero


def mostrar_tablero(tablero):
    """Imprime la grilla actual con números de fila y columna.

    Parámetros:
        tablero (list): Matriz (lista de listas) a mostrar por pantalla.

    Retorna:
        None: Solo produce una salida por pantalla.
    """
    encabezado = "     "
    for columna in range(len(tablero[0])):
        encabezado = encabezado + str(columna + 1) + "   "
    print(encabezado)

    for fila in range(len(tablero)):
        linea = " " + str(fila + 1) + " |"
        for columna in range(len(tablero[fila])):
            linea = linea + " " + tablero[fila][columna] + " |"
        print(linea)
    print()


def son_adyacentes(fila1, columna1, fila2, columna2):
    """Indica si dos posiciones están juntas: horizontal, vertical o
    diagonalmente (diferencia de a lo sumo 1 en fila y en columna).

    Parámetros:
        fila1 (int): Fila de la primera posición.
        columna1 (int): Columna de la primera posición.
        fila2 (int): Fila de la segunda posición.
        columna2 (int): Columna de la segunda posición.

    Retorna:
        bool: True si las posiciones son adyacentes (o iguales), False si no.
    """
    diferencia_fila = abs(fila1 - fila2)
    diferencia_columna = abs(columna1 - columna2)
    return diferencia_fila <= 1 and diferencia_columna <= 1


def posicion_valida(fila, columna, barcos):
    """Verifica que la posición no esté ocupada ni sea adyacente a un
    generador ya ubicado.

    Parámetros:
        fila (int): Fila de la posición a verificar.
        columna (int): Columna de la posición a verificar.
        barcos (list): Lista de posiciones [fila, columna] ya ubicadas.

    Retorna:
        bool: True si la posición es válida para ubicar un nuevo
            generador, False si está ocupada o es adyacente a otro.
    """
    for barco in barcos:
        if son_adyacentes(fila, columna, barco[0], barco[1]):
            return False
    return True


def generar_flota(filas, columnas, cantidad_barcos):
    """Genera aleatoriamente las posiciones de los generadores ocultos,
    sin que queden en posiciones repetidas ni adyacentes entre sí.

    Parámetros:
        filas (int): Cantidad de filas del tablero.
        columnas (int): Cantidad de columnas del tablero.
        cantidad_barcos (int): Cantidad de generadores a ubicar.

    Retorna:
        list: Lista de posiciones [fila, columna], una por generador.
    """
    barcos = []
    while len(barcos) < cantidad_barcos:
        fila = random.randint(0, filas - 1)
        columna = random.randint(0, columnas - 1)
        if posicion_valida(fila, columna, barcos):
            barcos.append([fila, columna])
    return barcos


def hay_barco_en(fila, columna, barcos):
    """Indica si en la posición dada hay un generador.

    Parámetros:
        fila (int): Fila a consultar.
        columna (int): Columna a consultar.
        barcos (list): Lista de posiciones [fila, columna] de los generadores.

    Retorna:
        bool: True si hay un generador en esa posición, False si no.
    """
    for barco in barcos:
        if barco[0] == fila and barco[1] == columna:
            return True
    return False


def pedir_numero_valido(mensaje, minimo, maximo):
    """Pide un número entero por teclado hasta que el jugador ingrese
    un valor válido dentro del rango [minimo, maximo].

    Parámetros:
        mensaje (str): Texto que se muestra al pedir el dato.
        minimo (int): Valor mínimo aceptado (inclusive).
        maximo (int): Valor máximo aceptado (inclusive).

    Retorna:
        int: Número entero válido ingresado por el jugador.
    """
    entrada = input(mensaje)
    while (not entrada.isdigit()) or int(entrada) < minimo or int(entrada) > maximo:
        print("ERROR: ingresá un número entero entre", minimo, "y", maximo)
        entrada = input(mensaje)
    return int(entrada)


def pedir_coordenada_disparo(tablero_visible):
    """Pide fila y columna del próximo escaneo, validando que la
    posición exista en el tablero y no haya sido escaneada antes.
    Un ingreso inválido no consume un intento.

    Parámetros:
        tablero_visible (list): Matriz que ve el jugador, para chequear
            si la posición ya fue escaneada.

    Retorna:
        tuple: fila (int) y columna (int) válidas, en índices desde 0.
    """
    while True:
        fila = pedir_numero_valido("Fila a escanear (1-5): ", 1, FILAS) - 1
        columna = pedir_numero_valido("Columna a escanear (1-5): ", 1, COLUMNAS) - 1
        if tablero_visible[fila][columna] == AGUA:
            return fila, columna
        print("Esa posición ya fue escaneada. Elegí otra.")
        print()


def procesar_disparo(fila, columna, barcos, barcos_hundidos, tablero_visible):
    """Aplica el escaneo sobre la grilla, actualiza el tablero visible
    y registra el resultado.

    Parámetros:
        fila (int): Fila escaneada.
        columna (int): Columna escaneada.
        barcos (list): Lista de posiciones [fila, columna] de los generadores.
        barcos_hundidos (list): Lista de posiciones ya encontradas (se
            modifica in place si hay impacto).
        tablero_visible (list): Matriz que ve el jugador (se modifica
            in place con el resultado del escaneo).

    Retorna:
        None: Modifica barcos_hundidos y tablero_visible directamente.
    """
    print()
    if hay_barco_en(fila, columna, barcos):
        tablero_visible[fila][columna] = IMPACTO
        barcos_hundidos.append([fila, columna])
        print("¡IMPACTO! Generador localizado y reactivado.")
    else:
        tablero_visible[fila][columna] = FALLO
        print("AGUA. No hay nada en esa posición.")


def informar_estado(disparos_restantes, barcos_hundidos, cantidad_barcos):
    """Muestra el resumen de la jugada: generadores encontrados,
    restantes e intentos de escaneo disponibles.

    Parámetros:
        disparos_restantes (int): Cantidad de disparos que le quedan al jugador.
        barcos_hundidos (list): Lista de posiciones de generadores ya encontrados.
        cantidad_barcos (int): Cantidad total de generadores en el tablero.

    Retorna:
        None: Solo produce una salida por pantalla.
    """
    print("Generadores encontrados:", len(barcos_hundidos), "de", cantidad_barcos)
    print("Generadores restantes:", cantidad_barcos - len(barcos_hundidos))
    print("Intentos de escaneo restantes:", disparos_restantes)
    print()


def revelar_flota(tablero_visible, barcos):
    """Muestra en el tablero todas las posiciones de los generadores,
    hayan sido encontrados o no.

    Parámetros:
        tablero_visible (list): Matriz que ve el jugador (se modifica
            in place para mostrar los generadores no encontrados).
        barcos (list): Lista de posiciones [fila, columna] de los generadores.

    Retorna:
        None: Modifica tablero_visible y lo muestra por pantalla.
    """
    for barco in barcos:
        fila = barco[0]
        columna = barco[1]
        if tablero_visible[fila][columna] != IMPACTO:
            tablero_visible[fila][columna] = "B"
    mostrar_tablero(tablero_visible)


def jugar_batalla_naval():
    """Punto de entrada de la Sala 2: ejecuta una partida completa.

    Parámetros:
        No recibe parámetros.

    Retorna:
        bool: True si el jugador encontró los 3 generadores antes de
            quedarse sin intentos de escaneo (victoria), False si no
            (derrota).
    """
    print("=" * 60)
    print("SALA 2 - ESCANEO DE LA RED ELÉCTRICA")
    print("=" * 60)
    print("El guardián de la red te lleva ante una vieja terminal.")
    print("\"El sabotaje escondió generadores de emergencia en esta")
    print("cuadrícula. Encontralos a todos antes de quedarte sin")
    print("intentos, o la ciudad se queda a oscuras para siempre.\"")
    print()

    tablero_visible = crear_tablero_visible(FILAS, COLUMNAS)
    barcos = generar_flota(FILAS, COLUMNAS, CANTIDAD_BARCOS)
    barcos_hundidos = []
    disparos_restantes = DISPAROS_MAXIMOS

    while disparos_restantes > 0 and len(barcos_hundidos) < CANTIDAD_BARCOS:
        mostrar_tablero(tablero_visible)
        fila, columna = pedir_coordenada_disparo(tablero_visible)
        procesar_disparo(fila, columna, barcos, barcos_hundidos, tablero_visible)
        disparos_restantes = disparos_restantes - 1
        print()
        informar_estado(disparos_restantes, barcos_hundidos, CANTIDAD_BARCOS)

    supero_sala = len(barcos_hundidos) == CANTIDAD_BARCOS
    if supero_sala:
        mostrar_tablero(tablero_visible)
        print("¡Restauraste la energía de la red! Superaste la Sala 2.")
    else:
        print("Se acabaron los intentos de escaneo. La red sigue apagada.")
        print("Estas eran las posiciones de los generadores:")
        revelar_flota(tablero_visible, barcos)
        print("No lograste superar la Sala 2. El examen se rendirá sin vos...")
    return supero_sala


if __name__ == "__main__":
    jugar_batalla_naval()
