# Blackout — Escape Room Virtual

Trabajo Práctico de Programación I (UADE) — Equipo 01: Fullstack Chipá.

## Historia

Es la noche del final de Programación I. Vas viajando a la facultad
cuando, de la nada, se corta la luz en toda la ciudad. En medio del
apagón se te aparece un hombre que nadie más parece ver: dice que él
mantiene la red eléctrica funcionando, y que el corte no fue casualidad.
Te ofrece un trato — resolver una serie de desafíos para llegar a la
facultad a tiempo para rendir el final.

## Equipo

| Integrante | Responsabilidad |
|---|---|
| Leguizamón José Ignacio | Login, seguridad y esqueleto de la app |
| Molinari Matias | Menú y cambio de contraseña |
| Martino Tiago | Diseño de niveles (salas) |
| Nuñez Felipe | Diseño de niveles (contenido técnico) |

## Cómo ejecutar

Requiere Python 3. No usa librerías externas, solo módulos de la librería estándar (random y textwrap).

```
python main.py
```

Usuario de prueba: `jugador` — Contraseña: `Chipa2026!`

## Estructura del proyecto

```
main.py            → punto de entrada, orquesta el flujo general
autenticacion.py    → login y encriptación de contraseña (cifrado César)
menu.py             → menú principal y cambio de contraseña
ahorcado.py         → Sala 1
batalla_naval.py    → Sala 2
```
