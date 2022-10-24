# capicua: str -> bool
# función: dada una palabra o frase evaluar si es capicúa o no
# Ej: 'ala' => True y 'hola' => False
def capicua(S):
    assert type(S) == str
    S = list(''.join(S.split()))
    invertS = list(S[::-1])
    if S == invertS:
        return 1
    else: 0
# test
#assert capicua('ala')
#assert capicua('anita lava la tina')
#assert not capicua('hola')
