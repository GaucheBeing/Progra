from arbol import *


# ---------------------------------
# AB's temperamentales de ejemplo

ABT1 = AB(50, 
          AB(16, AB(15, arbolVacio, arbolVacio), 
                 AB(5,  arbolVacio, arbolVacio)),
          AB(40, AB(20, arbolVacio, arbolVacio), 
                 AB(39, arbolVacio, arbolVacio)))

ABT2 = AB(88, 
          AB(50, AB(45, arbolVacio, arbolVacio), 
                 arbolVacio),
          AB(44, AB(33, arbolVacio, arbolVacio), 
                 arbolVacio))

# ---------------------------------
# AB no temperamental de ejemplo

AB3 = AB(50, 
          AB(5, AB(15, arbolVacio, arbolVacio), 
                 AB(4,  arbolVacio, arbolVacio)),
          AB(40, AB(20, arbolVacio, arbolVacio), 
                 AB(88, arbolVacio, arbolVacio)))

# validarTemperamento: AB -> bool
# Función: dado un árbol (binario) validar si este es temperamental o no
# Ej: validarTemperamento(ABT1) => True y para ABT2 también excepto para AB3  
def validarTemperamento(A):
    assert esAB(A)
    # caso base de las bases árbol vacío
    if A == None:
        return True
    # caso base hoja
    elif A.izq == None == A.der:
        return True
    # caso 1 rama izq
    elif A.izq.valor < A.valor and A.der == None:
        return validarTemperamento(A.izq)
    # caso 1 rama der
    elif A.izq == None and A.der.valor < A.valor:
        return validarTemperamento(A.der)
    # caso nodo ambas ramas
    elif A.izq.valor < A.valor and A.der.valor < A.valor:
        return validarTemperamento(A.izq) and validarTemperamento(A.der)
    # ninguno de los casos previos, A no es temperamental
    else: return False
# Testing
assert validarTemperamento(ABT1)
assert validarTemperamento(ABT2)
assert not validarTemperamento(AB3)

# Cuerpo de función equivalente pero más desordenado

#   if A == None
#       return True
#   elif A.izq == None:
#       if A.der == None:
#           return True
#       else:
#           if A.der.valor < A.valor:
#               return validarTemperamento(A.der)
#           else: return False
#   elif A.der == None:
#       if A.izq.valor < A.valor:
#           return validarTemperamento(A.izq)
#       else: return False
#   elif A.izq.valor < A.valor and A.der.valor < A.valor:
#       return validarTemperamento(A.izq) and validarTemperamento(A.der)
#   else: return False