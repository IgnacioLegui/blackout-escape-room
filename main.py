# ============================================================
# BLACKOUT — Escape Room Virtual
# Programación I - TPO Trabajo en clase 09_08 (entrega preliminar)
# Integrantes: Leguizamón José Ignacio, Martino Tiago, Molinari Matias y Nuñez Felipe
# ============================================================

USUARIO_VALIDO = "jugador"
CONTRASEÑA_INICIAL = "Chipa2026!"
CORRIMIENTO = 3  # desplazamiento del cifrado César

# ============================================================
# MÓDULO A — SEGURIDAD
# ============================================================

def encriptar_contraseña(contraseña, corrimiento):
    """Encripta una contraseña aplicando un cifrado César (corrimiento de caracteres).

    Parámetros:
        contraseña (str): Contraseña en texto plano.
        corrimiento (int): Cantidad de posiciones a desplazar cada caracter.

    Retorna:
        str: Contraseña encriptada.
    """
    encriptada = ""
    for caracter in contraseña:
        encriptada = encriptada + chr(ord(caracter) + corrimiento)
    return encriptada


# ============================================================
# MÓDULO A — LOGIN
# ============================================================

def pedir_credenciales():
    """Solicita usuario y contraseña por teclado.

    Parámetros:
        No recibe parámetros.

    Retorna:
        tuple: usuario ingresado (str) y contraseña ingresada (str).
    """
    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")
    return usuario, contraseña


def validar_login(usuario, contraseña, contraseña_valida_encriptada):
    """Valida las credenciales ingresadas contra las almacenadas.

    Parámetros:
        usuario (str): Usuario ingresado por el jugador.
        contraseña (str): Contraseña ingresada por el jugador (sin encriptar).
        contraseña_valida_encriptada (str): Contraseña vigente, ya encriptada.

    Retorna:
        bool: True si las credenciales son correctas, False en caso contrario.
    """
    contraseña_encriptada = encriptar_contraseña(contraseña, CORRIMIENTO)
    if usuario == USUARIO_VALIDO and contraseña_encriptada == contraseña_valida_encriptada:
        return True
    return False


def iniciar_sesion(contraseña_valida_encriptada):
    """Controla el ciclo de login, permitiendo reintentos ante credenciales inválidas.

    Parámetros:
        contraseña_valida_encriptada (str): Contraseña vigente, ya encriptada.

    Retorna:
        None: Solo retorna cuando el login fue exitoso.
    """
    autenticado = False
    while not autenticado:
        usuario, contraseña = pedir_credenciales()
        autenticado = validar_login(usuario, contraseña, contraseña_valida_encriptada)
        if not autenticado:
            print("Usuario o contraseña incorrectos. Intente nuevamente.")


# ============================================================
# MÓDULO A — ESQUELETO DE LA APLICACIÓN
# ============================================================

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


# ============================================================
# STUBS DE OTROS MÓDULOS
# ============================================================

def mostrar_menu():
    pass  # A DESARROLLAR


def pedir_opcion_menu():
    pass  # A DESARROLLAR
    return 3


def mostrar_instrucciones():
    pass  # A DESARROLLAR


def cambiar_contraseña(contraseña_actual_encriptada):
    pass  # A DESARROLLAR
    return contraseña_actual_encriptada


def jugar():
    pass  # A DESARROLLAR
    return False


main()