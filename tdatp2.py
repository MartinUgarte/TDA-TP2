import argparse
from algoritmos.fuerza_bruta import empaquetamiento_fb
from algoritmos.aproximacion_curso import empaquetamiento_aproximado_curso
from algoritmos.aproximacion_grupo import empaquetamiento_aproximado_grupo

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
        return 'Solución Aproximada: ', empaquetamiento_aproximado_curso
    if modo == 'A2':
        return 'Solución Aproximada Alumnos: ', empaquetamiento_aproximado_grupo

def main():
    parser = argparse.ArgumentParser(description='Programa para procesar datos de entrada')
    parser.add_argument('modo', choices=['E', 'A', 'A2'], help='Tipo de solución')
    parser.add_argument('archivo', type=argparse.FileType('r'), help='Archivo de datos')
    args = parser.parse_args()
    arreglo = leer_archivo(args.archivo.name)
    texto, solucion = obtener_solucion(arreglo, args.modo)
    print(f"{texto}{solucion}")

main()