import time
from aproximacion_grupo.aproximacion_grupo import empaquetamiento_aproximado_grupo

def copiar_lista(lista):
    nueva_lista = []
    for i in lista:
        nueva_lista.append(i[:])
    return nueva_lista

def _empaquetamiento_optimo(T, solucion_mejor, solucion_parcial, i):   
    if i == len(T) and len(solucion_parcial) < len(solucion_mejor):
        solucion_mejor = copiar_lista(solucion_parcial)
    
    if i == len(T):
        return solucion_mejor
    
    if len(solucion_parcial) > len(solucion_mejor):
        return solucion_mejor
    
    for envase in solucion_parcial:
        nueva_solucion = copiar_lista(solucion_parcial)
        nuevo_envase = envase[:]
        nueva_solucion.remove(envase)
        nueva_solucion.append(nuevo_envase)
        nuevo_envase.append(T[i]) 
        
        if sum(nuevo_envase) > 1 or len(nueva_solucion) > len(solucion_mejor):
            continue
        
        solucion_mejor = _empaquetamiento_optimo(T, solucion_mejor, nueva_solucion, i+1)

    nueva_solucion = copiar_lista(solucion_parcial)
    nueva_solucion.append([T[i]])
    return _empaquetamiento_optimo(T, solucion_mejor, nueva_solucion, i+1)

def empaquetamiento_optimo(T):
    start_time = time.time()
 
    if len(T) == 0:
        return T, start_time
    
    solucion_cota = empaquetamiento_aproximado_grupo(T)[0]
    solucion_mejor = _empaquetamiento_optimo(T, solucion_cota, [[T[0]]], 1)

    end_time = time.time()

    return solucion_mejor, end_time - start_time