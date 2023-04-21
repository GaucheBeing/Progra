import matplotlib.pyplot as plt       
import numpy as np

####### Parte a #######

# Función auxiliar para crear la matríz de pesos asociado a cada capa
def get_weights(di,dj):
    W = np.random.uniform(size=(di,dj), low=-1, high=1)
    return W

# Función auxiliar para crear los vectores de sesgos asociados a cada capa
def get_biases(di):
    b = np.random.uniform(size=di, low=-1, high=1)
    return b

# Función auxiliar para crear una lista con el par de matríz - sesgo asociado a cada capa
def get_phi(d):
    # Lista vacía para agregar los pares
    phi = []
    # Iteramos por la dimensión de cada una de las capas y generamos las matríces de peso y vectores sesgo para luego añadirlas en orden a phi hasta llegar a la dimensión del vector final
    for i in range(len(d)):
        if i+1 == len(d):
            break
        else: 
            W = get_weights(d[i+1],d[i])
            b = get_biases(d[i+1])
            phi.append([W, b])
    return phi

# Por familiaridad trabajamos el arreglo como una lista del vanilla Python para chequear si las componentes del vector dado son positivas o no, en caso de no serlo asignarlo como 0
def sigma_1(vec):
    if type(vec) == np.ndarray:
        vec = np.ndarray.tolist(vec)
    for i in range(len(vec)):
        if vec[i] < 0:
            vec[i] = 0
    return np.array(vec)

def sigma_2(vec):
    if type(vec) != np.ndarray:
        vec = np.array(vec)
    return (1+np.exp(vec))**(-1)

def R(x, d, Phi=None, sigma=sigma_1):
    if type(x) != np.ndarray:
        x = np.array(x)
    if Phi == None:
        Phi = get_phi(d)
    nodos = [x]
    for i in range(len(Phi)):
        x = sigma(Phi[i][0].dot(x) + Phi[i][1])
        nodos.append(x)
    return nodos[-1]

####### Parte b ####### 

# fijamos las dimensiones de cada capa, entrada y salida
# también usamos un phi aleatorio para que haga sentido calcular las imagenes de R(Phi)(x,y) y graficar
d = [2, 2, 1]
Phi_fijo = get_phi(d)

x = np.linspace(-1, 1, 101)
y = np.linspace(-1, 1, 101)
XX, YY = np.meshgrid(x,y)

def u(XX, YY, d, Phi=None, sigma=sigma_1):
    ZZ = np.zeros([len(XX), len(YY)])
    for i in range(len(XX)):
        for j in range(len(YY)):
            vec_ij = [XX[i][j], YY[i][j]]
            ZZ[i][j] = R(vec_ij, d, Phi, sigma)
    return ZZ

ZZ_1 = u(XX, YY, [2,2,1], Phi_fijo, sigma_1)
ZZ_2 = u(XX, YY, [2,2,1], Phi_fijo, sigma_2)

# graficar la función con sigma_1 (ReLu)
fig = plt.figure(figsize=(10,6))
ax = plt.axes(projection='3d')
ax.plot_surface(XX, YY, ZZ_1, cmap='coolwarm')
ax.set_title('Red neuronal R(Φ) con σ1')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()

# graficar la función con sigma_2 (Sigmoid) 
fig = plt.figure(figsize=(10,6))
ax = plt.axes(projection='3d')
ax.plot_surface(XX, YY, ZZ_2, cmap='coolwarm')
ax.set_title('Red neuronal R(Φ) con σ2')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()

####### Parte c ####### 

Phi_10 = [
    [np.array([[ 0.74448778, -0.35930282],
         [-0.56573241, -0.16938503],
         [ 0.72973341,  0.86772683],
         [ 0.51909915, -0.07904414],
         [-0.27377547, -0.04471656],
         [-0.46506753,  0.23847687],
         [ 0.66936176,  0.68990471],
         [-0.9138747 ,  0.55266934],
         [-0.06174716, -0.18054646],
         [ 0.99803183, -0.53426474]]),
  np.array([ 0.18864999, -0.96447815,  0.52955462,  0.47439194,  0.80843097,
          0.52987577,  0.91287043, -0.49067048,  0.78820278, -0.2028479 ])],

 [np.array([[ 0.18809518, -0.33971196,  0.49123748,  0.46640211,  0.38503698,
          -0.34018576,  0.63942813, -0.23665588,  0.18550646,  0.1300057 ]]),
  np.array([-0.81811501])]
  ]

Phi_5 = [
[np.array([[ 0.74448778, -0.35930282],
         [-0.56573241, -0.16938503],
         [ 0.72973341,  0.86772683],
         [ 0.51909915, -0.07904414],
         [-0.27377547, -0.04471656]]),
  np.array([ 0.18864999, -0.96447815,  0.52955462,  0.47439194,  0.80843097])],

 [np.array([[ 0.18809518, -0.33971196,  0.49123748,  0.46640211,  0.38503698]]),
  np.array([-0.81811501])]
  ]

Phi_3 = [
[np.array([[ 0.74448778, -0.35930282],
         [-0.56573241, -0.16938503],
         [ 0.72973341,  0.86772683]]),
  np.array([ 0.18864999, -0.96447815,  0.52955462])],

 [np.array([[ 0.18809518, -0.33971196,  0.49123748]]),
  np.array([-0.81811501])]
  ]

#### Realización con Phi_10

d = [2, 10, 1]
ZZ_Phi10 = u(XX, YY, d, Phi_10, sigma_2)

fig = plt.figure(figsize=(10,6))
ax = plt.axes(projection='3d')
ax.plot_surface(XX, YY, ZZ_Phi10, cmap='coolwarm')
ax.set_title('Red neuronal R(Φ_10) con σ2')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()

#### Realización con Phi_5

d = [2, 5, 1]
ZZ_Phi5 = u(XX, YY, d, Phi_5, sigma_2)

fig = plt.figure(figsize=(10,6))
ax = plt.axes(projection='3d')
ax.plot_surface(XX, YY, ZZ_Phi5, cmap='coolwarm')
ax.set_title('Red neuronal R(Φ_5) con σ2')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()

#### Realización con Phi_3

d = [2, 3, 1]
ZZ_Phi3 = u(XX, YY, d, Phi_3, sigma_2)

fig = plt.figure(figsize=(10,6))
ax = plt.axes(projection='3d')
ax.plot_surface(XX, YY, ZZ_Phi3, cmap='coolwarm')
ax.set_title('Red neuronal R(Φ_3) con σ2')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()