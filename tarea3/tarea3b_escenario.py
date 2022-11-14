from random import randint
from math import ceil
from copy import deepcopy

# mapa: list(list)
# bombas: list(list)
# intentos: int
# largo: int
class Escenario:

    # Constructor: int -> Escenario
    def __init__(self, largo, bombas=3):
        assert type(largo) == int, "El numero ingresado no es entero"
        assert largo >= 3, "La ciudad debe ser de tamaño mayor o igual a 3"
        assert 1 < bombas < ceil(largo**2/2)

        # establecer campos largo e intentos
        self.__largo = largo
        self.__intentos = ceil(largo**2 *3/4)

        # establecer campo mapa
        M = []
        for i in range(largo):
            L = []
            for j in range(largo):
                L.append("-")

            M.append(L)

        self.__mapa = M

        # establecer campo bombas
        B = []
        k = 0
        while k < bombas:
            L = [randint(0,largo-1), randint(0,largo-1)]
            if L not in B:
                B.append(L)
                k = k + 1 
        self.__bombas = B

        # lista de bombas para testear:
        # self.__bombas = [[0,0],[1,2],[3,1]]
        # self.__bombas = [[0,2],[1,0],[2,1]]
        return None

    # --- Getters de la Clase ---
    # (No es necesario hacer setters)


    # getLargo: None -> int
    def getLargo(self):
        return self.__largo

    # getMapa: None -> list(list)
    def getMapa(self):
        return deepcopy(self.__mapa)

    # getBombas: None -> list(list)
    def getBombas(self):
        return deepcopy(self.__bombas)

    # getIntentos: None -> int
    def getIntentos(self):
        return self.__intentos   


    # --- Metodos a implementar ---        

    # mostrarMapa: None -> None
    # Imprime en pantalla el estado actual del mapa
    def mostrarMapa(self):
        mapa = self.__mapa
        for fila in mapa:
            print(f"{' '.join(fila)}")


    # intentosRestantes: None -> int
    # Indica cuantos intentos quedan para encontrar las bombas
    def intentosRestantes(self):
        intentos = self.__intentos
        return intentos

    # bombasRestantes: None -> int
    # Indica cuantas bombas quedan en el campo __bombas
    def bombasRestantes(self):
        Lbombas = self.__bombas
        return len(Lbombas)


    # aSalvo: None -> bool
    # Entrega True si es que la lista de __bombas está vacía, y False si no
    def aSalvo(self):
        Lbombas = self.__bombas
        return Lbombas == []    


    # desactivarBomba: int int -> bool
    # Dado una par de coordenadas, revisa si hay una bomba en ese lugar
    def desactivarBomba(self, fil, col):
        assert type(fil) == type(col) == int
        assert fil < self.__largo and col < self.__largo,       "Las coordenadas están fuera del mapa"
        if self.__mapa[fil][col] == '-':
            for bomba in self.__bombas:
                if bomba[0] == fil and bomba[1] == col:
                    self.__bombas.remove(bomba)
                    self.__mapa[fil][col] = 'X'
                    self.__intentos -= 1                
                    return True
                else:
                    self.__mapa[fil][col] = 'O'
                    self.__intentos -= 1                
                    return False

    # ---- Extra ----    

    # esta fue la primera función que hicimos en la tarea 1
    # distancia: int int -> int
    # Dado una par de coordenadas, determina su distancia respecto a la bomba más cercana
    def distancia(self, fil, col):
        assert type(fil) == type(col) == int
        assert fil < self.__largo and col < self.__largo,       "Las coordenadas están fuera del mapa"
        Ldistancias = []
        for bomba in self.__bombas:
            Ldistancias.append(int(abs(fil-bomba[0])+abs(col-bomba[1])))
        return min(Ldistancias)

    # ---------------


# --- Fin Clase Escenario ---