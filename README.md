# blackjack-pareja

Blackjack por terminal hecho en Python como práctica de trabajo colaborativo con Git y GitHub.

## Integrantes
- Daniel Peñalosa Álvarez (Daniel-Penalosa) – lógica del juego: baraja, puntuación, banca y ganador.
- Hugo Mateo Posluszna (CachopoDabuela) – interfaz por terminal, desarrollo de la partida y documentación.

## Cómo ejecutarlo
Requisitos: Python 3.8 o superior. Sin librerías externas.

```bash
git clone https://github.com/USUARIO_A/blackjack-pareja.git
cd blackjack-pareja
python main.py
```
(En Mac/Linux puede ser `python3 main.py`.)

## Cómo se juega
1. Se reparten dos cartas al jugador y dos a la banca (una de la banca queda tapada).
2. El jugador pide carta (`p`) o se planta (`s`). Si supera 21, pierde.
3. La banca destapa y pide carta hasta llegar a 17 o más.
4. Gana quien tenga más puntos sin pasarse de 21. Un Blackjack (21 con dos cartas) gana a cualquier otro 21.

Valores: 2-10 su número, J/Q/K valen 10, el As vale 11 o 1 según convenga.

## Organización de los archivos
| Archivo | Contenido |
|---|---|
| `main.py` | Punto de entrada y bucle de la partida |
| `cartas.py` | Creación de la baraja y cálculo de puntos |
| `juego.py` | Reparto, Blackjack, pasarse de 21, turno de la banca y ganador |
| `interfaz.py` | Mostrar manos, pedir acciones y mostrar resultados |
| `.gitignore` | Archivos que Git no debe seguir |

## Funcionalidades
- Baraja de 52 cartas barajada en cada partida.
- Carta oculta de la banca durante el turno del jugador.
- As con valor 1 u 11 automático.
- Detección de Blackjack y de pasarse de 21.
- Validación de la entrada del jugador.
- Varias partidas seguidas.
