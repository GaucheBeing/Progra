# Entradas-Salida; promedioNotas: num num num -> num
# Funcionalidad: calcula el promedio simple entre las variables de entrada
# Ejemplo de uso: promedioNotas(5,4,3) devuelve 4
def promedioNotas(C1, C2, C3):
    sumaNotas = C1+C2+C3
    cantidadNotas = 3
    promedioSimple = sumaNotas / cantidadNotas
    return promedioSimple 

# Testing:
assert promedioNotas(5,4,3) == 4

###### Preguntas ######
# ¿Qué habría que considerar/modificar si se quisiera calcular la media de 4 notas?
# Una solución teniendo en cuenta las herramientas que tenemos por el momento sería aumentar el número de parámetros a 4, sumarlas y
# luego dividirlas por la nueva cantidad de notas (4). 
# Otra forma sería crear una función sin variables tal que pida las notas hasta que se escriba una palabra clave y se detenga, 
# estas se suman y de ahí cuenta la cantidad de valores aportados para hacer el cociente con la suma