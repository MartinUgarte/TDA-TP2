import argparse
from fuerzaBruta.fuerza_bruta import empaquetamiento_fb

def leer_archivo(filename):
    arreglo = []
    with open(filename) as archivo:
        n = archivo.readline().rstrip()
        archivo.readline()
        for linea in archivo:
            linea = linea.rstrip()
            arreglo.append(float(linea))
    return arreglo

def obtener_solucion(arreglo, modo):
    if modo == 'E':
        return 'Solución Exacta: ', empaquetamiento_fb(arreglo)
    if modo == 'A':
        return 'Solución Aproximada: ', []
    if modo == 'A2':
        return 'Solución Aproximada Alumnos: ', []

def main():
    parser = argparse.ArgumentParser(description='Programa para procesar datos de entrada')
    parser.add_argument('modo', choices=['E', 'A', 'A2'], help='Tipo de solución')
    parser.add_argument('archivo', type=argparse.FileType('r'), help='Archivo de datos')
    args = parser.parse_args()
    
    archivos = ['../datasets/env3.txt', '../datasets/env10.txt', '../datasets/env10b.txt', '../datasets/env10c.txt', '../datasets/env20.txt', '../datasets/env40.txt', '../datasets/env60.txt']
    for archivo in archivos:
        arreglo = leer_archivo(archivo)
        texto, solucion = obtener_solucion(arreglo, args.modo)
        envases, tiempo = solucion
        print(f'{archivo}: {texto}#{len(envases)}')
        print(tiempo)

main()