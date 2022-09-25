from lista import *
from palabras import crearPalabra, PalabraRosco, crearRosco, mostrarRosco

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
# --------------------------------



# --------------------------------
# Funciones que operan con Rosco(lista de PalabraRosco)
# --------------------------------



# --------------------------------
# Funciones Principales
# --------------------------------


