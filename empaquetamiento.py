def empaquetamiento(T, index, envase_actual, soluciones, indices_usados):
    if sum(envase_actual) > 1:
        return False
    
    if len(T) == len(indices_usados):
        return True
    
    if sum(envase_actual) == 1:
        soluciones.append(envase_actual[:])
        return True

    for i in range(index, len(T)):
        envase_actual.append(T[i])
        indices_usados.append(i)
        if not empaquetamiento(T, index + 1, envase_actual, soluciones, indices_usados):
            envase_actual.pop()
            indices_usados.pop()
        elif i == len(T) - 1:
            soluciones.append(envase_actual[:])
            empaquetamiento(T, 0, [], soluciones, indices_usados)
    # Empiezo denuevo con otro envase vacio
    return empaquetamiento(T, 0, [], soluciones, indices_usados)

soluciones = []
#T = [0.4, 0.8, 0.5, 0.1, 0.7, 0.6, 0.1, 0.4, 0.2, 0.2]
#T = [0.6, 0.5]
T = [0.2, 0.6]
empaquetamiento(T, 0, [], soluciones, [])
print(soluciones)
