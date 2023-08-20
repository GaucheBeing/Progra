"""
Original file is located at
    https://colab.research.google.com/drive/1SXfgTT2KLa4_T9tL8wCvzGu9pIeYMiuy
"""

import random
import matplotlib.pyplot as plt

# - - - - - - - - - - Sistema original - - - - - - - - - - #

def simulador_sistema_original(p, q):
    # Asignar con valores de verdad el caso en que cada jugar anote el penal
    equipo1 = random.random() < p
    equipo2 = random.random() < q
    # Chequear si no hay empate, o sea, que ocurran ambos eventos o ninguno a la vez
    if equipo1 != equipo2:
        return 1 if equipo1 else 0
    else:
        return simulador_sistema_original(p, q)

# - - - - - - - - - Sistema alternativo I - - - - - - - - - #

def simulador_sistema_alternativo_I(p, q):
    equipo1 = random.random() < p
    equipo2 = random.random() < q

    if equipo1 != equipo2:
        return 1 if equipo1 else 0
    # Análogo a alternar jugadores cambiamos las probabilidades de suceso por ronda
    else:
        return simulador_sistema_alternativo_I(q, p)

# - - - - - - - - - Sistema alternativo II - - - - - - - - - #

def simulador_sistema_alternativo_II(p, q):
    # Caso: primera ronda
    equipo1 = random.random() < p
    equipo2 = random.random() < q

    if equipo1 != equipo2:
        return 1 if equipo1 else 0

    # Caso: rondas posteriores
    # Definimos una subfunción que alterne cada 2 rondas de manera recursiva hasta que alguno de los equipos gane
    def _alternativo_II(p, q):
        for i in range(2):
            equipo1 = random.random() < p
            equipo2 = random.random() < q
            if equipo1 != equipo2:
                return 1 if equipo1 else 0
            else:
                return _alternativo_II(q, p)
    # Como estamos en ronda 2, el equipo que parte es el segundo, con lo que cambiamos las probabilidades
    return _alternativo_II(q, p)

# - - - - - - - - - Simulador de partidos - - - - - - - - - #

def simulador_de_partidos(n, sistema, p, q):
    equipo1 = 0
    for i in range(n):
        if sistema == "original":
            equipo1 += simulador_sistema_original(p, q)
        elif sistema == "alternativoI":
            equipo1 += simulador_sistema_alternativo_I(p, q)
        elif sistema == "alternativoII":
            equipo1 += simulador_sistema_alternativo_II(p, q)
    return equipo1/n

# Asignación de valores para las probabilidades y cantidad de partidos
p = 0.5
q = 0.3
n = 1000

# Generación de ejes
numPartidos = list(range(1, n+1))
Probabilidades_equipo1_sistemaOriginal = []
Probabilidades_equipo1_sistemaAlternativoI = []
Probabilidades_equipo1_sistemaAlternativoII = []

for partidos in numPartidos:
    Probabilidades_equipo1_sistemaOriginal.append(simulador_de_partidos(partidos, "original", p, q))
    Probabilidades_equipo1_sistemaAlternativoI.append(simulador_de_partidos(partidos, "alternativoI", p, q))
    Probabilidades_equipo1_sistemaAlternativoII.append(simulador_de_partidos(partidos, "alternativoII", p, q))

# Generación de gráficos
plt.title("Superposición de probabilidades según sistema de juego")
plt.plot(numPartidos, Probabilidades_equipo1_sistemaOriginal, label="Probabilidades según el sistema tradicional")
plt.plot(numPartidos, Probabilidades_equipo1_sistemaAlternativoI, label="Probabilidades según el sistema alternado por ronda")
plt.plot(numPartidos, Probabilidades_equipo1_sistemaAlternativoII, label="Probabilidades según el sistema alternado por cada dos rondas")
plt.grid(True)
plt.legend()
plt.xlabel('Número de partidos jugados')
plt.ylabel('Probabilidad de que el primer equipo gane')
plt.show()