def empaquetamiento(T, index, envase_actual, soluciones, indices_usados):
    if sum(envase_actual) > 1:
        envase_actual.pop()
        indices_usados.pop()
        return False
    
    if len(T) == len(indices_usados) or sum(envase_actual) == 1:
        return True
    
    for i in range(index, len(T)):
        if i in indices_usados: continue
        envase_actual.append(T[i])
        indices_usados.append(i)
        
        if empaquetamiento(T, index + 1, envase_actual, soluciones, indices_usados):
            soluciones.append(envase_actual[:])
            envase_actual = []

        if sum(envase_actual) < 1 and index == len(T) - 1:
            soluciones.append(envase_actual[:])
            envase_actual = []

        if sum(envase_actual) < 1 and i == len(T) - 1:
            if envase_actual:
                envase_actual.pop()
                indices_usados.pop()
            empaquetamiento(T, 0, envase_actual, soluciones, indices_usados)
        
    return False

soluciones = []
#T = [0.4, 0.8, 0.5, 0.1, 0.7, 0.6, 0.1, 0.4, 0.2, 0.2]
T = [0.5, 0.4, 0.6]
empaquetamiento(T, 0, [], soluciones, [])
print(soluciones)
