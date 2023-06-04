"""
1. Se abre el primer envase y se empaqueta el primer objeto
2. Por cada uno de los objetos restantes se prueba si cabe en el envase actual que está abierto
    - Si es así, se lo agrega a dicho envase y se sigue con el siguiente objeto
    - Si no entra, se cierra el envase actual, se abre uno nuevo que pasa a ser el envase actual,
      se empaqueta el objeto y se prosigue con el siguiente

Este algoritmo sirve como una aproximación para resolver el problema de empaquetamiento.
"""

import time

def empaquetamiento_aproximado_curso(T):
    start_time = time.time()
    solucion = []
    if len(T) == 0: return solucion, start_time
    envase_actual = [T[0]]
    agregado = False

    for i in range(1, len(T)):
        agregado = False
        if sum(envase_actual) + T[i] <= 1:
            envase_actual.append(T[i])
        else:
            solucion.append(envase_actual)
            envase_actual = [T[i]]
            if not i == len(T) - 1:
                agregado = True

    if not agregado:
        solucion.append(envase_actual)
    end_time = time.time()

    return solucion, end_time - start_time
