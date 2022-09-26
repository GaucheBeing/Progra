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


# universal: lista -> int
# Función: dada una lista de Sangre, cuente cuanta sangre hay del tipo O con factor RH negativo
# Ej: 
def universal(listaS):
       assert esLista(listaS)
       def _universal(listaS):
              if listaS == None:
                     return 0
              else:   
                     if cabeza(listaS) == "O" and cabeza(listaS) == "-":
                            1
                            return _universal(cola(listaS))
                     else:
                            0
                            return _universal(cola(listaS))
       return _universal(listaS)
# Test:
assert universal(LS1) == 2
assert universal(LS2) == 0

# soloTipo: lista str -> lista 
# Función: dada una lista de Sangre y un tipo, entregar una lista que solo contenga Sangre del tipo indicado
# Ej:
# def soloTipo(listaS, t):
#        assert esLista(listaS) and type(t) == str
#        assert t == "A" or t == "B" or t == "AB" or t == "O", \
#        "Sólo puedes escoger entre tipos A, B, AB u O de sangre"
#        def _soloTipo(listaS, t)       
#               if cabeza(listaS)

#               return None
#        return _soloTipo(listaS, t)
