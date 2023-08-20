import numpy as np
import matplotlib.pyplot as plt

def xh(t):
    return 1.3*np.exp(-0.2*t) - 1.2*np.exp(-0.3*t)

def vh(t):
    return 0.36*np.exp(-0.3*t) - 0.26*np.exp(-0.2*t)

def A(w):
    F0 = 0.5
    return (2*F0) / np.sqrt(w**2/4 + (w**2 - 0.06)**2)

t = np.arange(0, 40, 0.01)
w = np.arange(0, 5, 0.01)

# Calcular los valores de xh(t) para cada valor de t
x = xh(t)
v = vh(t)
# Calcular los valores de A(w) para cada valor de w
a = A(w)

fig, ax = plt.subplots()

# Graficar la función xh(t) contra el tiempo t
ax.plot(t, x, color="green")

ax.grid(True)

# Agregar etiquetas y título al gráfico
ax.set_xlabel('Tiempo (s)')
ax.set_ylabel('Posición (m)')
ax.set_title('Movimiento armónico amortiguado')

# # Mostrar el gráfico
plt.show()

fig, ax = plt.subplots()

# Graficar la función vh(t) contra el tiempo t
ax.plot(t, v, color="green")

ax.grid(True)

# Agregar etiquetas y título al gráfico
ax.set_xlabel('Tiempo (s)')
ax.set_ylabel('Rapidez (m/s)')
ax.set_title('Rapidez de la partícula en movimiento armónico amortiguado')

# Mostrar el gráfico
plt.show()

fig, ax = plt.subplots()

# Graficar la función A(w) contra la frecuencia angular w
ax.plot(w, a, color="green")

ax.grid(True)

# Agregar etiquetas y título al gráfico
ax.set_xlabel('Frecuencia (rad/s)')
ax.set_ylabel('Amplitud')
ax.set_title('Respuesta en amplitud del sistema')

# Mostrar el gráfico
plt.show()