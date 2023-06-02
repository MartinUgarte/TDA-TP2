import time

def con_alguno_suma(nro, lista):
    for i in lista:
        if nro + i <= 1:
            return True
    return False

def empaquetamiento_fb(T):
    start_time = time.time()
    soluciones = []
    envase_actual = []

    t_aux = T[:]
    while t_aux:
        envase_actual.append(t_aux.pop(0))

        if sum(envase_actual) > 1:
            t_aux.append(envase_actual.pop())
            
        if sum(envase_actual) == 1:
            soluciones.append(envase_actual[:])
            envase_actual = []

        elif con_alguno_suma(sum(envase_actual), t_aux):
            continue

        else: 
            soluciones.append(envase_actual[:])
            envase_actual = []
    end_time = time.time()
    return soluciones, end_time - start_time


