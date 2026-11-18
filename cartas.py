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