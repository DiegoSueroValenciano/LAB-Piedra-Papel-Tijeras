import random

def ordenador_decide_jugada():
    opciones = ["piedra", "papel", "tijeras"]
    res = random.choice(opciones)
    return res

def usuario_decide_jugada():
    eleccion_usuario = input("Elige piedra, papel o tijeras: ")
    while eleccion_usuario not in ["piedra", "papel", "tijeras"]:
        eleccion_usuario = input("Opción no válida, por favor elige piedra, papel o tijeras: ")
    return eleccion_usuario

def determina_ganador(jugada_usuario, jugada_ordenador):
    if jugada_usuario == jugada_ordenador:
        return "Empate"
    elif jugada_usuario == "piedra" and jugada_ordenador == "tijeras":
        return "Ganaste"
    elif jugada_usuario == "tijeras" and jugada_ordenador == "papel":
        return "Ganaste"
    elif jugada_usuario == "papel" and jugada_ordenador == "piedra":
        return "Ganaste"
    else:
        return "Perdiste"

def jugar():
    print('Bienvenido, vamos a jugar a piedra papel o tijera')
    jugada_ordenador = ordenador_decide_jugada()
    jugada_usuario = usuario_decide_jugada()
    print('El ordenador elige', jugada_ordenador)
    print('El usuario elige', jugada_usuario)
    ganador = determina_ganador(jugada_usuario, jugada_ordenador)
    print('El resultado es:', ganador)
    return ganador

def jugar_torneo(puntuacion=3):
    puntuacion_jugador = 0
    puntuacion_maquina = 0
    
    while puntuacion_jugador < puntuacion and puntuacion_maquina < puntuacion:
        resultado = jugar()
        if resultado == "Ganaste":
            puntuacion_jugador += 1
        elif resultado == "Perdiste":
            puntuacion_maquina += 1

        print(f"Puntuación -> Usuario: {puntuacion_jugador}, Ordenador: {puntuacion_maquina}")
    
    if puntuacion_jugador == puntuacion:
        print("¡Has ganado el torneo! Maquina.")
    else:
        print("Has perdido el torneo, pringao")

if __name__ == "__main__":
    jugar_torneo(5)
