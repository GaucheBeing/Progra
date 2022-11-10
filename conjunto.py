L1 = ["Alpha", "Beta", "Gamma", "Delta"]
L2 = ['a', "be", 'ce', 'de']

def conjunto(X):
    assert type(X) == list
    frecuencias = {}
    for palabra in X:
        if palabra not in frecuencias:
            frecuencias[palabra] = 1
        else: frecuencias[palabra] = frecuencias[palabra] + 1
    for frec in frecuencias.values():
        if frec > 1:
            return False
        else: return True


def union(X, Y):
    assert type(X) == type(Y) == list
    Z = X + Y
    print(Z)


def grabar(X, S):
    assert type(X) in [list, dict] and type(S) == str
    file = open(S + '.txt', 'w')
    for palabra in X:
        file.write(palabra + '\n')


def leer(S):
    file = open(S + '.txt', 'r')
    for line in file:
        line = line.strip()
        print(line)
    file.close()


def mostrar(X, S):
    Dpalabras = {}
    for palabra in X:
        if palabra not in Dpalabras:
            Dpalabras[palabra] = 1
        else: Dpalabras[palabra] = Dpalabras[palabra] + 1
    X = [str(pal + ': ' + str(frec)) for pal, frec in Dpalabras.items()]
    grabar(X, S)
    leer(S)
