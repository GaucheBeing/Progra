from tarea3b_escenario import *


# bombanya: int int any -> None
# programa interactivo que simula las acciones del juego
# usando el objeto Escenario definido en otro archivo
def bombanya(N, bombas=3, hint=False):
    assert type(N) == type(bombas) == int,      "Aquí debe ir un número entero ^-^"
    # mensajes de bienvenida
    print("Ayudemos a Anya a salvar la ciudad!")
    print("")
    print("Hay 3 bombas repartidas en la ciudad")
    print("Buscaremos en los cuadrantes de la ciudad si hay bombas escondidas")

    # iniciar la ciudad con el objeto Escenario
    ciudad = Escenario(N, bombas)

    # mientras queden intentos
    while ciudad.intentosRestantes() > 0:

        # logica de mostrar el estado actual del juego
        ciudad.getBombas()
        ciudad.mostrarMapa()
        b = ciudad.bombasRestantes()
        intentos = ciudad.intentosRestantes()
        print("")
        print("Quedan", b, "bombas en la ciudad")
        print("Quedan", intentos, "intentos de busqueda antes de que exploten todas las bombas")
        print("")
        
        # logica de obtener coordenadas de un cuadrante
        print("Ingrese coordenadas del cuadrante a investigar")

        fila = input("fila: ")
        if fila.lower() in ["salir()", "salir", "quit()", "quit"]:
            print("\nHasta pronto!")
            return None
        if not fila.isnumeric():
            print("Aquí debe ir un número entero, intenta otra vez\n")
            continue
        fila = int(fila)
        if not fila < N:
            print(f"Aquí debe ir un número entero menor que {N}\n")
            continue

        columna = input("columna: ")
        if columna.lower() in ["salir()", "salir", "quit()", "quit"]:
            print("\nHasta pronto!")
            return None
        if not columna.isnumeric():
            print("Aquí debe ir un número entero, intenta otra vez\n")
            continue
        columna = int(columna)
        if not columna < N:
            print(f"Aquí debe ir un número entero menor que {N}\n")
            continue

        print("")

        # logica de revisar si habia una bomba en el cuadrante
        print("Buscando en el cuadrante (",fila,columna,")...")
        if ciudad.desactivarBomba(fila,columna):
            print("")
            print("Se ha encontrado una bomba en este cuadrante")
            print("y ha sido desactivada")
            print("")
        else:
            print("")
            print("No se ha encontrado una bomba en este cuadrante")
            print("")

            # --- Extra ---
            if hint not in [False, "no", 'n', 0]:
                print(f"La bomba más próxima se encuentra a una distancia de {ciudad.distancia(fila,columna)} bloques")
                print("")
            # -------------

        # logica de revisar si se gano el juego
        if ciudad.aSalvo():
            print("")
            print("Todas las bombas han sido encontradas!")
            print("Anya esta muy feliz de haber salvado la ciudad")
            print("(Good ending del juego, felicidades!)")

            return None            


    # logica si se perdio el juego
    print("")
    print("Oh no, se acabaron los intentos")
    b = ciudad.bombasRestantes()
    print("Han explotado", b, "bombas")
    print("Lamentablemente no lograste desactivarlas todas")
    print("La ciudad ha sido dañada y mucha gente ha quedado herida :(")
    print("Anya esta triste :c")
    print("(Bad ending del juego, intentalo denuevo)")
    return None

