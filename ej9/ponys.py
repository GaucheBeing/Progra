# listaPony: str str -> list | None
# Dado el nombre de un archivo y una letra, entrega una lista con todos los nombres que empiecen por la letra dada.
# Agregado: en caso de inexistencia se muestra en la consola de la persona usuarix el mensaje indicando esto
# Ej: 
def listaPony(archN, letra):
    assert type(archN) == type(letra) == str
    # Sólo para este caso particular podemos obligar a que la letra/palabra u oración/set de palabras
    # dada por la persona usuarix parta(n) con mayúscula(s) y el resto de la(s) palabra(s) en minúsculas 
    if not letra.istitle():
        modificar = input("Los carácteres ingresados no se encuentran en formato 'Nombre'. ¿Quieres modificación automática? [y/n]: ")
        if modificar in ["yes", 'y', "si", 's']:
            print()
            letra = letra.title()

    arch = open(f"{archN}.txt", 'r')
    Lline = []
    for line in arch:
        line = line.strip()
        if letra in line[0 : len(letra)]:
            Lline.append(line)
    arch.close()
    ##### Agregado #####
    if Lline == []:
        if len(letra) == 1:
            print("No hay nombre con esa letra")
            return None
        elif len(letra) != 1 and ' ' in letra:
            print("No hay nombre que parta con ese set de carácteres")
            return None
        else: 
            print("No hay nombre que parta con esa palabra")
            return None
    Lline.sort()
    return Lline
# Test con listas ordenadas y asumiendo que ponys.txt está en el mismo directorio:
assert listaPony("ponys", 'Z') == sorted(['Zapp', 'Zephyr Breeze', 'Zesty Gourmand', 'Zipporwhill', 'Zirconic'])
assert listaPony("ponys", "Welch") == ["Welch / Cloudy Haze"]
assert listaPony("ponys", "Aunt") == sorted(['Aunt Orange', 'Auntie Applesauce', 'Aunt Pine Apple', 'Aunt Bae Mare'])
