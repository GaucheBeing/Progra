import tarea1_funciones
# from tarea1_funciones import *

# Entradas-Salida: None -> None
# Funcionalidad: Iniciar, introducir y asignar variables base del juego
def inicioJuego():
    # Introducción e instructivo para poder jugar
    print("Hey mortal! Anya necesita de tu ayuda para encontrar los " '\033[1m' + "Documentos Espias Super Secretos (DESS)! \n" + '\033[0m')
    instructivo = input("Antes de empezar humanx puedes escribir ayuda para recibir info adicional")
    if instructivo == "ayuda":
        print('\033[1m' + "Distancia" + '\033[0m'": Muestra a cuántos pasos horizontales y/o verticales estás de un DESS \n" '\033[1m' + "Ubicación" + '\033[0m'": Indica la posición actual de Anya\n\nControles: \n    " '\033[1m' + "w" + '\033[0m' " = arriba \n    " '\033[1m' + "s" + '\033[0m' " = abajo \n    " '\033[1m' + "a" + '\033[0m' " = izquierda \n    " '\033[1m' + "d" + '\033[0m' " = derecha\n\nAhora sí, partamos!! \n")
    else: print("Entonces partamos!! \n")
    
    # Generar ubicación del objetivo y asignar la posición base del jugador
    (xDESS, yDESS) = (tarea1_funciones.numeroAleatorio(-50,50), tarea1_funciones.numeroAleatorio(-50,50))
    return cicloJuego(0, 0, xDESS, yDESS)

# Entradas-Salida: int int int int -> None
# Funcionalidad: Displayar información del objetivo y jugador, solicitar su jugada y comenzar/seguir/terminar la recursión/juego
def cicloJuego(xAnya, yAnya, xDESS, yDESS):
    # Indicarle al jugador la distancia del objetivo y su ubicación
    print('\033[1m' + "Distancia:" + '\033[0m', tarea1_funciones.distancia(xAnya, yAnya, xDESS, yDESS), "\n" '\033[1m' + "Ubicación:" + '\033[0m', (xAnya, yAnya), "\n")

    # Pedirle al usuario su jugada y asignarle los cambios a su ubicación
    paso = input("¿A dónde te quieres mover?")
    cantPaso = int(input("¿Cuántos pasos?"))
    (despX, despY) = (0, 0)
    if paso == "w" or paso == "arriba":
        despY = 1*cantPaso
    elif paso == "s" or paso == "abajo":
        despY = -1*cantPaso
    elif paso == "a" or paso == "izquierda":
        despX = -1*cantPaso
    elif paso == "d" or paso == "derecha":
        despX = 1*cantPaso
    else: (despX, despY) = (0, 0)
    (xAnya, yAnya) = (xAnya+despX, yAnya+despY)
    
    # Chequear por cada recursión si el jugador ganó, en tal caso preguntar si seguir o terminar la recursión 
    if tarea1_funciones.encontrado(xAnya, yAnya, xDESS, yDESS):
        print("Enhorabuena mortal, lo lograsté! \n")
        resp = input("¿Quieres seguir? \n Y o N")
        if resp == "Y" or resp == "y" or resp == "si" or resp == "sí" or resp == "1":
            return inicioJuego()
        elif resp == "N" or resp == "n" or resp == "no" or resp == "0":
            return print("Entonces hasta la próxima mortal \n ^-^")
        else:
            print("Asumiré que no quieres seguir pequeño mortal, hasta la próxima \n ^-^")
            return None
    else: None
    
    # Chequear si el jugador se encuentra fuera de los límites, en tal caso parte en el origen
    if tarea1_funciones.fueraCuadrado(xAnya, yAnya):
        (xAnya, yAnya) = (0, 0)
        print("Opa! te saliste del radar, Loid te devolvió a casa")

    return cicloJuego(xAnya, yAnya, xDESS, yDESS)
