import estructura

# --------------------------------------
# definición est. arbol binario

# AB: valor(any) izq(AB) der(AB)
estructura.crear('AB', 'valor izq der')

arbolVacio = None



# --------------------------------------
# ab de ejemplo

raiz = AB(25, 
          AB(16, AB(26, arbolVacio, arbolVacio), 
                 AB(31, AB(40, arbolVacio, arbolVacio), 
                        AB(5, arbolVacio, arbolVacio))),
          AB(9, AB(39, arbolVacio, arbolVacio), 
                arbolVacio))

# --------------------------------------
# esAB: any -> bool
# indica si lo entregado cumple con ser AB
# ej: esAB(raiz) entrega True
def esAB(A):
    
    # el nodo vacío se considera un árbol AB
    if A == arbolVacio:
        return True
    
    # El nodo actual debe ser de tipo AB, y 
    # sus ramas izq y der también deben serlo
    return type(A) == AB and \
           esAB(A.izq) and \
           esAB(A.der)

# Test
assert esAB(raiz)
assert esAB(arbolVacio)
assert not esAB("gatito")

# --------------------------------------
# valores: AB -> int
# cuenta cuantos nodos tiene el arbol
# ej: valores(raiz) entrega 8
def valores(A):
    assert esAB(A)

    # el nodo vacío no tiene elementos
    if A == arbolVacio:
        return 0
    
    # Contamos el actual, y contamos cuantos 
    # valores hay en las ramas izq y der
    return 1 + valores(A.izq) + valores(A.der)

# test
assert valores(raiz) == 8

# --------------------------------------
# altura: AB -> int
# cuenta cual es la profundidad del arbol
# ej: altura(raiz) entrega 4
def altura(A):
    assert esAB(A)
    
    # el nodo vacío no tiene elementos
    if A == arbolVacio:
        return 0
    
    # Contamos el nivel actual y nos quedamos con el sub-árbol de mayor altura
    return 1 + max(altura(A.izq), altura(A.der))

# test
assert altura(raiz) == 4

# --------------------------------------
# hojas: AB -> int
# cuenta cuantos nodos sin ramas hay en el arbol
# ej: hojas(raiz) entrega 4
def hojas(A):
    assert esAB(A)
    
    if A == arbolVacio:
        return 0
    
    if A.izq == arbolVacio and A.der == arbolVacio:
        return 1
    else: 
        return hojas(A.izq) + hojas(A.der)

# Test
assert hojas(raiz) == 4

# --------------------------------------
# buscar: AB any -> bool
# busca si existe el elemento buscado en el arbol
# ej: buscar(raiz, 99) entrega False
def buscar(A,elem):
    assert esAB(A)
    
    # el nodo vacío no tiene valor, por lo que el elemento no existe
    if A == arbolVacio:
        return False
    
    # Si el valor del nodo actual coincide con el buscado, 
    # entonces si está en el árbol
    if A.valor == elem:
        return True
    
    # Si no, entonces buscamos si existe en las ramas izq o der
    return buscar(A.izq, elem) or buscar(A.der,elem)

# test
assert buscar(raiz,31)
assert not buscar(raiz,99)














