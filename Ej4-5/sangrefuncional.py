import estructura
from lista import *
from absfun import *

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
SS2 = Sangre(308, 'AB', '-')
SS3 = Sangre(124, 'B', '-')

# definicion de listas de sangre de ejemplo
LS1 = lista(S1, lista(S2, lista(S3, lista(S4, lista(S5, \
       lista(S6, lista(S7, lista(S8, lista(S9, lista(S0, listaVacia))))))))))

LS2 = lista(SS1, lista(SS2, lista(SS3, listaVacia)))

# universal: lista(Sangre) -> int
# Función: dada una lista de Sangre, cuente cuanta sangre hay del tipo O con factor RH negativo
# Ej: universal(LS1) y universal(LS2) han de retornar 2 y 0 respectivamente
def universal(LS):
       assert esLista(LS)
       newLS = filtro(lambda x: x.tipo == 'O' and x.rh == '-', LS)
       return largo(newLS)
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
       return filtro(lambda x: x.tipo == t, LS)
# Test:
assert soloTipo(LS1, "AB") == lista(Sangre(460, 'AB', '-') , lista(Sangre(809, 'AB', '+'), None))
assert soloTipo(LS1, "A") == lista(Sangre(127, 'A', '+'), None)
assert soloTipo(LS2, "A") == None

# RHmas: lista(Sangre) -> lista(Sangre)
# Función: dada una lista de sangre, se entrega la lista de todas las sangres volviendolas factor RH +
# Ej1: 
def RHmas(LS):
       assert esLista(LS)
       return mapa(lambda x: Sangre(x.cod, x.tipo, '+'), LS)
# Test:
assert RHmas(LS2) == lista(Sangre(839, 'O', '+'), lista(Sangre(308, 'AB', '+'), \
       lista(Sangre(124, 'B', '+'), listaVacia)))

assert RHmas(LS1) == lista(Sangre(127, 'A', '+'), lista(Sangre(510, 'B', '+'), \
       lista(Sangre(460, 'AB', '+'), lista(Sangre(637, 'B', '+'), \
       lista(Sangre(174, 'B', '+'), lista(Sangre(809, 'AB', '+'), \
       lista(Sangre(331, 'B', '+'), lista(Sangre(803, 'O', '+'), \
       lista(Sangre(648, 'B', '+'), lista(Sangre(207, 'O', '+'), listaVacia))))))))))