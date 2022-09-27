from re import S
import estructura
from lista import *


# deficion estructura sangre
# Sangre: cod(int) tipo(str) rh(str)
estructura.crear('Sangre', 'cod tipo rh')

# definicion de sangres de ejemplo
S1 = Sangre(127, 'A', '+')
S2 = Sangre(510, 'B', '-')
S3 = Sangre(460, 'AB', '-')
S4 = Sangre(637, 'B', '-')
S5 = Sangre(174, 'B', '+')
S6 = Sangre(809, 'AB', '+')
S7 = Sangre(331, 'B', '-')
S8 = Sangre(803, 'O', '-')
S9 = Sangre(648, 'B', '-')
S0 = Sangre(207, 'O', '-')

SS1 = Sangre(839, 'O', '+')
SS2 = Sangre(308, 'AB', '+')
SS3 = Sangre(124, 'B', '+')

# definicion de listas de sangre de ejemplo
LS1 = lista(S1, lista(S2, lista(S3, lista(S4, lista(S5, \
       lista(S6, lista(S7, lista(S8, lista(S9, lista(S0, listaVacia))))))))))

LS2 = lista(SS1, lista(SS2, lista(SS3, listaVacia)))


# universal: lista(Sangre) -> int
# Función: dada una lista de Sangre, cuente cuanta sangre hay del tipo O con factor RH negativo
# Ej: universal(LS1) y universal(LS2) han de retornar 2 y 0 respectivamente
def universal(listaS):
       assert esLista(listaS)
       def _universal(listaS):
              # caso base
              if listaS == None:
                     return 0
              else:
                     # chequear los atributos 'tipo' y 'rh' de elementos (Sangre) de una lista recursivamente
                     elementS = cabeza(listaS)
                     if elementS.tipo == 'O' and elementS.rh == "-":
                            return 1 + _universal(cola(listaS))
                     else:
                            return 0 + _universal(cola(listaS))
       # correr la subfunción hasta terminar la lista dada
       return _universal(listaS)
# Test:
assert universal(LS1) == 2
assert universal(LS2) == 0

# soloTipo: lista(Sangre) str -> lista(Sangre) 
# Función: dada una lista de Sangre y un tipo, entregar una lista que solo contenga Sangre del tipo indicado
# Ej1: soloTipo(LS1, "AB") debería entregar una lista con Sangre de códigos 460 y 809
# Ej2: soloTipo(LS1, "A") entrega una lista con Sangre de código 127
# Ej3: soloTipo(LS2, "A") entrega nada (la lista vacía)
def soloTipo(listaS, t):
       assert esLista(listaS) and type(t) == str
       assert t == "A" or t == "B" or t == "AB" or t == "O", \
       "Sólo puedes escoger entre tipos A, B, AB u O de sangre"
       def _soloTipo(listaS, t):
              if listaS == None:
                     return None
              else:
                     # chequear si el atributo 'tipo' de un elemento perteneciente a la lista es igual a t
                     # si la sangre es en efecto tipo *t*, agregar este elemento a una nueva lista
                     # en caso contrario proceder a analizar el siguiente elemento de la lista proveída hasta finalizar la recursión
                     elementS = cabeza(listaS)
                     if elementS.tipo == t:
                            return lista(elementS, _soloTipo(cola(listaS), t))
                     else:
                            return _soloTipo(cola(listaS), t)
       return _soloTipo(listaS, t)
# Test:
assert soloTipo(LS1, "AB") == lista(Sangre(460, 'AB', '-') , lista(Sangre(809, 'AB', '+'), None))
assert soloTipo(LS1, "A") == lista(Sangre(127, 'A', '+'), None)
assert soloTipo(LS2, "A") == None
