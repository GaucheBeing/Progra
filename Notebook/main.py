def main():
    ARCHIVO_SOSPECHOSOS = open('DOMICILIARIO.txt', 'r', encoding="utf8")
    ARCHIVO_LOGS = open('LOGS.txt', 'r', encoding="utf8")
    SALIDA = open('SALIDA.txt', 'w', encoding="utf8")
    
    # Crear lista de listas de sospechosos con sus características
    Lsospechosos = []
    for line in ARCHIVO_SOSPECHOSOS:
        line = line.split(',')
        Lsospechosos.append(line)

    # Crear lista de listas de registros dividida por categorías
    Llogs = []
    for line in ARCHIVO_LOGS:
        line = line.split(',')
        Llogs.append(line)

    # Hacer diccionario que mapea los teléfonos con los registros (en particular las antenas asociadas a dicho número) de Llogs
    Dtelefonos = {}
    for registro in Llogs:
        telefono = registro[2]
        # Si el número/llave se encuentra en el diccionario, su antena asociada se le agrega a la lista de antenas
        if telefono in Dtelefonos:
            Dtelefonos[telefono].append(registro[0])
        # Si el número/llave no existe, se crea y se le asocia de elemento la antena
        else:
            Dtelefonos[telefono] = [registro[0]]

    Lincumplidores = []
    for sospechoso in Lsospechosos:
        telefono = sospechoso[2]
        # Revisar si el número de un sospechoso se encuentra en el registro de teléfonos
        if telefono in Dtelefonos:
            # Eliminar antenas duplicadas
            antenas_unicas = []
            for antena in Dtelefonos[telefono]:
                if antena not in antenas_unicas:
                    antenas_unicas.append(antena)
            # Guardar el nombre del criminal, el delito (sin salto de línea), número y lista de antenas 
            incumplidor = [sospechoso[0], sospechoso[3].strip(), telefono, ','.join(antenas_unicas)]
            Lincumplidores.append(incumplidor)

    # Ordenar la lista de listas alfabéticamente por el nombre del criminal
    # Cabe destacar que no es necesario pues el archivo DOMICILIARIO ya está ordenada
    # Lincumplidores.sort(key=lambda incumplidor: incumplidor[0])

    # En caso de que no haya registro (i.e la lista de incumplidores está vacía) escribir que no existen registros
    if Lincumplidores == []:
        SALIDA.write("No es posible escribir `SALIDA.txt` debido a que no existen registros para escribir")
    # Caso contrario escribir los datos de los criminales que incumplieron el arresto domiciliario
    else:
        for i in range(len(Lincumplidores)-1):
            SALIDA.write(f"{','.join(Lincumplidores[i])}\n")
        # Aseguramos que la última línea no esté vacía a causa de \n
        SALIDA.write(','.join(Lincumplidores[-1]))
main()