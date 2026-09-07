"""
BLACKOUT — Escape Room Virtual
Sala 1 — Ahorcado.

Resuelve el subproblema de la primera sala: el jugador debe descubrir una
palabra oculta relacionada con la temática del juego (vocabulario de
Programación I) antes de agotar la cantidad máxima de intentos.

"""

import random

MAX_INTENTOS_AHORCADO = 6


def elegir_palabra():
    """Elige al azar una palabra del banco de palabras de la temática.

    Parámetros:
        No recibe parámetros.

    Retorna:
        str: Palabra secreta seleccionada para la partida.
    """
    palabras = [
        "ALGORITMO",
        "VARIABLE",
        "FUNCION",
        "ITERACION",
        "RECURSION",
        "ARREGLO",
        "PARAMETRO",
        "CONDICION",
        "ESTRUCTURA",
        "COMPILADOR",
        "DEPURACION",
        "SECUENCIA",
        "BUCLE",
        "CONSTANTE",
        "ALGORITMIA"
    ]
    return random.choice(palabras)


def mostrar_progreso(palabra, letras_usadas):
    """Arma el string de progreso mostrando letras descubiertas y guiones en el resto.

    Parámetros:
        palabra (str): Palabra secreta del juego.
        letras_usadas (list): Letras ingresadas hasta el momento.

    Retorna:
        str: Representación de la palabra con las letras descubiertas visibles.
    """
    progreso = ""
    for letra in palabra:
        if letra in letras_usadas:
            progreso += letra + " "
        else:
            progreso += "_" + " "
    return progreso


def es_letra_valida(letra):
    """Verifica que el ingreso sea un único carácter alfabético.

    Parámetros:
        letra (str): Texto ingresado por el jugador.

    Retorna:
        bool: True si es un solo carácter alfabético, False en caso contrario.
    """
    return len(letra) == 1 and letra.isalpha()


def letra_ya_usada(letra, letras_usadas):
    """Detecta si una letra ya fue ingresada anteriormente.

    Parámetros:
        letra (str): Letra a verificar.
        letras_usadas (list): Letras ingresadas hasta el momento.

    Retorna:
        bool: True si la letra ya estaba registrada, False si no.
    """
    return letra in letras_usadas


def letra_en_palabra(letra, palabra):
    """Verifica si una letra pertenece a la palabra secreta.

    Parámetros:
        letra (str): Letra a verificar.
        palabra (str): Palabra secreta del juego.

    Retorna:
        bool: True si la letra está presente en la palabra, False si no.
    """
    return letra in palabra


def ingresar_letra(letras_usadas):
    """Solicita una letra al jugador, la valida y la registra si es nueva.

    Parámetros:
        letras_usadas (list): Letras ingresadas hasta el momento (se modifica in place).

    Retorna:
        str | None: La letra ingresada en mayúscula si es válida y nueva,
            None si el ingreso fue inválido o ya se había usado.
    """
    letra_valida = None
    letra = input("Ingrese una letra: ").upper()
    if not es_letra_valida(letra):
        print("Debe ingresar una sola letra.")
    elif letra_ya_usada(letra, letras_usadas):
        print("Ya ingresaste esa letra.")
    else:
        letras_usadas.append(letra)
        letra_valida = letra
    return letra_valida


def palabra_completa(palabra, letras_usadas):
    """Verifica si todas las letras de la palabra ya fueron descubiertas.

    Parámetros:
        palabra (str): Palabra secreta del juego.
        letras_usadas (list): Letras ingresadas hasta el momento.

    Retorna:
        bool: True si la palabra fue descubierta por completo, False si no.
    """
    for letra in palabra:
        if letra not in letras_usadas:
            return False
    return True


def jugar_ahorcado(max_intentos=MAX_INTENTOS_AHORCADO):
    """Ejecuta una partida completa de Ahorcado (Sala 1).

    Parámetros:
        max_intentos (int): Cantidad máxima de intentos incorrectos permitidos.

    Retorna:
        bool: True si el jugador descubrió la palabra (victoria),
            False si agotó los intentos (derrota).
    """
    palabra_secreta = elegir_palabra()
    letras_usadas = []
    intentos_restantes = max_intentos
    gano = False

    print()
    print("--- SALA 1: AHORCADO ---")
    while intentos_restantes > 0 and not gano:
        print()
        print(mostrar_progreso(palabra_secreta, letras_usadas))
        print()
        print("Letras usadas:", letras_usadas)
        print("Intentos restantes:", intentos_restantes)

        letra_a_usar = None
        while letra_a_usar is None:
            letra_a_usar = ingresar_letra(letras_usadas)

        if not letra_en_palabra(letra_a_usar, palabra_secreta):
            intentos_restantes -= 1

        gano = palabra_completa(palabra_secreta, letras_usadas)

    print()
    if gano:
        print("¡Ganaste! La palabra era:", palabra_secreta)
    else:
        print("Perdiste. La palabra era:", palabra_secreta)
    print()
    return gano


if __name__ == "__main__":
    jugar_ahorcado()
