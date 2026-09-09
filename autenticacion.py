"""
BLACKOUT — Escape Room Virtual
Módulo de autenticación y seguridad.
Integrantes: Leguizamón José Ignacio, Molinari Matias, Martino Tiago, Nuñez Felipe

Resuelve el subproblema de login: encriptación de contraseña y validación
de credenciales. encriptar_contraseña() es reutilizable — el módulo de
menú (menu.py) también la usa al implementar el cambio de contraseña.

"""

USUARIO_VALIDO = "jugador"
CONTRASEÑA_INICIAL = "Chipa2026!"
CORRIMIENTO = 3  # desplazamiento del cifrado César


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
