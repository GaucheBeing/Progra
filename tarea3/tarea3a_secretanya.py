
alfabeto = " 0123456789abcdefghijklmnopqrstuvwxyz"


# --------------------------------
# Funciones de (des)encriptado
# --------------------------------


# posicion: str str -> int
# dado un carácter string entregar el número de la posición de este en el abecedario. Si no existe en el abecedario, entonces entregar -1
# ej: posicion('a') => 11 y posición('ñ') => -1
def posicion(S, abecedario):
    assert type(S) == str
    if S.lower() in abecedario:
        return list(abecedario).index(S)
    else: return -1
# test
assert posicion('a', alfabeto) == 11
assert posicion('ñ', alfabeto) == -1
assert posicion('b', alfabeto) == 12


# encriptadoStrix: str int str -> str
# recibe un string que representa un mensaje y un número que representa la llave, y entrega un nuevo string que representa el mensaje encriptado
# ej: encriptadoStrix('anya tiene hambre >:c',8) => 'iv5i70qmvm7piujzm7>:k' y encriptadoStrix("mensaje secreto!!",0) => 'mensaje secreto!!' 
def encriptadoStrix(msg, llave, abecedario):
    assert type(msg) == str,        'tu mensaje debe ser una palabra o frase'
    assert type(llave) == int,      'tu "llave" debe ser un número entero'

    # transformamos la lista compuesta de los carácteres del msg a su índice equivalente en el abecedario
    # es decir, vamos de letra a índice | letra (si es que no está en el abecedario)
    LnumRepresentante_msg = []
    for i in list(msg):
        if posicion(i, abecedario) != -1:
            LnumRepresentante_msg.append(posicion(i, abecedario))
        else: LnumRepresentante_msg.append(i)
    # su equivalente por comprensión dado que no vimos if / else
    # LnumRepresentante_msg = [posicion(i, abecedario) if i in abecedario else i for i in list(msg)]

    # función que mapea dos objetos y devuelve al elemento representante en Z_{len(L)} de la suma entre los números originales si estos son en efecto números
    # en caso contrario se devolverán los mismos parámetros entregados
    encrypt = lambda x, n, L: (x+n) % len(L) if type(x)==int else x 

    # lista de imagenes de la función encrypt que parte desde el conjunto de todos los carácteres del msg representados por su índice en el abecedario hacia el producto cartesiano Z_{37} * list(msg)
    # es decir, vamos de índice | letra a índice | letra
    LnumRepresentante_msgEncriptado = [encrypt(i, llave, abecedario) for i in LnumRepresentante_msg]

    # transformamos la lista numérica ya encriptada que representa nuestro msg hacia su equivalente en el abecedario
    # es decir, vamos de índice | letra a letra
    msgEncriptado = []
    for i in LnumRepresentante_msgEncriptado:
        if type(i) == int:
            msgEncriptado.append(abecedario[i])
        else: msgEncriptado.append(i)
    # su equivalente por comprensión
    # msgEncriptado = [abecedario[i] if type(i)==int else i for i in LnumRepresentante_msgEncriptado]
    return ''.join(msgEncriptado)

# test
assert encriptadoStrix('anya tiene hambre >:c', 8, alfabeto) == 'iv5i70qmvm7piujzm7>:k'
assert encriptadoStrix("mensaje secreto!!", 0, alfabeto) == 'mensaje secreto!!'
assert encriptadoStrix('hola mundo!', 1, alfabeto) == 'ipmb0nvoep!'


# desencriptadoStrix: str int str -> str
# recibe un string que representa un mensaje encriptado y un número que representa la llave, y entrega un nuevo string que representa el mensaje desencriptado
# ej: desencriptadoStrix('iv5i70qmvm7piujzm7>:k',8) => 'anya tiene hambre >:c' y desencriptadoStrix("mensaje secreto!!",0) => 'mensaje secreto!!'
def desencriptadoStrix(msg, llave, abecedario):
    assert type(msg) == str,        'tu mensaje debe ser una palabra o frase'
    assert type(llave) == int,      'tu "llave" debe ser un número entero'
    # análogo a encriptar
    LnumRepresentante_msg = [posicion(i, abecedario) if i in abecedario else i for i in list(msg)]
    desencrypt = lambda x, n, L: (x-n) % len(L) if type(x)==int else x
    LnumRepresentante_msgDesencriptado = [desencrypt(i, llave, abecedario) for i in LnumRepresentante_msg]
    msgDesencriptado = [abecedario[i] if type(i)==int else i for i in LnumRepresentante_msgDesencriptado]
    return ''.join(msgDesencriptado)

# test
assert desencriptadoStrix('iv5i70qmvm7piujzm7>:k', 8, alfabeto) == 'anya tiene hambre >:c'
assert desencriptadoStrix("mensaje secreto!!", 0, alfabeto) == 'mensaje secreto!!'
assert desencriptadoStrix('ipmb0nvoep!', 1, alfabeto) == 'hola mundo!'


# --------------------------------
# Función principal
# --------------------------------


# secretanya: None -> None
# función recursiva que llama al resto de funciones para (de)codificar mensajes
def secretanya():
    print('Bienvenidx al (de)codificador humanx! escribe la letra en paréntesis para elegir\n\n')
    def _secretanya():
        print('Acciones: Encriptar mensaje (E) - Desencriptar mensaje (D) - Salir (S)\n\n--------------------\n')
        action = input('Acción: ').lower()
        if action in ['salir', 's']:
            print('Hasta pronto!')
            return None 
        msg = input('Mensaje: ')
        key = input('Llave (número): ')
        if not key.isnumeric():
            print('La llave debe ser un número, partamos otra vez\n')
            return _secretanya()
        if action in ['encriptar', 'e']:
            print(f'Mensaje encriptado: {encriptadoStrix(msg, int(key), alfabeto)}')
        elif action in ['desencriptar', 'd']:
            print(f'Mensaje desencriptado: {desencriptadoStrix(msg, int(key), alfabeto)}')
        print('\n--------------------\n')
        return _secretanya()
    return _secretanya()
