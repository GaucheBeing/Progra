import estructura
from random import choice
from lista import *
'''
Se solicita no destruir o modificar irreparablemente este modulo, para
garantizar el correcto funcionamiento de las funciones de la tarea
'''

# ----------------------------------
letras_secretas = ['A','B','C','D','E','F','G','H','I','J','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z']
datos_encriptados = {}

for l in letras_secretas:
    datos_encriptados[l] = []
datos_encriptados['A'].append(['abrazar', 'Cennir o rodear algo o a alguien con los brazos, especialmente como muestra de afecto o carinno'])
datos_encriptados['A'].append(['aliento', 'Aire que se expulsa por la boca al respirar'])
datos_encriptados['A'].append(['aeropuerto', 'Conjunto de instalaciones que sirve de estacion para el trafico de los aviones de pasajeros y mercancias'])
datos_encriptados['A'].append(['aceptable', 'Que se puede aceptar'])
datos_encriptados['B'].append(['balon', 'Pelota grande, usada en juegos o con fines terapeuticos'])
datos_encriptados['B'].append(['beso', 'Accion y efecto de besar'])
datos_encriptados['B'].append(['bicicleta', 'Vehiculo de dos ruedas, normalmente de igual tamanno, cuyos pedales transmiten el movimiento a la rueda trasera por medio de un plato, un pinnon y una cadena'])
datos_encriptados['B'].append(['bandera', 'Tela de forma comunmente rectangular, que se asegura por uno de sus lados a un asta o a una driza y se emplea como ensenna o sennal de una nacion, una ciudad o una institucion'])
datos_encriptados['C'].append(['caballo', 'Mamifero solipedo del orden de los perisodactilos, de tamanno grande y extremidades largas, cuello y cola poblados de cerdas largas y abundantes, que se domestica facilmente y suele utilizarse como montura o animal de tiro'])
datos_encriptados['C'].append(['casa', 'Edificio para habitar'])
datos_encriptados['C'].append(['consejo', 'Opinion que se expresa para orientar una actuacion de una determinada manera'])
datos_encriptados['C'].append(['computador', 'Que computa'])
datos_encriptados['D'].append(['doctor', 'Persona que ha recibido el mas alto grado academico universitario'])
datos_encriptados['D'].append(['dinosaurio', 'Reptil fosil de gran tamanno, con cabeza pequenna, cuello largo, cola robusta y larga, y, en general, extremidades posteriores mas largas que las anteriores'])
datos_encriptados['D'].append(['diamante', 'Piedra preciosa constituida por carbono cristalizado en el sistema cubico, que se utiliza en joyeria por su brillo y transparencia y en la industria por su elevada dureza'])
datos_encriptados['D'].append(['declarar', 'Manifestar, hacer publico'])
datos_encriptados['E'].append(['eclipse', 'Ocultacion transitoria total o parcial de un astro por interposicion de otro cuerpo celeste'])
datos_encriptados['E'].append(['elefante', 'Mamifero del orden de los proboscidios, el mayor de los animales terrestres, con cabeza y ojos pequennos, orejas grandes y colgantes, nariz y labio superior unidos y muy prolongados en forma de trompa prensil, y dos dientes incisivos, macizos y muy grandes, vulgarmente llamados colmillos, que vive en Asia y africa'])
datos_encriptados['E'].append(['emboscada', ' Ocultacion de una o varias personas en parte retirada para atacar por sorpresa a otra u otras'])
datos_encriptados['E'].append(['explicar', 'Declarar, manifestar, dar a conocer lo que alguien piensa'])
datos_encriptados['F'].append(['fuego', 'Fenomeno caracterizado por la emision de calor y de luz, generalmente con llama'])
datos_encriptados['F'].append(['flor', 'Brote de muchas plantas, formado por hojas de colores, del que se formara el fruto'])
datos_encriptados['F'].append(['fantasma', 'Imagen de una persona muerta que, segun algunos, se aparece a los vivos'])
datos_encriptados['F'].append(['fabrica', 'Establecimiento dotado de la maquinaria, herramienta e instalaciones necesarias para la fabricacion de ciertos objetos, obtencion de determinados productos o transformacion industrial de una fuente de energia'])
datos_encriptados['G'].append(['gato', 'Mamifero carnivoro de la familia de los felidos, digitigrado, domestico, de unos 50 cm de largo desde la cabeza hasta el arranque de la cola, que por si sola mide unos 20 cm, de cabeza redonda, lengua muy aspera, patas cortas y pelaje espeso, suave, de color blanco, gris, pardo, rojizo o negro, que se empleaba en algunos lugares para cazar ratones'])
datos_encriptados['G'].append(['galleta', 'Pasta compuesta de harina, azucar y a veces huevo, manteca o confituras diversas, que, dividida en trozos pequennos y moldeados o modelados en forma varia, se cuecen al horno'])
datos_encriptados['G'].append(['guitarra', 'Instrumento musical de cuerda compuesto por una caja de resonancia en forma de ocho, un mastil largo con trastes, y cuerdas, generalmente seis, que se hacen sonar con los dedos'])
datos_encriptados['G'].append(['guante', 'Prenda para cubrir la mano, que se hace, por lo comun, de piel, tela o tejido de punto, y tiene una funda para cada dedo'])
datos_encriptados['H'].append(['hada', 'Ser fantastico que se representa bajo la forma de mujer, a quien se atribuyen poderes magicos'])
datos_encriptados['H'].append(['hospital', 'Establecimiento destinado al diagnostico y tratamiento de enfermos, donde a menudo se practican la investigacion y la docencia'])
datos_encriptados['H'].append(['huevo', 'Cuerpo redondeado, de tamanno y dureza variables, que producen las hembras de las aves o de otras especies animales, y que contiene el germen del embrion y las sustancias destinadas a su nutricion durante la incubacion'])
datos_encriptados['H'].append(['hielo', 'Agua convertida en cuerpo solido y cristalino por un descenso suficiente de temperatura'])
datos_encriptados['I'].append(['invierno', 'Estacion del anno que, astronomicamente, comienza en el solsticio del mismo nombre y termina en el equinoccio de primavera'])
datos_encriptados['I'].append(['isla', 'Porcion de tierra rodeada de agua por todas partes'])
datos_encriptados['I'].append(['iglesia', 'Templo cristiano'])
datos_encriptados['I'].append(['instituto', 'Centro estatal de ensennanza secundaria'])
datos_encriptados['J'].append(['jaula', 'Armazon, cerrada o no segun los casos, hecha con barras o listones y destinada a encerrar generalmente animales'])
datos_encriptados['J'].append(['jugo', 'Zumo de las sustancias animales o vegetales sacado por presion, coccion o destilacion'])
datos_encriptados['J'].append(['joya', 'Adorno de oro, plata o platino, con perlas o piedras preciosas o sin ellas'])
datos_encriptados['J'].append(['jirafa', 'Mamifero artiodactilo rumiante, originario de africa, de hasta cinco metros de altura de los que la mitad corresponden al cuello, largo, esbelto y rigido, de pelaje leonado con grandes manchas poligonales oscuras y la cabeza con dos pequennos cuernos cubiertos de piel.'])
#datos_encriptados['K']append(['karaoke', 'Diversion consistente en interpretar una cancion sobre un fondo musical grabado, mientras se sigue la letra que aparece en una pantalla.'])
#datos_encriptados['K']append(['kiwi', 'Ave apterigiforme, del tamanno de una gallina, que habita en Nueva Zelanda.'])
#datos_encriptados['K']append(['kayak', 'Canoa de pesca usada por los esquimales, tradicionalmente fabricada con piel de foca, cuya cubierta solo tiene una abertura, cerrada con un material impermeable que se ajusta al tronco del tripulante.'])
#datos_encriptados['K']append(['koala', 'Mamifero marsupial arboricola parecido a un oso pequenno, propio de los eucaliptales australianos.'])
datos_encriptados['L'].append(['lapiz', 'Utensilio para escribir o dibujar formado por un cilindro o prisma de madera con una barra de grafito en su interior'])
datos_encriptados['L'].append(['lobo', 'Mamifero carnicero, semejante a un perro grande, pelaje de color gris oscuro, cabeza aguzada, orejas tiesas y cola larga con mucho pelo, salvaje, gregario y que ataca al ganado'])
datos_encriptados['L'].append(['libro', 'Conjunto de muchas hojas de papel u otro material semejante que, encuadernadas, forman un volumen'])
datos_encriptados['L'].append(['luna', 'unico satelite natural de la Tierra, que se encuentra a 384400 km de esta, tiene un diametro de 3476 km y realiza un giro completo alrededor de aquella cada 27,32 dias'])
datos_encriptados['M'].append(['mano', 'Parte del cuerpo humano unida a la extremidad del antebrazo y que comprende desde la munneca inclusive hasta la punta de los dedos'])
datos_encriptados['M'].append(['momia', 'Cadaver que naturalmente o por preparacion artificial se deseca con el transcurso del tiempo sin entrar en putrefaccion'])
datos_encriptados['M'].append(['mapa', 'Representacion geografica de la Tierra o parte de ella en una superficie plana'])
datos_encriptados['M'].append(['madre', 'Mujer o animal hembra que ha parido a otro ser de su misma especie'])
datos_encriptados['N'].append(['nieve', 'Agua helada que se desprende de las nubes en cristales sumamente pequennos, los cuales, agrupandose al caer, llegan al suelo en copos blancos'])
datos_encriptados['N'].append(['nube', 'Agregado visible de minusculas gotitas de agua, de cristales de hielo o de ambos, suspendido en la atmosfera y producido por la condensacion de vapor de agua'])
datos_encriptados['N'].append(['negro', 'Dicho de un color: Semejante al del carbon o al de la oscuridad total'])
datos_encriptados['N'].append(['nariz', 'organo prominente del rostro humano, entre la frente y la boca, con dos orificios, que forma parte del aparato respiratorio'])
datos_encriptados['O'].append(['ojo', 'organo de la vista en el ser humano y en los animales'])
datos_encriptados['O'].append(['olla', 'Vasija redonda de barro o metal, que comunmente forma barriga, con cuello y boca anchos y con una o dos asas, la cual sirve para cocer alimentos, calentar agua, etc'])
datos_encriptados['O'].append(['oveja', 'Mamifero rumiante de tamanno mediano, que posee lana y carne muy apreciadas, cuyo macho presenta cuernos arrollados en espiral y de cuya hembra se obtiene leche con la que se elaboran quesos'])
datos_encriptados['O'].append(['ovni', 'Objeto volador no identificado, al que en ocasiones se considera como una nave espacial de procedencia extraterrestre'])
datos_encriptados['P'].append(['payaso', 'Dicho de una persona: Que hace reir con sus dichos o gestos'])
datos_encriptados['P'].append(['peine', 'Utensilio de madera, marfil, concha u otra materia, provisto de dientes muy juntos, con el cual se desenreda y compone el pelo'])
datos_encriptados['P'].append(['pato', 'Ave palmipeda acuatica, con el pico aplanado y patas cortas, con dedos unidos entre si por una membrana, de la cual existen varias especies, algunas de ellas domesticas'])
datos_encriptados['P'].append(['padre', 'Varon o animal macho que ha engendrado a otro ser de su misma especie'])
datos_encriptados['Q'].append(['quejar', 'Expresar con la voz el dolor o pena que se siente'])
datos_encriptados['Q'].append(['quena', 'Flauta aborigen del Altiplano, construida tradicionalmente con canna, hueso o barro, que mide unos 50 cm de longitud y se caracteriza por su escotadura en forma de U con el borde anterior afilado'])
datos_encriptados['Q'].append(['quirofano', 'Local convenientemente acondicionado para hacer operaciones quirurgicas de manera que puedan presenciarse al traves de una separacion de cristal, y, por ext., cualquier sala donde se efectuan estas operaciones'])
datos_encriptados['Q'].append(['queso', 'Producto obtenido por maduracion de la cuajada de la leche con caracteristicas propias para cada uno de los tipos segun su origen o metodo de fabricacion'])
datos_encriptados['R'].append(['rey', 'Monarca soberano de un reino'])
datos_encriptados['R'].append(['rueda', 'Objeto circular, de poco grosor respecto a su radio, que puede girar sobre un eje de multiples aplicaciones'])
datos_encriptados['R'].append(['raqueta', 'Instrumento que se utiliza para golpear la pelota en ciertos juegos y deportes, como el tenis o el badminton; es de madera, metal u otros materiales mas ligeros, y consta de un mango y una parte ovalada generalmente con cuerdas cruzadas en su interior'])
datos_encriptados['R'].append(['reciclar', 'Someter materiales usados o desperdicios a un proceso de transformacion o aprovechamiento para que puedan ser nuevamente utilizados'])
datos_encriptados['S'].append(['serpiente', 'Reptil sin extremidades, de cuerpo muy alargado y estrecho, con la cabeza aplastada, la boca grande y la piel escamosa; se aplica este nombre especialmente a los de gran tamanno; hay especies terrestres y especies acuaticas'])
datos_encriptados['S'].append(['sopa', 'Plato de caldo con pasta, arroz, semola, hortalizas, u otros alimentos troceados que se cuecen en ese caldo'])
datos_encriptados['S'].append(['sol', 'Estrella con luz propia alrededor de la cual gira la Tierra'])
datos_encriptados['S'].append(['suma', 'Operacion aritmetica que consiste en reunir varias cantidades en una sola; se representa con el signo +'])
datos_encriptados['T'].append(['tierra', 'Planeta del Sistema Solar, tercero en la proximidad al Sol, entre Venus y Marte, habitado por el hombre'])
datos_encriptados['T'].append(['taza', 'Recipiente que sirve para beber liquidos, en especial bebidas calientes, como cafe o te; forma parte del servicio de mesa, es mas ancho que alto, generalmente mas ancho en la boca que en la base, y esta provisto de un asa'])
datos_encriptados['T'].append(['telefono', 'Sistema de comunicacion que transmite la voz y el sonido a larga distancia por medios electricos o electromagneticos'])
datos_encriptados['T'].append(['titere', 'Munneco que se mueve por medio de una cruceta de la cual cuelgan unos hilos que van atados a su cuerpo o bien metiendo la mano por debajo del vestido; se usa generalmente para representaciones teatrales infantiles o populares'])
datos_encriptados['U'].append(['unicornio', 'Animal fabuloso con figura de caballo y con un cuerno recto en mitad de la frente'])
datos_encriptados['U'].append(['urna', 'Recipiente o caja de piedra o de metal que se utiliza para guardar ciertas cosas, como dinero, joyas o las cenizas de las personas muertas'])
datos_encriptados['U'].append(['universo', 'Conjunto de todo lo que tiene existencia fisica, en la Tierra y fuera de ella'])
datos_encriptados['U'].append(['uniforme', 'Que tiene o presenta la misma forma'])
datos_encriptados['V'].append(['vino', 'Bebida alcoholica que se obtiene por fermentacion del jugo de la uva'])
datos_encriptados['V'].append(['viento', 'Corriente de aire que se produce en la atmosfera al variar la presion'])
datos_encriptados['V'].append(['viajar', 'Visitar o recorrer diversos lugares o paises, por cualquier medio de locomocion'])
datos_encriptados['V'].append(['video', 'Sistema que permite la grabacion de imagenes y sonidos en una cinta magnetica que despues puede reproducirse y verse en la pantalla de un televisor'])
datos_encriptados['X'].append(['xilofono', 'Instrumento musical de percusion formado por una serie de laminas de madera dispuestas horizontalmente y ordenadas segun su tamanno que, al ser golpeadas, emiten sonidos correspondientes a diferentes notas musicales; se toca con dos o cuatro macillas'])
datos_encriptados['X'].append(['xenofobia', 'Rechazo a los extranjeros'])
datos_encriptados['X'].append(['xenon', 'Elemento quimico de numero atomico 54, masa atomica 131,3 y simbolo Xe ; es un gas noble incoloro e inodoro, que esta presente en la atmosfera en cantidades minimas y se usa en ciertos mecanismos de iluminacion'])
datos_encriptados['X'].append(['xilofago', 'Que se alimenta de madera'])
datos_encriptados['Y'].append(['yate', 'Embarcacion de recreo a motor o a vela, de manga o anchura mayor que un velero, con camarotes y generalmente lujosa'])
datos_encriptados['Y'].append(['yogurt', 'Alimento liquido y espeso o pastoso, de sabor agrio, que se obtiene por fermentacion de la leche de vaca entera o desnatada'])
datos_encriptados['Y'].append(['yunque', 'Bloque de hierro, generalmente con uno de sus lados acabado en punta, sobre el que se trabajan los metales al rojo vivo golpeandolos con un martillo'])
datos_encriptados['Y'].append(['yema', 'Nucleo de los huevos de los vertebrados oviparos; es esferoidal, de color amarillo y esta rodeada por la clara'])
datos_encriptados['Z'].append(['zapato', 'Calzado que cubre total o parcialmente el pie sin sobrepasar el tobillo, con una suela de un material casi siempre mas duro que el resto'])
datos_encriptados['Z'].append(['zafiro', 'Mineral compuesto de oxido de aluminio, de color azul y extraordinaria dureza, que se usa para tallar diamantes; es una variedad del corindon'])
datos_encriptados['Z'].append(['zoologico', 'Recinto con instalaciones adecuadas para conservar, cuidar y criar especies diferentes de animales, especialmente salvajes y exoticos, que puede ser visitado por el publico'])
datos_encriptados['Z'].append(['zanahoria', 'Planta herbacea de hojas muy divididas, flores blancas y fruto seco y comprimido'])

# nico gavilan
datos_encriptados['A'].append(['analitico', 'Perteneciente o relativo al analisis'])
datos_encriptados['B'].append(['bellotero', 'Persona que recolecta o vende bellotas'])
datos_encriptados['C'].append(['clave', 'Instrumento musical de percusion', 'de origen cubano', 'que consiste en dos palos pequennos que se golpean uno contra otro'])
datos_encriptados['D'].append(['desclavar', 'Arrancar o quitar un clavo'])
datos_encriptados['E'].append(['edificable', 'Dicho de un terreno. Propio para edificar'])
datos_encriptados['F'].append(['forma', 'Modo o manera en que se hace o en que ocurre algo'])
datos_encriptados['G'].append(['gitanismo', 'Vocablo o giro propio de la lengua que hablan los gitanos'])
datos_encriptados['H'].append(['hondero', 'Soldado que usaba honda en la guerra'])
datos_encriptados['I'].append(['inadvertencia', 'Falta de advertencia'])
#datos_encriptados['J'].append(['injustificadamente', 'Contiene la J: De manera injustificada'])
datos_encriptados['I'].append(['injustificadamente', 'De manera injustificada'])
datos_encriptados['L'].append(['lucha', 'Esfuerzo que se hace para resistir a una fuerza hostil o a una tentacion,para subsistir o para alcanzar algun objetivo'])
datos_encriptados['M'].append(['marcar', 'Pulsar en un telefono los numeros de otro para comunicar con el'])
#datos_encriptados['N'].append(['desnivelado', 'Contiene la N: Que presenta desnivel'])
datos_encriptados['D'].append(['desnivelado', 'Que presenta desnivel'])
datos_encriptados['O'].append(['oceanografico', 'Perteneciente o relativo a la oceanografia'])
datos_encriptados['P'].append(['presente', 'Obsequio,regalo que alguien da a otra persona en sennal de reconocimiento o de afecto'])
#datos_encriptados['Q'].append(['etiqueta', 'Contiene la Q: Ceremonial de los estilos', 'usos y costumbres que se debe guardar en actos publicos solemnes'])
datos_encriptados['E'].append(['etiqueta', 'Ceremonial de los estilos', 'usos y costumbres que se debe guardar en actos publicos solemnes'])
datos_encriptados['R'].append(['repartir', 'Entregar a personas distintas lo que han encargado o deben recibir'])
datos_encriptados['S'].append(['subarriendo', 'Accion y efecto de subarrendar'])
datos_encriptados['T'].append(['trifloro', 'Que tiene tres flores'])
#datos_encriptados['U'].append(['cuadruplicar', 'Contiene la U: Hacer cuadruple algo o multiplicarlo por cuatro'])
datos_encriptados['C'].append(['cuadruplicar', 'Hacer cuadruple algo o multiplicarlo por cuatro'])
datos_encriptados['V'].append(['volante', 'Hoja impresa de caracter politico o publicitario,que se reparte en lugares publicos'])
#datos_encriptados['X'].append(['extincion', 'Contiene la X: Accion y efecto de extinguir o extinguirse'])
datos_encriptados['E'].append(['extincion', 'Accion y efecto de extinguir o extinguirse'])
#datos_encriptados['Y'].append(['gay', 'Contiene la Y: Perteneciente o relativo a los homosexuales'])
datos_encriptados['G'].append(['gay', 'Perteneciente o relativo a los homosexuales'])
#datos_encriptados['Z'].append(['arqueozoologia', 'Contiene la Z: Parte de la arqueologia que se ocupa especialmente del estudio de restos de animales en yacimientos de antiguas culturas'])
datos_encriptados['A'].append(['arqueozoologia', 'Parte de la arqueologia que se ocupa especialmente del estudio de restos de animales en yacimientos de antiguas culturas'])

# ----------------------------------

### definicion de estructura PalabraRosco ###

# PalabraRosco: letra(str) palabra(str) definicion(str) status(str)
estructura.crear('PalabraRosco','letra palabra definicion status')

### definicion de función validadora ###

# esPalabraRosco: any -> bool
# valida si el dato entregado corresponde a una PalabraRosco valida
# ej: esPalabraRosco('pasapalabra') entrega False
def esPalabraRosco(PR):
    if type(PR) != PalabraRosco:
        return False
    if type(PR.letra) != str or len(PR.letra) != 1:
        return False
    if type(PR.palabra) != str:
        return False
    if type(PR.definicion) != str:
        return False
    if type(PR.status) != str:
        return False
    if PR.status not in ['pendiente','correcta','incorrecta']:
        return False
    return True

assert not esPalabraRosco('pasapalabra')
testRA = PalabraRosco('A', 'abracadabra',\
                      'Palabra cabalistica a la que se atribuyen efectos magicos.' ,'pendiente')
assert esPalabraRosco(testRA)



### definicion de función crearPalabra ###

# crearPalabra: str -> PalabraRosco
# entrega una 'pelotita' del rosco, que contiene una palabra aleatoria,
#  su definición, su letra asociada, y estado 'Pendiente'
# Ej: crearPalabra('R') puede entregar:
#   PalabraRosco('R', 'rey', 'Monarca soberano de un reino', 'Pendiente')
def crearPalabra(letra):
    assert len(letra) == 1, 'Error: Se ingresa algo que no es una letra'
    assert letra.upper() in letras_secretas, 'Error: No hay palabras con la letra ingresada'
    
    seleccion = datos_encriptados[letra.upper()]
    ganadora = choice(seleccion)
    # lawful debug
    nueva = PalabraRosco(letra.upper(),ganadora[0],ganadora[1],'pendiente')
    # chaos debug
    #kkk = choice(['pendiente','correcta','incorrecta'])
    #nueva = PalabraRosco(letra.upper(),ganadora[0],ganadora[1],kkk)
    return nueva


### definicion de función crearRosco ###

def construirListaRec(Lp):
    if Lp == []:
        return listaVacia
    elem = Lp.pop(0)
    return lista(elem,construirListaRec(Lp))

# crearRosco: lista(str) -> lista(PalabraRosco)
# dada una lista de letras, crea una lista de PalabraRosco para cada letra dada
# ej: crearRosco(...)
def crearRosco(S):
    LdeLetras = list(S)
    L = construirListaRec(LdeLetras)
    return crearRoscoAux(L)

def crearRoscoAux(listaLetras):
    assert esLista(listaLetras)

    if listaLetras == listaVacia:
        return listaVacia
    else:
        letraAct = cabeza(listaLetras)
        pelotita = crearPalabra(letraAct)
        return lista(pelotita, crearRoscoAux(cola(listaLetras)))


### definicion de función mostrarRosco ###

# cadenaLetras: lista(PalabraRosco) -> str
# a partir del rosco, crea una string con todas las letras en el orden actual
# ej: rosco = A -> B -> C -> .... -> Y -> Z -> listaVacia
#     cadenaLetras(rosco) entrega 'A B C ... Y Z '
def cadenaLetras(LR):
    assert esLista(LR)
    
    if LR == listaVacia:
        return ''
    else:
        act = cabeza(LR)
        return act.letra + ' ' + cadenaLetras(cola(LR))


# cadenaStatus: lista(PalabraRosco) -> str
# a partir del rosco, crea una string con todos los status en el orden actual
# ej: rosco = A -> B -> C -> .... -> Y -> Z -> listaVacia
#     cadenaStatus(rosco) entrega '_ o x ... _ x '
def cadenaStatus(LR):
    assert esLista(LR)

    if LR == listaVacia:
        return ''
    else:
        act = cabeza(LR)
        simb = ''
        if act.status == 'pendiente':
            simb = '_'
        elif act.status == 'correcta':
            simb = 'o'
        else:
            simb = 'x'
        
        return simb + ' ' + cadenaStatus(cola(LR))

# mostrarRosco: lista(PalabraRosco) -> None
# muestra en pantalla el estado actual de un Rosco
# ej: mostrarRosco(rosco)
#      A B C ... Y Z       
#      _ o x ... _ x 
def mostrarRosco(LR):
    assert esLista(LR)
    
    print(cadenaLetras(LR))
    print(cadenaStatus(LR))
