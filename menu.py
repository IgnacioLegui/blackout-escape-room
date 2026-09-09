"""
BLACKOUT — Escape Room Virtual
Módulo de menú y gestión de contraseña.
Integrantes: Leguizamón José Ignacio, Molinari Matias, Martino Tiago, Nuñez Felipe

Resuelve el subproblema de navegación (menú principal) y el cambio de
contraseña, reutilizando encriptar_contraseña() del módulo de autenticación.
Las validaciones de la nueva contraseña están separadas en funciones
chicas y reutilizables (una por regla).

"""
import textwrap

from autenticacion import encriptar_contraseña, CORRIMIENTO

CARACTERES_ESPECIALES = "!@#$%^&*()_+-=[]{}|;:,.<>?/~`"

def mostrar_menu():
    """Muestra las opciones del menú principal por pantalla.

    Parámetros:
        No recibe parámetros.

    Retorna:
        None: Solo produce una salida por pantalla.
    """
    print("\n--- BLACKOUT: Cuenta Regresiva al Final ---")
    print("0. Instrucciones")
    print("1. Jugar")
    print("2. Cambiar contraseña")
    print("3. Cerrar sesión")


def pedir_opcion_menu():
    """Solicita y valida la opción elegida del menú.

    Parámetros:
        No recibe parámetros.

    Retorna:
        int: Opción válida elegida (0, 1, 2 o 3).
    """
    entrada = input("Elija una opción: ")
    while (not entrada.isdigit()) or int(entrada) < 0 or int(entrada) > 3:
        print("ERROR. Debe ingresar un número entre 0 y 3.")
        entrada = input("Elija una opción: ")
    return int(entrada)


def mostrar_instrucciones():
    """Muestra las instrucciones del juego, justificadas a 80 columnas.

    Parámetros:
        No recibe parámetros.

    Retorna:
        None: Solo produce una salida por pantalla.
    """
    texto = (
        "Es la noche del final de Programacion I. Vas viajando a la "
        "facultad cuando, de la nada, se corta la luz en toda la ciudad. "
        "En medio del apagon se te aparece un hombre que nadie mas parece "
        "ver: dice que el mantiene la red electrica funcionando, y que el "
        "corte no fue casualidad. Te ofrece un trato: resolver una serie "
        "de desafios para llegar a la facultad a tiempo para rendir el "
        "final.\n\n"
        "Para superar cada obstaculo vas a tener que resolver los "
        "desafios de cada sala: primero un Ahorcado con palabras propias "
        "de la materia, y despues una Mini Batalla Naval para encontrar "
        "los generadores que te iluminen el camino. Suerte."
    )
    print(textwrap.fill(texto, width=80))


def tiene_mayuscula(texto):
    """Verifica si el texto contiene al menos una letra mayúscula.

    Parámetros:
        texto (str): Texto a analizar.

    Retorna:
        bool: True si contiene al menos una mayúscula, False si no.
    """
    for caracter in texto:
        if caracter.isupper():
            return True
    return False


def tiene_minuscula(texto):
    """Verifica si el texto contiene al menos una letra minúscula.

    Parámetros:
        texto (str): Texto a analizar.

    Retorna:
        bool: True si contiene al menos una minúscula, False si no.
    """
    for caracter in texto:
        if caracter.islower():
            return True
    return False


def tiene_numero(texto):
    """Verifica si el texto contiene al menos un dígito.

    Parámetros:
        texto (str): Texto a analizar.

    Retorna:
        bool: True si contiene al menos un número, False si no.
    """
    for caracter in texto:
        if caracter.isdigit():
            return True
    return False


def tiene_caracter_especial(texto):
    """Verifica si el texto contiene al menos un carácter especial.

    Parámetros:
        texto (str): Texto a analizar.

    Retorna:
        bool: True si contiene al menos un carácter especial, False si no.
    """
    for caracter in texto:
        if caracter in CARACTERES_ESPECIALES:
            return True
    return False


def tiene_espacios(texto):
    """Verifica si el texto contiene algún espacio.

    Parámetros:
        texto (str): Texto a analizar.

    Retorna:
        bool: True si contiene al menos un espacio, False si no.
    """
    for caracter in texto:
        if caracter == " ":
            return True
    return False


def validar_contraseña_nueva(nueva, contraseña_actual_encriptada):
    """Valida que la nueva contraseña cumpla con todas las reglas del TP.

    Parámetros:
        nueva (str): Nueva contraseña ingresada por el jugador, en texto plano.
        contraseña_actual_encriptada (str): Contraseña vigente, ya encriptada.

    Retorna:
        str | None: Mensaje describiendo el primer requisito incumplido,
            o None si la contraseña cumple con todas las reglas.
    """
    error = None
    if len(nueva) < 8:
        error = "debe tener al menos 8 caracteres."
    elif not tiene_mayuscula(nueva):
        error = "debe contener al menos una letra mayúscula."
    elif not tiene_minuscula(nueva):
        error = "debe contener al menos una letra minúscula."
    elif not tiene_numero(nueva):
        error = "debe contener al menos un número."
    elif not tiene_caracter_especial(nueva):
        error = "debe contener al menos un carácter especial."
    elif tiene_espacios(nueva):
        error = "no puede contener espacios."
    elif encriptar_contraseña(nueva, CORRIMIENTO) == contraseña_actual_encriptada:
        error = "debe ser diferente de la contraseña actual."
    return error


def cambiar_contraseña(contraseña_actual_encriptada):
    """Permite modificar la contraseña actual respetando las reglas del TP.

    Solicita primero la contraseña actual para verificarla, y luego pide
    una nueva contraseña hasta que cumpla con todas las reglas de
    seguridad definidas en la consigna.

    Parámetros:
        contraseña_actual_encriptada (str): Contraseña vigente, ya encriptada.

    Retorna:
        str: Nueva contraseña encriptada si el cambio fue exitoso, o la
             misma contraseña recibida si no se pudo verificar la actual.
    """
    contraseña_final = contraseña_actual_encriptada
    actual = input("Ingrese su contraseña actual: ")
    if encriptar_contraseña(actual, CORRIMIENTO) == contraseña_actual_encriptada:
        nueva = input("Ingrese la nueva contraseña: ")
        error = validar_contraseña_nueva(nueva, contraseña_actual_encriptada)
        while error is not None:
            print("ERROR. La contraseña", error)
            nueva = input("Ingrese la nueva contraseña: ")
            error = validar_contraseña_nueva(nueva, contraseña_actual_encriptada)
        contraseña_final = encriptar_contraseña(nueva, CORRIMIENTO)
        print("Contraseña actualizada correctamente.")
    else:
        print("La contraseña actual ingresada es incorrecta.")
    return contraseña_final