import estructura
from lista import *
<<<<<<< HEAD:Ej4-5/sangrefuncional.py
=======
from absfun import *

>>>>>>> 7ee5b552af86cbf5bcb2a6a996d14819913b94a3:Ej4/sangrefuncional.py

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
<<<<<<< HEAD:Ej4-5/sangrefuncional.py
SS2 = Sangre(308, 'AB', '+')
SS3 = Sangre(124, 'B', '+')
=======
SS2 = Sangre(308, 'AB', '-')
SS3 = Sangre(124, 'B', '-')
>>>>>>> 7ee5b552af86cbf5bcb2a6a996d14819913b94a3:Ej4/sangrefuncional.py

# definicion de listas de sangre de ejemplo
LS1 = lista(S1, lista(S2, lista(S3, lista(S4, lista(S5, \
       lista(S6, lista(S7, lista(S8, lista(S9, lista(S0, listaVacia))))))))))

LS2 = lista(SS1, lista(SS2, lista(SS3, listaVacia)))

<<<<<<< HEAD:Ej4-5/sangrefuncional.py
def reductor(fun, L):
       assert esLista(L)

def filtro(fun, L):
       assert esLista(L)

def mapa(fun, L):
       assert esLista(L)
# mapa: (any->any) lista(any) -> lista(any)
# entrega una lista sobre la cual se aplicó una operación
# a sus elementos
def mapa(fun, L):
       assert esLista(L)
       if L == listaVacia:
              return listaVacia
       actual = cabeza(L)
       # La función de operación, determina que operación hay que aplicar al elemento en la lista
       nuevo = fun(actual)
       return lista(nuevo, mapa(fun, cola(L)))






# universal: lista(Sangre) -> int
# Función: dada una lista de Sangre, cuente cuanta sangre hay del tipo O con factor RH negativo
# Ej: universal(LS1) y universal(LS2) han de retornar 2 y 0 respectivamente
def universal(LS):
       assert esLista(listaS)
       contador = lambda 
       return reductor(contador, LS, 0)
# Test:
assert universal(LS1) == 2
assert universal(LS2) == 0

# soloTipo: lista(Sangre) str -> lista(Sangre) 
# Función: dada una lista de Sangre y un tipo, entregar una lista que solo contenga Sangre del tipo indicado
# Ej1: soloTipo(LS1, "AB") debería entregar una lista con Sangre de códigos 460 y 809
# Ej2: soloTipo(LS1, "A") entrega una lista con Sangre de código 127
# Ej3: soloTipo(LS2, "A") entrega nada (la lista vacía)
def soloTipo(LS, t):
       assert esLista(LS) and type(t) == str
       assert t in ['A','B','AB', 'O'],          "Sólo puedes escoger entre tipos A, B, AB u O de sangre"
       return 
# Test:
assert soloTipo(LS1, "AB") == lista(Sangre(460, 'AB', '-') , lista(Sangre(809, 'AB', '+'), None))
assert soloTipo(LS1, "A") == lista(Sangre(127, 'A', '+'), None)
assert soloTipo(LS2, "A") == None
=======
def
>>>>>>> 7ee5b552af86cbf5bcb2a6a996d14819913b94a3:Ej4/sangrefuncional.py
