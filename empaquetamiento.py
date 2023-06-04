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


    for i in range(len(T)):

        t_aux = T[i:] + T[:i]

        soluciones_parciales = armar_paquetes(t_aux, soluciones)

        if len(soluciones_parciales) < len(soluciones) or len(soluciones) == 0:
            soluciones = soluciones_parciales[:]

        
        solucion_dos = copiar_lista(soluciones)

        solucion_dos = encontrar_mejor_solucion(solucion_dos)

        if len(solucion_dos) < len(soluciones):
            soluciones = solucion_dos[:]
        
    end_time = time.time()

    # print("Solucion: ", soluciones)

    return soluciones, end_time - start_time


def copiar_lista(soluciones):
    other = []
    for i in range(len(soluciones)):
        other.append(soluciones[i][:])
    return other

def verificar_mejor_solucion(solucion_actual, num_envases, mejor_solucion, num_envases_mejor):
    if num_envases < num_envases_mejor:
        return True
    elif num_envases == num_envases_mejor:
        for envase in solucion_actual:
            if sum(envase) > 1:
                return False
        return True
    else:
        return False
    
def encontrar_mejor_solucion(envases):
    mejor_solucion = envases
    num_envases_mejor = len(envases)
    
    def backtracking(envases_actuales, indice_elemento):
        nonlocal mejor_solucion, num_envases_mejor
        
        if indice_elemento == len(envases_actuales):
            if verificar_mejor_solucion(envases_actuales, len(envases_actuales), mejor_solucion, num_envases_mejor):
                mejor_solucion = envases_actuales.copy()
                num_envases_mejor = len(envases_actuales)
            return
        
        elemento = envases_actuales[indice_elemento]
        
        for i, envase in enumerate(envases_actuales):
            envase.append(elemento)
            backtracking(envases_actuales, indice_elemento + 1)
            envase.pop()
        
        nuevo_envase = [elemento]
        envases_actuales.append(nuevo_envase)
        backtracking(envases_actuales, indice_elemento + 1)
        envases_actuales.pop()
    
    backtracking(envases, 0)
    
    return mejor_solucion 


# indice paquete en el que itero 
# indice elemento que estoy iterando

# indice paquete donde deje el elemento anterior
# elemento anterior
# estoy volviendo para atras

# [0.3, 0.1, 0.2, 0.4] [0.9] [0.5] [0.7] --> og empezando en 0.3
    # [0.1, 0.2, 0.4] [0.9] [0.5, 0.3] [0.7]  --> 0.3
        # [0.2, 0.4] [0.9, 0.1] [0.5, 0.3] [0.7] --> 0.1
            # [0.4] [0.9, 0.1] [0.5, 0.3, 0.2] [0.7] --> 0.2
            # [0.4] [0.9, 0.1] [0.5, 0.3] [0.7, 0.2]
        # [0.2, 0.4] [0.9] [0.5, 0.3, 0.1] [0.7]
            # [0.4] [0.9] [0.5,0.3,0.1] [0.7, 0.2]
        # [0.2, 0.4] [0.9] [0.5, 0.3] [0.7, 0.1]
            # [0.4] [0.9] [0.5, 0.3, 0.2] [0.7, 0.1]
            # [0.4] [0.9] [0.5, 0.3] [0.7, 0.1, 0.2]
    # [0.1, 0.2, 0.4] [0.9] [0.5] [0.7, 0.3]
        # [0.2, 0.4] [0.9, 0.1] [0.5] [0.7, 0.3]
            # [0.4] [0.9, 0.1] [0.5, 0.2] [0.7, 0.3]
        # [0.2, 0.4] [0.9] [0.5, 0.1] [0.7, 0.3]
            # [0.4] [0.9] [0.5, 0.1, 0.2] [0.7, 0.3]
# [0.1, 0.3, 0.2, 0.4] [0.9] [0.5] [0.7]  --> og empezando en 0.1
    # [0.3, 0.2, 0.4] [0.9, 0.1] [0.5] [0.7] --> 0.1



#T = [[0.3, 0.1, 0.2, 0.4], [0.9], [0.5], [0.7]]
# T = [0.02,0.03,0.135,0.758,0.011,0.05,0.077,0.683,0.939,0.038,0.165,0.224,0.152,0.918,0.049,0.485,0.551,0.79,0.69,0.21,0.097,0.345,0.655,0.962,0.291,0.449,0.164,0.023,0.039]
T = [0.085, 0.006, 0.008, 0.024, 0.106, 0.357, 0.001, 0.915, 0.643, 0.255, 0.513, 0.039, 0.048]
# T = [0.401,0.495,0.002,0.958,0.306,0.473,0.149,0.758,0.694,0.022,0.312,0.13,0.042,0.001, 0.164, 0.482, 0.905, 0.044 ,0.073, 0.836, 0.02, 0.242, 0.22, 0.65, 0.095, 0.005, 0.526, 0.995]
empaquetamiento_fb(T)

