"""Logica de la partida: reparto, comprobaciones y ganador."""
from cartas import calcular_puntos

# --- Bloque A3: reparto y comprobaciones ---
def repartir(baraja, mano, n=1):
    """Saca n cartas de la baraja y las anade a la mano."""
    for _ in range(n):
        mano.append(baraja.pop())


def es_blackjack(mano):
    """Blackjack = 21 con las dos primeras cartas."""
    return len(mano) == 2 and calcular_puntos(mano) == 21


def se_pasa(mano):
    return calcular_puntos(mano) > 21

# --- Bloque A4: banca y ganador ---
def turno_banca(baraja, mano_banca):
    """La banca pide carta hasta llegar a 17 o mas."""
    while calcular_puntos(mano_banca) < 17:
        repartir(baraja, mano_banca)


def determinar_ganador(mano_jugador, mano_banca):
    """Devuelve 'jugador', 'banca' o 'empate'."""
    pj, pb = calcular_puntos(mano_jugador), calcular_puntos(mano_banca)
    bj_j, bj_b = es_blackjack(mano_jugador), es_blackjack(mano_banca)
    if pj > 21:
        return "banca"
    if pb > 21:
        return "jugador"
    if bj_j and not bj_b:
        return "jugador"
    if bj_b and not bj_j:
        return "banca"
    if pj > pb:
        return "jugador"
    if pb > pj:
        return "banca"
    return "empate"
