# -*- coding: utf-8 -*-
"""
Original file is located at
    https://colab.research.google.com/drive/1qmAqG6SlwJymOivhP8H9NclJoRXt1pG3
"""

import numpy as np
import matplotlib.pyplot as plt

# ----------------------------------------------------------- #
# - - - - - - - - - - - - - Parte 1 - - - - - - - - - - - - - #
# ----------------------------------------------------------- #

def B(x):
    return np.cos(np.pi/2 * x)

val_x = np.linspace(-1, 1, 100)
val_y = B(val_x)

fig, ax = plt.subplots()
ax.plot(val_x, val_y, color="green")
ax.grid(True)
ax.set_title('Gráfico B(x)')
ax.set_xlabel('Eje x')
ax.set_ylabel('Eje y')
plt.show()

# ----------------------------------------------------------- #
# - - - - - - - - - - - - - Parte 2 - - - - - - - - - - - - - #
# ----------------------------------------------------------- #

# - - - - - - - - - - Sección 1 - - - - - - - - - - #

D = np.random.uniform(-1, 1, 100)
# D = np.array([
# -0.92075802, -0.90460685, -0.80837862, -0.80385251, -0.79584054, -0.76973524, -0.75730413, 
# -0.72224559, -0.71336764, -0.71280782, -0.67044931, -0.66970782, -0.65154524, -0.64365218, 
# -0.60583625, -0.58835131, -0.53869231, -0.52749781, -0.50755884, -0.49340023, -0.41799446, 
# -0.39700323, -0.3732882 , -0.35467585, -0.34160003, -0.30811194, -0.28018213, -0.27776987, 
# -0.25766811, -0.23012599, -0.21797488, -0.18768971, -0.17690727, -0.09493208, -0.08580037, 
# -0.08470427, -0.0731018 , -0.05785285, -0.05639786, -0.04371286, -0.04314696, -0.01492119, 
# -0.00941034,  0.02267355,  0.02455109,  0.03064105,  0.03421928,  0.03586817,  0.04310657,  
#  0.06599364,  0.07120264,  0.097664  ,  0.11428252,  0.13539854,  0.18744502,  0.20046222,  
#  0.25281776,  0.256866  ,  0.3098043 ,  0.31628216,  0.31689808,  0.31867114,  0.32184614, 
#  0.33310731,  0.33426332,  0.36429202,  0.36842066,  0.37920723,  0.40121683,  0.45102364, 
#  0.45571234,  0.46153068,  0.47296723,  0.49548794,  0.52734099,  0.55296066,  0.57470988,  
#  0.57905664,  0.58221249,  0.60883142,  0.64303052,  0.65537999,  0.67012381,  0.68969268,  
#  0.75801785,  0.76282817,  0.79223887,  0.82070695,  0.82923925,  0.83052789,  0.83539136,  
#  0.8451296 ,  0.85868994,  0.86655049,  0.89373667,  0.89424039,  0.89424355,  0.9304471 ,  
#  0.94428847,  0.99862616]) 

fig, ax = plt.subplots()
ax.set_ylim(0, 0.1)
for dato in D:
    ax.plot([dato, dato], [0, 0.1], color='green', linewidth=1)
ax.yaxis.set_ticks([])
fig.set_size_inches(7, 0.4)
ax.set_title('Representación gráfica de set de datos D')
ax.set_xlabel('Elementos del conjunto D')
plt.show()

# - - - - - - - - - - Sección 2 - - - - - - - - - - #

def sigma(s):
    return np.sin(s)

def R(x, Phi, sigma=sigma):
    w1, w2, b1, b2 = Phi
    return w2*sigma(w1*x + b1) + b2

def d2R(x, Phi, sigma=sigma):
    w1, w2, b1, b2 = Phi
    return -w2*sigma(w1*x + b1)*w1**2

def grad_R(x, Phi):
    w1, w2, b1, b2 = Phi
    s = w1*x + b1
    dR_db1 = w2*np.cos(s)
    dR_db2 = np.ones_like(x)
    dR_dw2 = np.sin(s)
    dR_dw1 = dR_db1*x
    return np.array([dR_dw1, dR_dw2, dR_db1, dR_db2])

def grad_d2R(x, Phi):
    w1, w2, b1, b2 = Phi
    s = w1*x + b1
    d2R_db1 = -w1**2*w2*np.cos(s)
    d2R_db2 = np.zeros_like(x)
    d2R_dw2 = -w1**2*np.sin(s)
    d2R_dw1 = -2*w1*w2*np.sin(s) + d2R_db1*x
    return np.array([d2R_dw1, d2R_dw2, d2R_db1, d2R_db2])

def C(Phi, D=D):
    p = np.pi**2/4
    # Usando listas
    # C1 = 0
    # for j in range(len(D)):
    #     x = D[j]
    #     C1 += (d2R(x, Phi) +  p*R(x, Phi))**2
    # C1 = C1/len(D)
    C1 = np.mean( (d2R(D, Phi) + p*R(D, Phi))**2 )
    C2 = (R(-1,Phi)**2 + R(1,Phi)**2 + (R(0,Phi)-1)**2)/3
    return (C1+C2)/2

def grad_C(Phi, D=D):
    p = np.pi**2/4
    # Usando listas
    # grad_C1 = np.zeros(4)
    # for j in range(len(D)):
    #     x = D[j]
    #     grad_C1 += (d2R(x, Phi) + p*R(x, Phi)) * (grad_d2R(x, Phi) + p*grad_R(x, Phi))
    # grad_C1 = grad_C1/len(D)
    grad_C1 = np.mean( (d2R(D, Phi) + p*R(D, Phi)) * (grad_d2R(D, Phi) + p*grad_R(D, Phi)), axis=1)
    grad_C2 = (R(-1, Phi)*grad_R(-1, Phi) + R(1, Phi)*grad_R(1, Phi) + (R(0, Phi)-1)*grad_R(0, Phi))/3
    return (grad_C1+grad_C2)

# - - - - - - - - - - Sección 3-4 - - - - - - - - - - #

Phi0 = [0.5, 1.1, 1.3, 0]

def gradiente_conjugado(M, l=0.01, Phi=Phi0, D=D):
    for reps in range(M):
        Phi -= l*grad_C(Phi, D)
    return Phi

Phi100 = gradiente_conjugado(100)
Phi500 = gradiente_conjugado(500)
Phi1000 = gradiente_conjugado(1000)

print(f"\nPhi entrenado con 100 iteraciones {Phi100}\nPhi entrenado con 500 iteraciones {Phi500}\nPhi entrenado con 1000 iteraciones {Phi1000}\n")

x = np.linspace(-1, 1, 500)
y = np.cos(np.pi/2 * x)
y100 = R(x, Phi100)
y500 = R(x, Phi500)
y1000 = R(x, Phi1000)

plt.title('Superposición de las funciones R(Φ) entrenadas y B(x)')
plt.plot(x, y, label="B(x) original")
plt.plot(x, y100, label="Aproximación con M=100")
plt.plot(x, y500, label="Aproximación con M=500")
plt.plot(x, y1000, label="Aproximación con M=1000")
plt.grid(True)
plt.legend()
plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.show()

# - - - - - - - - - - Sección 5 - - - - - - - - - - #

M_grid = np.linspace(100, 1000, 10)
C_vals = [C(gradiente_conjugado(int(M))) for M in M_grid]

plt.plot(M_grid, C_vals, marker='o', color="green")
plt.title('Costo C(Φᴹ) según número de iteraciones de entrenamiento')
plt.xlabel('M')
plt.ylabel('C(Φᴹ)')
plt.grid(True)
plt.show()