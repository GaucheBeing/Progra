alfabeto = " 0123456789abcdefghijklmnopqrstuvwxyz"
endl = "\n----------------------------------------\n"


# --------------------------------
# Funciones de (des)encriptado
# --------------------------------


# posicion: str str -> int
# dado un carácter string entregar el número de la posición de este en el abecedario. Si no existe en el abecedario, entonces entregar -1
# ej: posicion('a') => 11 y posición('ñ') => -1
def posicion(S, abecedario=alfabeto):
    assert type(S) == str
    if S in abecedario:
        return list(abecedario).index(S)
    else: return -1
# test
assert posicion('a') == 11
assert posicion('ñ') == -1
assert posicion('o') == 25
assert posicion('S') == -1


# encriptadoStrix: str int str -> str
# recibe un string que representa un mensaje y un número que representa la llave, y entrega un nuevo string que representa el mensaje encriptado
# ej: encriptadoStrix('anya tiene hambre >:c',8) => 'iv5i70qmvm7piujzm7>:k' y encriptadoStrix("mensaje secreto!!",0) => 'mensaje secreto!!' 
def encriptadoStrix(msg, llave, abecedario=alfabeto):
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
assert encriptadoStrix('anya tiene hambre >:c', 8) == 'iv5i70qmvm7piujzm7>:k'
assert encriptadoStrix("mensaje secreto!!", 0) == 'mensaje secreto!!'
assert encriptadoStrix('hola mundo!', 1) == 'ipmb0nvoep!'


# desencriptadoStrix: str int str -> str
# recibe un string que representa un mensaje encriptado y un número que representa la llave, y entrega un nuevo string que representa el mensaje desencriptado
# ej: desencriptadoStrix('iv5i70qmvm7piujzm7>:k',8) => 'anya tiene hambre >:c' y desencriptadoStrix("mensaje secreto!!",0) => 'mensaje secreto!!'
def desencriptadoStrix(msg, llave, abecedario=alfabeto):
    assert type(msg) == str,        'tu mensaje debe ser una palabra o frase'
    assert type(llave) == int,      'tu "llave" debe ser un número entero'
    # análogo a encriptar
    LnumRepresentante_msg = [posicion(i, abecedario) if i in abecedario else i for i in list(msg)]
    desencrypt = lambda x, n, L: (x-n) % len(L) if type(x)==int else x
    LnumRepresentante_msgDesencriptado = [desencrypt(i, llave, abecedario) for i in LnumRepresentante_msg]
    msgDesencriptado = [abecedario[i] if type(i)==int else i for i in LnumRepresentante_msgDesencriptado]
    return ''.join(msgDesencriptado)

# test
assert desencriptadoStrix('iv5i70qmvm7piujzm7>:k', 8,) == 'anya tiene hambre >:c'
assert desencriptadoStrix("mensaje secreto!!", 0,) == 'mensaje secreto!!'
assert desencriptadoStrix('ipmb0nvoep!', 1,) == 'hola mundo!'


# --------------------------------
# Función principal
# --------------------------------


# secretanya: None -> None
# función iterativa que llama al resto de funciones para (de)codificar mensajes + reescribirlos en un archivo .txt 
def secretanya():
    # presentación :D
    print("Bienvenidx al (de)codificador humanx! escribe la letra en paréntesis para elegir\n\n")
    # creamos una lista vacía con el propósito de almacenar otras listas 
    Lcodificaciones = []
    while True:
        print(f"Acciones: Encriptar mensaje (E) - Desencriptar mensaje (D) - Salir (S)\n{endl}")
        action = input("Acción: ").lower()
        if action not in ["salir", 's', "encriptar", 'e', "desencriptar", 'd']:
            print("escribe la letra en paréntesis para elegir\n")
            continue
        if action in ["salir", 's']:
            break
        msg = input("Mensaje: ")
        key = input("Llave (número): ")
        if not key.isnumeric():
            print("La llave debe ser un número, partamos otra vez\n")
            continue
        if action in ["encriptar", 'e']:
            msgEncrypt = encriptadoStrix(msg, int(key),)
            print(f"Mensaje encriptado: {msgEncrypt}\n{endl}")
            # inserción iterativa de listas compuestas del input de la persona usuarix por orden de llegada, en lugar de diccionario asociaremos al valor 1 con el mensaje encriptado
            Lcodificaciones.append([action, msg, str(key), [1, msgEncrypt]])
        elif action in ["desencriptar", 'd']:
            msgDesencrypt = desencriptadoStrix(msg, int(key),)
            print(f"Mensaje desencriptado: {msgDesencrypt}\n{endl}")
            # análogo al caso previo a excepción de que el valor 0 está asociado a una "llave" que es en verdad el mensaje desencriptado
            Lcodificaciones.append([action, msg, str(key), [0, msgDesencrypt]])
        print(endl)

    
    # preguntamos a la persona usuarix si desea grabar en un archivo lo que escribió en el programa
    grabar = input("\n¿Quieres guardar registro de lo escrito humanx? (y/n)").lower()
    if grabar in ["si", 's', "yes",'y']:
        file = input("Nombre del archivo: ")
        file = open(file + ".txt", 'w', encoding="utf-8")
        file.write(f"Transcripción del diálogo humanx-(de)codificador, se ignoran los intentos de uso fallidos {endl}\n")
        # accedemos a cada codificación bien hecha y guardada en la lista de codificaciones, escribimos los elementos de estas listas y 
        # hacemos la distinción en los casos que se codificó o encriptó un mensaje 
        for cod in Lcodificaciones:
            file.write(f"Acción: {cod[0]}\nMensaje: {cod[1]}\nLlave: {cod[2]}\n")
            if cod[3][0] == 1:
                file.write(f"Mensaje encriptado: {cod[3][1]}")
            else:
                file.write(f"Mensaje desencriptado: {cod[3][1]}")
            file.write(f"\n{endl}\n") 

    print("Hasta pronto!\n")


# recursive_secretanya: None -> None
# función recursiva que llama al resto de funciones para (de)codificar mensajes + reescribirlos en un archivo .txt
def recursive_secretanya():
    print("Bienvenidx al (de)codificador humanx! escribe la letra en paréntesis para elegir\n\n")
    Lcodificaciones = []
    def _recursive_secretanya():
        print(f"Acciones: Encriptar mensaje (E) - Desencriptar mensaje (D) - Salir (S)\n{endl}")
        action = input("Acción: ").lower()
        if action not in ["salir", 's', "encriptar", 'e', "desencriptar", 'd']:
            print("escribe la letra en paréntesis para elegir\n")
            return _recursive_secretanya()
        if action in ["salir", 's']:
            return _transcriptor(Lcodificaciones) 
        msg = input("Mensaje: ")
        key = input("Llave (número): ")
        if not key.isnumeric():
            print("La llave debe ser un número, partamos otra vez\n")
            return _recursive_secretanya()
        if action in ["encriptar", 'e']:
            msgEncrypt = encriptadoStrix(msg, int(key),)
            print(f"Mensaje encriptado: {msgEncrypt}\n{endl}")
            Lcodificaciones.append([action, msg, str(key), [1, msgEncrypt]])
        elif action in ["desencriptar", 'd']:
            msgDesencrypt = desencriptadoStrix(msg, int(key),)
            print(f"Mensaje desencriptado: {msgDesencrypt}\n{endl}")
            Lcodificaciones.append([action, msg, str(key), [0, msgDesencrypt]])
        print(endl)
        return _recursive_secretanya()
    
    def _transcriptor(L):
        grabar = input("¿Quieres guardar registro de lo escrito humanx? (y/n)\n").lower()
        if grabar in ["si", 's', "yes",'y']:
            file = input("Nombre del archivo: ")
            file = open(file + ".txt", 'w', encoding="utf-8")
            file.write(f"Transcripción del diálogo humanx-(de)codificados, se ignoran los intentos de uso fallidos {endl}\n")
            for cod in L:
                file.write(f"Acción: {cod[0]}\nMensaje: {cod[1]}\nLlave: {cod[2]}\n")
                if cod[3][0] == 1:
                    file.write(f"Mensaje encriptado: {cod[3][1]}")
                else:
                    file.write(f"Mensaje desencriptado: {cod[3][1]}")
                file.write(f"\n{endl}\n")
        print("Hasta pronto!\n")

    return _recursive_secretanya()