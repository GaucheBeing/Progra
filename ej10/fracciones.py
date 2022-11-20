from math import gcd

# campos
# numerador: int
# denominador: int
class Fraccion:

    # Constructor
    # Notas que es posible definir valores por omision
    # en caso de que no se especifiquen al momento de crear el objeto
    def __init__(self, numerador = 0, denominador = 1):
        assert denominador != 0,            "Denominador debe ser distinto de cero"
        # Inicializar campos

        self.__numerador = numerador
        self.__denominador = denominador


    # getters y setters
    # consideramos que solo hay que tener getters

    # getNumerador: None -> int
    # entrega el valor del campo numerador
    def getNumerador(self):
        return self.__numerador

    # getDenominador: None -> int
    # entrega el valor del campo denominador
    def getDenominador(self):
        return self.__denominador


    # toString: None -> str
    # muestra la representación como str de la fracción
    def toString(self):
        return str(self.__numerador) + "/" + str(self.__denominador)


    # suma: Fraccion -> Fraccion
    # crea una nueva fracción a partir de sumar esta fracción con otra
    def suma(self,f):
        nuevoNum = self.__numerador * f.__denominador +\
                   f.__numerador * self.__denominador
        nuevoDen = self.__denominador * f.__denominador

        return Fraccion(nuevoNum, nuevoDen)

    # simplificar: None -> None
    # efecto: simplifica la fracción, editando sus campos
    def simplificar(self):
        valor = gcd(self.__numerador, self.__denominador)

        if valor > 1:
            self.__numerador = self.__numerador // valor
            self.__denominador = self.__denominador // valor

    # --- operadores sobrecargados ---

    # operador +: Fraccion + Fraccion -> Fraccion
    def __add__(self,f):
        nuevoNum = self.__numerador * f.__denominador +\
                   f.__numerador * self.__denominador
        nuevoDen = self.__denominador * f.__denominador

        return Fraccion(nuevoNum, nuevoDen)
    
    # funcion str: Fraccion -> str
    def __str__(self):
        return str(self.__numerador) + "/" + str(self.__denominador)

    # representación "natural": Fraccion -> str
    def __repr__(self):
        return self.__str__()


    # --- metodos a implementar en ejercicio 10 ---


    # multiplicar: Fraccion -> Fraccion
    # multiplica dos objetos de tipo Fracción, entregando una nueva Fracción como resultado
    def multiplicar(self, f2):
        # mismo código para __mul__(self, f2)                          
        num_producto = self.__numerador * f2.__numerador
        den_producto = self.__denominador * f2.__denominador
        f_producto = Fraccion(num_producto, den_producto)      
        return f_producto


    # igualdad: Fraccion -> bool
    # Indica si dos objetos Fracción representan el mismo valor numérico/decimal o no, entregando True en tal caso y False si no
    def igualdad(self, f2):        
        # mismo código para __eq__(self, f2)                          
        # forma 1: haciendo uso del divisor común (simplificar las fracciones) y comparar numerador y denominador de ambas fracciones
        f1_prima = Fraccion(self.__numerador, self.__denominador)
        f1_prima.simplificar()
        f2_prima = Fraccion(f2.__numerador, f2.__denominador)
        f2_prima.simplificar()
        return f1_prima.__numerador - f2_prima.__numerador == 0 == f1_prima.__denominador - f2_prima.__denominador
        # también se podrían comparan los strings de cada fracción en lugar de trabajar con números (asumiendo que las fracciones cumplen con ser fracciones como tal)
        # forma 2: calcular el cociente de ambas fracciones y si el valor absoluto de la resta de estos es menor que un epsilon chiquito es porque convergen / son iguales
        # forma 2.1: dados a/b = c/d, si b != 0 y d != 0 se tiene la igualdad si es que el producto cruzado es el mismo, i.e. a*d = b*c -> sad-bc = 0
    

# ---- Fin Clase Fraccion ----

# ---- Testeo ----

f1 = Fraccion(1,2)
f2 = Fraccion(2,4)
f3 = Fraccion(3,4)
f4 = Fraccion(3,6)

# test método multiplicar
assert f1.multiplicar(f1).getNumerador() == 1 and f1.multiplicar(f1).getDenominador() == 4
assert f1.multiplicar(f2).getNumerador() == 2 and f1.multiplicar(f2).getDenominador() == 8
assert f2.multiplicar(f3).getNumerador() == 6 and f2.multiplicar(f3).getDenominador() == 16
assert f3.multiplicar(f4).getNumerador() == 9 and f3.multiplicar(f4).getDenominador() == 24

# test método igualdad
assert f1.igualdad(f2)
assert not f2.igualdad(f3)
assert not f3.igualdad(f4)

# test de inmutación de fracciones
assert f1.getNumerador() == 1 and f1.getDenominador() == 2
assert f2.getNumerador() == 2 and f2.getDenominador() == 4
assert f3.getNumerador() == 3 and f3.getDenominador() == 4
assert f4.getNumerador() == 3 and f4.getDenominador() == 6
