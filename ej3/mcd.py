# mdc: int int -> int
# Función: calcular mediante recursion el máximo común divisor entre dos enteros positivos 
# Ej1: evaluar mcd() con 4 y 2 debería retornar 2
# Ej2: mcd(0, 7) devuelve 7
# Ej3: mcd(100, 10) devuelve 10
def mcd(x, y):
    # chequear precondiciones 1 vez por ejecución
    assert type(x) == type(y) == int,   "los parámetros no son enteros"
    assert x >= 0 and y >= 0,           "los parámetros no son positivos"
    # definir sub-función tal que si las precondiciones son satisfechas se ejecuta el algorítmo recursivo de Euclides
    def _mcd(x, y):
        # caso base
        if x == y or x == 0 or y == 0:
            return max(x, y)
        # caso recursivo (1)
        elif x < y:
            return _mcd(x, abs(x-y))
        # caso recursivo (2)
        elif x > y:
            return _mcd(abs(x-y), y)
    # invocar _mcd() hasta llegar al caso base, luego retornar el máximo común divisor de los parámetros entregados
    return _mcd(x, y)

# Testing:
assert mcd(0, 100) == 100               #caso base con parámetro 0
assert mcd(13, 14) == 1                 #caso de coprimos (primo-compuesto)
assert mcd(64, 8) == 8                  #caso de múltiplos

""" Alternativa...
def mcd(x, y):
    assert type(x) == type(y) == int,   "los parámetros no son enteros"
    assert x >= 0 and y >= 0,           "los parámetros no son positivos"
    if x == y or x == 0 or y == 0:
        return max(x, y)
    elif x < y: return mcd(x, abs(x-y))
    else: return mcd(abs(x-y), y)
"""