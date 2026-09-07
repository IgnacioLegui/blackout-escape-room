"""
BLACKOUT — Escape Room Virtual
Módulo de menú y gestión de contraseña.

Resuelve el subproblema de navegación (menú principal) y el cambio de
contraseña, reutilizando encriptar_contraseña() del módulo de autenticación.

NOTA: cambiar_contraseña() todavía es un placeholder — falta implementar
las 7 validaciones que pide la consigna (longitud, mayúscula, minúscula,
número, carácter especial, sin espacios, distinta de la actual).
"""

from autenticacion import encriptar_contraseña, CORRIMIENTO


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
    opcion = int(input("Elija una opción: "))
    while opcion < 0 or opcion > 3:
        print("ERROR. Opción fuera de rango.")
        opcion = int(input("Elija una opción: "))
    return opcion


def mostrar_instrucciones():
    """Muestra las instrucciones del juego justificadas en 80 columnas.

    Parámetros:
        No recibe parámetros.

    Retorna:
        None: Solo produce una salida por pantalla.
    """
    # TODO: reemplazar por el texto definitivo de la historia
    #  y ambientación de Blackout, justificado a 80 columnas.
    print("Instrucciones: (pendiente de redacción final)")


def cambiar_contraseña(contraseña_actual_encriptada):
    """Permite modificar la contraseña actual respetando las reglas del TP.

    Parámetros:
        contraseña_actual_encriptada (str): Contraseña vigente, ya encriptada.

    Retorna:
        str: Nueva contraseña encriptada si el cambio fue exitoso, o la
             misma contraseña recibida si el jugador canceló o no cumplió
             las validaciones.
    """
    # TODO: implementar las 7 validaciones de la nueva contraseña.
    #  Usar encriptar_contraseña(nueva, CORRIMIENTO) al final para devolver la contraseña ya encriptada.
    print("Función de cambio de contraseña en desarrollo.")
    return contraseña_actual_encriptada
