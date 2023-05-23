
def encapsulamiento(productos):
    indices_usados = set()
    solucion = []
    paquete = []
    return _encapsulamiento(productos, paquete, solucion, 0, indices_usados)

def _encapsulamiento(productos, paquete, solucion, i, indices_usados):
    if len(indices_usados) == len(productos):
        return solucion
    
    if i >= len(productos):
        return _encapsulamiento(productos, paquete, solucion, 0, indices_usados)
    
    if i in indices_usados:
        return _encapsulamiento(productos, paquete, solucion, i+1, indices_usados)
    
    paquete.append(productos[i])

    if sum(paquete) > 1:
        paquete.pop()
        return _encapsulamiento(productos, paquete, solucion, i+1, indices_usados)
    
    indices_usados.add(i)

    if sum(paquete) == 1:
        solucion.append(paquete)
        paquete = []
        return _encapsulamiento(productos, paquete, solucion, i+1, indices_usados)
    
    if sum(paquete) < 1 and i == len(productos) - 1 :
        paquete.pop()
        indices_usados.remove(i)
        return _encapsulamiento(productos, paquete, solucion, 0, indices_usados)
    
    return _encapsulamiento(productos, paquete, solucion, i+1, indices_usados)

T = [0.4, 0.8, 0.5, 0.1, 0.7, 0.6, 0.1, 0.4, 0.2, 0.2]

print(encapsulamiento(T))

