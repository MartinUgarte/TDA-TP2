import argparse
from algoritmos.solucion_optima import empaquetamiento_optimo
from algoritmos.aproximacion_curso import empaquetamiento_aproximado_curso
from algoritmos.aproximacion_grupo import empaquetamiento_aproximado_grupo
from archivos import leer_archivo

def obtener_solucion(arreglo, modo):
    if modo == 'E':
        return 'Solución Exacta: ', empaquetamiento_optimo(arreglo)
    if modo == 'A':
        return 'Solución Aproximada: ', empaquetamiento_aproximado_curso(arreglo)
    if modo == 'A2':
        return 'Solución Aproximada Alumnos: ', empaquetamiento_aproximado_grupo(arreglo)

def main():
    parser = argparse.ArgumentParser(description='Programa para procesar datos de entrada')
    parser.add_argument('modo', choices=['E', 'A', 'A2'], help='Tipo de solución')
    parser.add_argument('archivo', type=argparse.FileType('r'), help='Archivo de datos')
    args = parser.parse_args()
    arreglo, _ = leer_archivo(args.archivo.name)
    texto, solucion = obtener_solucion(arreglo, args.modo)
    print(f"{texto}{len(solucion[0])} {solucion[1]}")
    

main()