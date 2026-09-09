"""
BLACKOUT — Escape Room Virtual
main.py — Punto de entrada de la aplicación.
Integrantes: Leguizamón José Ignacio, Molinari Matias, Martino Tiago, Nuñez Felipe

Orquesta el flujo general: Login -> Menú -> Jugar / Cambiar contraseña /
Cerrar sesión. Cada responsabilidad vive en su propio módulo (ver
README.md para el detalle de la arquitectura).

"""

from autenticacion import encriptar_contraseña, iniciar_sesion, USUARIO_VALIDO, CONTRASEÑA_INICIAL, CORRIMIENTO
from menu import mostrar_menu, pedir_opcion_menu, mostrar_instrucciones, cambiar_contraseña
from ahorcado import jugar_ahorcado
from batalla_naval import jugar_batalla_naval


def jugar():
    """Inicia el recorrido del Escape Room: Sala 1 (Ahorcado) y Sala 2 (Batalla Naval).

    Parámetros:
        No recibe parámetros.

    Retorna:
        bool: True si el jugador superó ambas salas, False si abandonó o
              perdió en alguna de ellas.
    """
    print()
    print("=" * 60)
    print("Es la noche del final de Programación I. De la nada, se corta")
    print("la luz en toda la ciudad. En medio del apagón se te aparece un")
    print("hombre que nadie más parece ver: dice que él mantiene la red")
    print("eléctrica funcionando, y que el corte no fue casualidad.")
    print("Te ofrece un trato: resolver una serie de desafíos para llegar")
    print("a la facultad a tiempo para rendir el final.")
    print("=" * 60)
    print()

    supero_juego = False
    if jugar_ahorcado():
        supero_juego = jugar_batalla_naval()
    return supero_juego


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