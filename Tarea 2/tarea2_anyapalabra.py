from lista import *
from palabras import crearPalabra, PalabraRosco, crearRosco, mostrarRosco, esPalabraRosco

# definicion strings con todas las letras, para usar en la función iniciar
Lletras = "ABCDEFGHIJLMNOPQRSTUVXYZ"
Lchica = "AEIOU"

# PalabrasRosco de ejemplo
PRa = PalabraRosco('A', 'aceptable', 'Que se puede aceptar',\
                   'pendiente')
PRb = PalabraRosco('B', 'beso','Accion y efecto de besar',\
                   'correcta')
PRc = PalabraRosco('C', 'clave', 'Instrumento musical de percusion',\
                   'incorrecta')
PRs = PalabraRosco('S', 'sol', 'Estrella con luz propia alrededor de la cual gira la Tierra',\
                   'pendiente')
PRt = PalabraRosco('T', 'telefono', 'Sistema de comunicacion que transmite la voz y el sonido a larga distancia por medios electricos o electromagneticos',\
                   'correcta')
PRp = PalabraRosco('P', 'payaso', 'Dicho de una persona: Que hace reir con sus dichos o gestos',\
                   'pendiente')
PRq = PalabraRosco('Q', 'quejar', 'Expresar con la voz el dolor o pena que se siente', \
                   'correcta')
PRr = PalabraRosco('R', 'rey', 'Monarca soberano de un reino', \
                   'incorrecta')
PRe = PalabraRosco('E', 'explicar', 'Declarar, manifestar, dar a conocer lo que alguien piensa', \
                   'correcta')
PRi = PalabraRosco('I', 'iglesia', 'Templo cristiano', \
                   'pendiente')
PRo = PalabraRosco('O', 'ojo', 'organo de la vista en el ser humano y en los animales', \
                   'incorrecta')
PRu = PalabraRosco('U', 'uniforme', 'Que tiene o presenta la misma forma', \
                   'pendiente')
# Roscos de ejemplo:

# Rosco A -> B -> C
Roscoej1 = lista(PRa, lista(PRb, lista(PRc, listaVacia)))

# Rosco S -> T -> P -> Q -> R
Roscoej2 = lista(PRs, lista(PRt, lista(PRp, lista(PRq, lista(PRr, listaVacia)))))

# Rosco A -> E -> I -> O -> U
Roscoej3 = lista(PRa, lista(PRe, lista(PRi, lista(PRo, lista(PRu, listaVacia)))))


# --------------------------------
# Funciones que operan con listas 

# agregarAlPrincipio: lista(any) any -> lista(any)
# Función: dada una lista, agrega un elemento dado al principio de ella
# Ej: agregarAlPrincipio(lista(1, None), 0) entrega lista(0, lista(1, None))
def agregarAlPrincipio(L, e):
    assert esLista(L)
    return lista(e, L)
# Test:
assert agregarAlPrincipio(lista(1, None), 0) == lista(0, lista(1, None))
assert agregarAlPrincipio(lista('b', None), 'a') == lista('a', lista('b', None))


# agregarAlFinal: lista(any) any -> lista(any)
# Función: dada una lista, agrega un elemento dado al final de ella
# Ej: agregarAlFinal(lista(0, None), 1) retorna lista(0, lista(1, None))
def agregarAlFinal(L,e):
    assert esLista(L)
    if L == None:
        return agregarAlPrincipio(L, e)
    else:
        return lista(cabeza(L), agregarAlFinal(cola(L), e))        
# Test:
assert agregarAlFinal(lista(0, None), 1) == lista(0, lista(1, None))
assert agregarAlFinal(lista('a', None), 'b') == lista('a', lista('b', None))

# --------------------------------


# --------------------------------
# Funciones que operan con Rosco(lista de PalabraRosco)

# contarStatus: lista(PalabraRosco) str -> int
# Función: dado un rosco y estado, contar cuantas PalabraRosco poseen su atributo status el estado S
# Ej: contarStatus(Roscoej1, "pendiente") debería contar 1
def contarStatus(Lrosco, S):
    assert esLista(Lrosco)
    assert type(S) == str
    def _contarStatus(LR, S):
        # guardar 1er elemento del rosco y chequear si es de tipo PalabraRosco o es la listaVacia
        PR = cabeza(LR)
        assert esPalabraRosco(PR) or PR == None
        # sumar el neutro si el elemento en revisión corresponde a la listaVacia 
        if LR == None:
            return 0
        # chequear si el atributo *status* del elemento en revisión es S, si lo es, suma 1 y pasa al siguiente, si no, pasa al siguiente
        else:
            if PR.status == S:
                return 1 + _contarStatus(cola(LR), S)
            else: 
                return _contarStatus(cola(LR), S)
    return _contarStatus(Lrosco, S)
# Test:
assert contarStatus(Roscoej1, "pendiente") == 1
assert contarStatus(Roscoej2, "pendiente") == 2
assert contarStatus(Roscoej3, "pendiente") == 3


# cambiarStatus: lista(PalabraRosco) str -> lista(PalabraRosco)
# Función: dado un rosco y un estado, entrega un rosco tal que el status del primer elemento ha cambiado al estado S entregado
# Ej: cambiarStatus(Roscoej1, 'mitochondria is...') entrega lista(PalabraRosco('A', 'aceptable', 'Que se puede aceptar', \
#                                                                              'mitochondria is...'), cola(Roscoej1))
def cambiarStatus(Lrosco, S):
    assert esLista(Lrosco)
    assert type(S) == str
    def _cambiarStatus(LR, S):
        if LR == None:
            return None
        else:
            PR = cabeza(LR)
            if PR.status == S:
                return LR
            else:
                newPR = PalabraRosco(PR.letra, PR.palabra, PR.definicion, S)
                return agregarAlPrincipio(cola(LR), newPR)
    return _cambiarStatus(Lrosco, S)
# Test:
assert cambiarStatus(Roscoej1, 'mitochondria is...') == \
        lista(PalabraRosco('A', 'aceptable', 'Que se puede aceptar', 'mitochondria is...'), lista(PRb, lista(PRc, None)))
assert cambiarStatus(Roscoej2, 'the powerhouse of the cell!') == \
        lista(PalabraRosco('S', 'sol', 'Estrella con luz propia alrededor de la cual gira la Tierra', 'the powerhouse of the cell!'), \
        lista(PRt, lista(PRp, lista(PRq, lista(PRr, None)))))


# avanzar: lista(PalabraRosco) -> lista(PalabraRosco)
# Función: dado un rosco, entrega el rosco avanzado a la siguiente PalabraRosco en la lista
# Ej:
def avanzar(Lrosco):
    return agregarAlFinal(cola(Lrosco), cabeza(Lrosco))
# Test:
assert avanzar(Roscoej1) == lista(PRb, lista(PRc, lista(PRa, listaVacia)))
assert avanzar(Roscoej2) == lista(PRt, lista(PRp, lista(PRq, lista(PRr, lista(PRs, listaVacia)))))

# siguientePendiente: lista(PalabraRosco) -> lista(PalabraRosco) | bool
# Función: dado un rosco, entrega el rosco avanzado hasta llegar a la siguiente palabra pendiente
# Ej:
def siguientePendiente(Lrosco):
    def siguienteStatus(LR, S):
        # chequear la existencia de al menos 1 elemento del rosco tal que tenga estado S
        # en tal caso por recursión llegar hasta ese elemento y hacer un rosco con este en cabeza
        # caso contrario retornar falso
        if contarStatus(LR, S) != 0:
            if LR == None:
                return None
            else:
                PR = cabeza(LR)
                if PR.status == S:
                    return agregarAlPrincipio(cola(LR), PR)
                else:
                    return siguienteStatus(avanzar(LR), S)
        else:
            return False
    return siguienteStatus(Lrosco, 'pendiente')
# Test:
assert siguientePendiente(Roscoej1) == Roscoej1
assert siguientePendiente(lista(PRc, lista(PRa, lista(PRb, None)))) == lista(PRa, lista(PRb, lista(PRc, None)))
assert siguientePendiente(lista(PRb, lista(PRc, None))) == False


# mostrarDefinicion: lista(PalabraRosco) -> None
# Función: dado un rosco, mostrar el mensaje “Comienza con ”, junto a la letra y definición correspondiente a la primera PalabraRosco del rosco
# Ej: mostrarDefinicion(Roscoej1) imprime "Comienza con ' A ': Que se puede aceptar"
def mostrarDefinicion(Lrosco):
    assert esLista(Lrosco)
    PR = cabeza(Lrosco)
    print(f"Comienza con \033[1m' {PR.letra} '\033[0m: \x1B[3m{PR.definicion}\x1B[0m")


# adivinar: lista(PalabraRosco) str -> bool
# Función: dado un rosco y un string palabra, entrega True si la palabra entregada corresponde exactamente \
#          a la palabra del PalabraRosco que se encuentra en la primera posición del rosco
# Ej: adivinar(Rosco, 'abelardo') entrega False
def adivinar(Lrosco, Palabra):
    assert esLista(Lrosco)
    assert type(Palabra) == str
    # hacemos uso de la función lower para prevenir casos que sí hubiesen sido admisibles pero no por la comparación case sensitive de strings
    if cabeza(Lrosco).palabra == Palabra.lower():
        return True
    else:
        return False
# Test:
assert adivinar(Roscoej1, 'australopithecus') == False
assert adivinar(Roscoej1, 'AcEpTaBlE') == True == adivinar(Roscoej1, 'aceptable')


# --------------------------------


# --------------------------------
# Funciones Principales

# iniciar: ->
# Función:
# Ej:
def iniciar(dificultad):
    return 


# anyapalabra: ->
# Función:
# Ej:
def anyapalabra(Lrosco):
    if siguientePendiente == False:
        print(f"Wena, ganaste humanx")
    

# --------------------------------