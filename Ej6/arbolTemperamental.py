from arbol import *



# ---------------------------------
# AB's temperamentales de ejemplo

ABT1 = AB(50, 
          AB(16, AB(15, arbolVacio, arbolVacio), 
                 AB(5,  arbolVacio, arbolVacio)),
          AB(40, AB(20, arbolVacio, arbolVacio), 
                 AB(39, arbolVacio, arbolVacio)))

ABT2 = AB(88, 
          AB(50, AB(45, arbolVacio, arbolVacio), 
                 arbolVacio),
          AB(44, AB(33, arbolVacio, arbolVacio), 
                 arbolVacio))

# ---------------------------------
# AB no temperamental de ejemplo

AB3 = AB(50, 
          AB(5, AB(15, arbolVacio, arbolVacio), 
                 AB(4,  arbolVacio, arbolVacio)),
          AB(40, AB(20, arbolVacio, arbolVacio), 
                 AB(88, arbolVacio, arbolVacio)))




