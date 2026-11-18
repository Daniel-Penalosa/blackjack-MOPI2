"""Interaccion con el usuario por terminal."""
# --- Bloque B1: mostrar cartas ---
def texto_carta(carta):
    return f"[{carta[0]}{carta[1]}]"


def mostrar_mano(nombre, mano, puntos, ocultar_segunda=False):
    """Imprime la mano. Si ocultar_segunda, la segunda carta sale tapada."""
    if ocultar_segunda:
        cartas = f"{texto_carta(mano[0])} [??]"
        print(f"{nombre}: {cartas}")
    else:
        cartas = " ".join(texto_carta(c) for c in mano)
        print(f"{nombre}: {cartas}  -> {puntos} puntos")


# --- Bloque B2: preguntar al jugador ---
def pedir_accion():
    """Pregunta hasta recibir 'p' (pedir) o 's' (plantarse)."""
    while True:
        opcion = input("¿Pedir carta (p) o plantarse (s)? ").strip().lower()
        if opcion in ("p", "s"):
            return opcion
        print("Opcion no valida. Escribe p o s.")

