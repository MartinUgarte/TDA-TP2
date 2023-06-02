import time

def con_alguno_suma(nro, lista):
    for i in lista:
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

def empaquetamiento_fb(T):
    start_time = time.time()
    soluciones = []
    
    T = sorted(T, reverse=True)

    for i in range(len(T)):

        t_aux = T[i:] + T[:i]

        soluciones_parciales = armar_paquetes(t_aux, soluciones)
       
        if len(soluciones_parciales) < len(soluciones) or len(soluciones) == 0:
            soluciones = soluciones_parciales[:]

        t_aux = T[i:] + T[:i]
        
        elem = t_aux.pop(i)

        soluciones_parciales = armar_paquetes(t_aux, soluciones)
        
        dentro = False
        for i in range(len(soluciones)):
            if sum(soluciones[i] ) < 1 and sum(soluciones[i]) + elem <= 1:
                soluciones[i].append(elem)
                dentro = True
                break
        if not dentro:
            soluciones.append([elem])

        if len(soluciones_parciales) < len(soluciones) or len(soluciones) == 0:
            soluciones = soluciones_parciales[:]
    
    end_time = time.time()
    return soluciones, end_time - start_time


T = [0.02,0.03,0.135,0.758,0.011,0.05,0.077,0.683,0.939,0.038,0.165,0.224,0.152,0.918,0.049,0.485,0.551,0.79,0.69,0.21,0.097,0.345,0.655,0.962,0.291,0.449,0.164,0.023,0.039]
# T = [0.085, 0.006, 0.008, 0.024, 0.106, 0.357, 0.001, 0.915, 0.643, 0.255, 0.513, 0.039, 0.048]
print(empaquetamiento_fb(T))
print(len(empaquetamiento_fb(T)[0]))
