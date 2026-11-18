"""Gestion de la baraja y de la puntuacion de las cartas."""
import random

# --- Bloque A1: crear y barajar la baraja ---
PALOS = ["♠", "♥", "♦", "♣"]
VALORES = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]


def crear_baraja():
    """Devuelve una baraja de 52 cartas barajada. Cada carta es (valor, palo)."""
    baraja = [(valor, palo) for palo in PALOS for valor in VALORES]
    random.shuffle(baraja)
    return baraja


# --- Bloque A2: puntuacion ---
def valor_carta(carta):
    """Valor base de una carta: figuras 10, As 11, resto su numero."""
    valor = carta[0]
    if valor in ("J", "Q", "K"):
        return 10
    if valor == "A":
        return 11
    return int(valor)


def calcular_puntos(mano):
    """Suma la mano; cada As pasa de 11 a 1 mientras la mano supere 21."""
    puntos = sum(valor_carta(c) for c in mano)
    ases = sum(1 for c in mano if c[0] == "A")
    while puntos > 21 and ases:
        puntos -= 10
        ases -= 1
    return puntos
