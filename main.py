"""
BLACKOUT — Escape Room Virtual
main.py — Punto de entrada de la aplicación.
Integrantes: Leguizamón José Ignacio, Martino Tiago, Molinari Matias, Nuñez Felipe

Orquesta el flujo general: Login -> Menú -> Jugar / Cambiar contraseña /
Cerrar sesión. Cada responsabilidad vive en su propio módulo (ver
README.md para el detalle de la arquitectura).


"""

from autenticacion import encriptar_contraseña, iniciar_sesion, USUARIO_VALIDO, CONTRASEÑA_INICIAL, CORRIMIENTO
from menu import mostrar_menu, pedir_opcion_menu, mostrar_instrucciones, cambiar_contraseña


def jugar():
    """Inicia el recorrido del Escape Room: Sala 1 (Ahorcado) y Sala 2 (Batalla Naval).

    Parámetros:
        No recibe parámetros.

    Retorna:
        bool: True si el jugador superó ambas salas, False si abandonó o
              perdió en alguna de ellas.
    """
    # TODO (Martino Tiago / Nuñez Felipe): reemplazar este cuerpo por:
    #   from ahorcado import jugar_ahorcado
    #   from batalla_naval import jugar_batalla_naval
    #   if jugar_ahorcado():
    #       return jugar_batalla_naval()
    #   return False
    # una vez que jugar_ahorcado() esté lista y probada en ahorcado.py.
    print("Sala 1 (Ahorcado) y Sala 2 (Batalla Naval) en desarrollo.")
    return False


def main():
    """Punto de entrada de la aplicación: controla el flujo Login -> Menú.

    Mantiene el estado del jugador durante la ejecución: la contraseña
    vigente (que puede cambiar desde el menú) y si ya completó el juego.

    Parámetros:
        No recibe parámetros.

    Retorna:
        None: Ejecuta el ciclo principal del programa.
    """
    contraseña_vigente = encriptar_contraseña(CONTRASEÑA_INICIAL, CORRIMIENTO)
    juego_completado = False

    sesion_activa = True
    while sesion_activa:
        iniciar_sesion(contraseña_vigente)
        print("¡Bienvenido/a a Blackout,", USUARIO_VALIDO + "!")

        en_menu = True
        while en_menu:
            mostrar_menu()
            opcion = pedir_opcion_menu()
            if opcion == 0:
                mostrar_instrucciones()
            elif opcion == 1:
                juego_completado = jugar()
            elif opcion == 2:
                contraseña_vigente = cambiar_contraseña(contraseña_vigente)
            elif opcion == 3:
                print("Cerrando sesión...")
                en_menu = False


main()
