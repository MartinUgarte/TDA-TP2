import time

def con_alguno_suma(nro, lista):
    for i in lista:
        if nro + i <= 1:
            return True
    return False


def empaquetamiento_fb(T):
    start_time = time.time()
    soluciones = []
    soluciones_parciales = []
    envase_actual = []
    
    for i in range(len(T)):
        soluciones_parciales = []
        envase_actual = []
        t_aux = T[i:] + T[:i]
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

        if len(soluciones_parciales) < len(soluciones) or len(soluciones) == 0:
            soluciones = soluciones_parciales[:]

    end_time = time.time()
    return soluciones, end_time - start_time



