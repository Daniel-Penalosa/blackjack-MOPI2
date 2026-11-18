"""Punto de entrada del Blackjack. Ejecutar: python main.py"""
from cartas import crear_baraja, calcular_puntos
from juego import repartir, es_blackjack, se_pasa, turno_banca, determinar_ganador
from interfaz import mostrar_mano, pedir_accion, otra_partida, mostrar_resultado


# --- Bloque B4: desarrollo de la partida ---
def jugar_partida():
    baraja = crear_baraja()
    jugador, banca = [], []
    repartir(baraja, jugador, 2)
    repartir(baraja, banca, 2)

    print("\n--- Nueva partida ---")
    mostrar_mano("Banca", banca, calcular_puntos(banca), ocultar_segunda=True)
    mostrar_mano("Tu", jugador, calcular_puntos(jugador))

    # Turno del jugador
    if es_blackjack(jugador):
        print("¡Blackjack!")
    else:
        while not se_pasa(jugador) and pedir_accion() == "p":
            repartir(baraja, jugador)
            mostrar_mano("Tu", jugador, calcular_puntos(jugador))
        if se_pasa(jugador):
            print("Te has pasado de 21.")

    # Turno de la banca (solo si el jugador no se ha pasado)
    if not se_pasa(jugador):
        turno_banca(baraja, banca)
    print()
    mostrar_mano("Banca", banca, calcular_puntos(banca))
    mostrar_mano("Tu", jugador, calcular_puntos(jugador))
    mostrar_resultado(determinar_ganador(jugador, banca))


def main():
    print("=== BLACKJACK ===")
    while True:
        jugar_partida()
        if not otra_partida():
            print("¡Hasta la proxima!")
            break


if __name__ == "__main__":
    main()

