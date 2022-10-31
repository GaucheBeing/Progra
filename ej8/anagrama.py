# joiner: str -> str
# dado un conjunto de carácteres, se entrega otro pero sin espacios ni símbolos especiales
def joiner(S):
    assert type(S) == str
    S = list(S.lower())
    # chequear si el elemento actual de índice i del string es un carácter especial por cada iteración
    # en caso de que tal elemento esté contenido en el conjunto de carácteres especiales se remueve de la lista S y procede hasta revisar S entera
    for i in S[:]:
        if i in [" ", ',', ';', '.', ':', '_', '-', '¿', '?', '¡', '!', '"', "'", '(', ')', '[', ']', '{', '}']:
            S.remove(i)
    return ''.join(S)


# anagrama: str str -> bool
# recibe dos strings, y evalua si son anagramas o no
# ej: 'caso' y 'saco' => True, 'tommarvoloriddle' y 'I am lord Voldemort' => True
def anagrama(S1, S2):
    assert type(S1) == type(S2) == str
    S1 = list(joiner(S1))
    S2 = list(joiner(S2))
    S1.sort()
    S2.sort()
    return S1 == S2
# test
assert anagrama('Happy end of semester...', 'amperes feed pythons')
assert anagrama("there's more?!", "Eh, sore term :( ")
assert not anagrama('moderna peor ramo 1er año?', 'en efecto estimadx')
assert anagrama('tommarvoloriddle', 'I am lord Voldemort')
assert anagrama('caso', 'saco')
