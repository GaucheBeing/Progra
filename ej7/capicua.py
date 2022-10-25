# capicua: str -> bool
# función: dada una palabra o frase evaluar si es capicúa o no
# Ej: 'Lol' => True y 'Pochita' => False
def capicua(S):
    assert type(S) == str
    # mutar el parámetro dado de manera tal que
    # 1. separamos las palabras que tengan espacios entremedio y eliminar estos últimos
    # 2. concatenamos los elementos de la lista generada por split() reduciendola lista a un string
    # 3. usamos el método para strings lower() para que todo esté en minúsculas
    # 4. creamos una lista nuevamente donde cada elemento sea un carácter del string obtenido tras paso 3
    S = list(''.join(S.split()).lower())
    # chequear si el elemento actual de índice i del string es un carácter especial por cada iteración
    # en caso de que tal elemento esté contenido en el conjunto de carácteres especiales se remueve de la lista S y procede hasta revisar S entera
    for i in S[:]:
        if i in [',', ';', '.', ':', '_', '-', '¿', '?', '¡', '!', '"', "'"]:
            S.remove(i)
    # slice-amos S partiendo desde el final hasta llegar al 1er elemento de S tal que obtenemos la lista invertida 
    # donde el elemento de índice i de la lista original está en la posición len(S)-i, con i natural tal que 0 <= i <= len(S)
    invertS = list(S[len(S) : : -1])
    if S == invertS:
        return True
    else: return False
# test
assert capicua('Lol')
assert capicua('anita lava la tina')
assert not capicua('Pochita')