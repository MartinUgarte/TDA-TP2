Vertex Cover:

A partir de un grafo donde cada arista representa un objeto y cada vértice un posible envase, recorremos todas las aristas para generar el arreglo T de n elementos, con la restricción de que la sumatoria de las aristas de un nodo no puede ser mayor a uno.

A partir del arreglo T formado con los pesos de las aristas, se aplica el algoritmo de backtracking para el empaquetamiento y se consiguen la minima cantidad de envases de a lo sumo valor 1. Cada envase va a representar un vertice, y entre todos los envases se tienen guardadas todas las aristas. 

Para encontrar los vertices solucion, hay que iterar los vertices del grafo, y ver cual aplica a cada envase. 

Poner ejemplo