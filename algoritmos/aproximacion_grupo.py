import time

def con_alguno_suma(nro, elementos_restantes):
    for i in elementos_restantes:
        if nro + i <= 1:
            return True
    return False

def armar_paquetes(t_aux, soluciones):
    soluciones_parciales = []
    envase_actual = []
    while t_aux:
        envase_actual.append(t_aux.pop(0))

        if sum(envase_actual) > 1:
            t_aux.append(envase_actual.pop())
            
        if sum(envase_actual) == 1:
            soluciones_parciales.append(envase_actual[:])
            envase_actual = []

        elif con_alguno_suma(sum(envase_actual), t_aux):
            continue

        else: 
            soluciones_parciales.append(envase_actual[:])
            envase_actual = []
        
        if len(soluciones_parciales) >= len(soluciones) and len(soluciones) != 0:
            break

    return soluciones_parciales

def empaquetamiento_aproximado_grupo(T):
    start_time = time.time()
    solucion_mejor = []
    if len(T) == 0:
        return T, start_time
    for i in range(len(T)):
        t_aux = T[i:] + T[:i]
        solucion_aux = armar_paquetes(t_aux, solucion_mejor)
        if len(solucion_aux) < len(solucion_mejor) or len(solucion_mejor) == 0:
            solucion_mejor = solucion_aux[:]
    end_time = time.time()
    return solucion_mejor, end_time - start_time