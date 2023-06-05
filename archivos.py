def leer_archivo(filename):
    arreglo = []
    with open(filename) as archivo:
        n = archivo.readline().rstrip()
        archivo.readline()
        for linea in archivo:
            linea = linea.rstrip()
            arreglo.append(float(linea))
    return arreglo, n