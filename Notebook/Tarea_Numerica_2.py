import numpy as np

def get_weights(di,dj):
    return np.random.uniform(size=(dj,di), low=-1, high=1)

def get_biases(dj):
    return np.random.uniform(size=dj, low=-1, high=1)

def get_phi(d):
    L = len(d) - 2
    Phi = []
    for l in range(L+1):
        Wl = get_weights(d[l],d[l+1])
        bl = get_biases(d[l+1])
        Phi.append([Wl,bl])
    return Phi

def sigmoide(vec):
    return (1+np.exp(-vec))**(-1)

def R(x0, d, Phi, sigma=sigmoide):
    # Para el caso de d = 2 la iteración y definiciones pueden ser comentadas sin afectar el resultado
    L = len(d) - 2
    xl = x0
    for l in range(L):
        Wl, bl = Phi[l]
        xl = sigma(np.matmul(Wl,xl) + bl)
    Wf, bf = Phi[-1]
    Output = np.matmul(Wf,xl) + bf
    return sigma(Output)

####### Parte a ####### 

def grad_conjugado(Phi, D, l=0.01, M=1000):
    w1 = Phi[0][0][0][0]
    w2 = Phi[0][0][0][1]
    b = Phi[0][1][0]
    for reps in range(M):
        dw1 = 0
        dw2 = 0
        db = 0
        for i in range(len(D)):
            s = w1*D[i][0]+w2*D[i][1]+b
            commonFact = (np.exp(s)*( np.exp(s)*(1-D[i][2])-D[i][2] )) / (1+np.exp(s))**3
            dw1 += D[i][0]*commonFact
            dw2 += D[i][1]*commonFact
            db += commonFact
        w1 = w1 - l*dw1
        w2 = w2 - l*dw2
        b = b - l*db
    return [[np.array([[w1, w2]]), np.array([b])]]

####### Parte b ####### 

D = [
    [9.0, 7.00, 0], [2.0, 5.00, 1], 
    [3.2, 4.94, 1], [9.1, 7.46, 0], 
    [1.6, 4.83, 1], [8.4, 7.46, 0], 
    [8.0, 7.28, 0], [3.1, 4.58, 1], 
    [6.3, 9.14, 0], [3.4, 5.36, 1]
    ]

Phi = grad_conjugado(get_phi([2,1]), D)
R([8,7], [2,1], Phi)

####### Contador de tendencia ####### 

sup = 0
sub = 0
for i in range(0, 100):
    Phi = grad_conjugado(get_phi([2,1]), D)
    realizacion = R([8,7], [2,1], Phi)
    if realizacion>=0.5:
        sup += 1
    else: sub += 1

# sup / sub