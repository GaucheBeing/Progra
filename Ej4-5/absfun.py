#Modulo absfun, que contiene las funciones de abstracción funcional
from lista import *

# -----------------------------------------------
# filtro: (any->bool) lista(any) -> lista(any)
# entrega una lista con los elementos que pasen un criterio
def filtro(funCriterio, L):
    assert esLista(L)

    if L == listaVacia:
        return listaVacia
    
    actual = cabeza(L)
    if funCriterio(actual):
        return lista(actual, filtro(funCriterio, cola(L)))
    else:
        return filtro(funCriterio, cola(L))


# Test
valores = lista(6, lista(4, lista(8, listaVacia)))
assert filtro(lambda x: x < 5, valores) == lista(4, listaVacia)

valores = lista("a", lista("b", lista("c", lista("d", listaVacia))))
assert filtro(lambda x: x == "b" or x == "d", valores) == lista("b", lista("d", listaVacia))

# -----------------------------------------------
# mapa: (any->any) lista(any) -> lista(any)
# entrega una lista sobre la cual se aplicó una operación
# a sus elementos
def mapa(funOperacion, L):
    assert esLista(L)

    if L == listaVacia:
        return listaVacia
    
    actual = cabeza(L)
    nuevo = funOperacion(actual)
    return lista(nuevo, mapa(funOperacion, cola(L)))


# Test
valores = lista(1, lista(2, lista(3, lista(4, listaVacia)))) 
assert mapa(lambda x: 10*x, valores) == lista(10, lista(20, lista(30, lista(40, listaVacia))))

valores = lista("pedro", lista("juan", lista("diego", listaVacia)))
assert mapa(lambda x: "hola "+x , valores) == lista("hola pedro", lista("hola juan", lista("hola diego", listaVacia)))

# -----------------------------------------------
# reductor: lista(any) (any any -> any) any -> any
# opera todos los elementos de la lista entre si, reduciéndolo
# a un solo valor
def reductor(funOperacion, L, init):
    assert esLista(L)

    if L == listaVacia:
        return init
    
    actual = cabeza(L)
    nuevoInit = funOperacion(init, actual)
    return reductor(funOperacion, cola(L), nuevoInit)


# Test
valores = lista(1, lista(2, lista(3, lista(4, listaVacia))))
assert reductor(lambda x, y: x + y, valores, 0) == 10

valores = lista("pedro", lista("juan", lista("diego", listaVacia))) 
assert reductor(lambda x, y: x + " " + y, valores, "") == " pedro juan diego"

