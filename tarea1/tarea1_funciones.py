from random import randint

# Entradas-Salida: num num num num -> int
# Funcionalidad: Toma cuatro números, los trata como dos pares ordenados y saca la distancia (truncada) entre estos
# Ejemplo de uso: distancia(10, 0, 0, 10) devuelve 20
def distancia(x1, y1, x2, y2):
    return int(abs(x2-x1)+abs(y2-y1))
# Testing:
assert distancia(10, 0, 0, 10) == 20

# Entradas-Salida; num num num num -> bool
# Funcionalidad: Toma cuatro números, los trata como dos pares ordenados y compara coordenada por coordenada si son iguales
# Ejemplo de uso: encontrado(1, 2, 2, 1) devuelve False, encontrado(1.0, 0, 1, 0) entrega True
def encontrado(x1, y1, x2, y2):
    return (x1,y1) == (x2,y2)
# Testing:
assert encontrado(1.0, 0, 1, 0) == True
assert encontrado(1, 2, 2, 1) == False

# Entradas-Salida: int int -> int | None
# Funcionalidad: Toma dos enteros y entrega otro entero dentro del intervalo generado por los números entregados
# Ejemplo de uso: numeroAleatorio(-50,50) entrega un número dentro del intervalo [-50, 50]
def numeroAleatorio(a,b):
    if a<b:
        return randint(a, b)
    else: print("Ops! para crear un número aleatorio dentro del intervalo deseado este debe existir")

# Entradas-Salida; num num -> bool
# Funcionalidad: Toma dos números y evalua si estos están fuera del intervalo [-50, 50]
# Ejemplo de uso: fueraCuadrado(-49.9, 0) entrega False
def fueraCuadrado(x,y):
    return abs(x) >= 50 or abs(y) >= 50
# Testing:
assert fueraCuadrado(-49.9, 0) == False
