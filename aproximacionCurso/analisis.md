# Análisis de la solución aproximada

En el siguiente documento se analizará el algoritmo de aproximación propuesto por el curso.

## Análisis de complejidad

La complejidad del algoritmo propuesto es $O(n)$ ya que básicamente se recorre todo el arreglo de objetos una vez, y en cada iteración se realizan consultas de tiempo constante para chequear si el elemento actual entra o no en el envase acumulado hasta el momento.

## Análisis de la aproximación

Sea $I$ una instancia cualquiera del problema de empaquetamiento, y $z(I)$ una solución óptima para dicha instancia, y sea $A(I)$ la solución aproximada.

Se define $\frac{A(I)}{z(I)}\leq r(A)$ para todas las instancias posibles. Para calcular la cota $r(A)$, se necesita demostrar que esta ecuación siempre se cumple.

Suponiendo que hay un solo objeto en la instancia $I$, por ejemplo $T=[0.1]$, el algoritmo aproximado y el que brinda la solución óptima coincidirán ya que la única forma es empaquetarlo en un solo envase. De esta forma, $A(I) = z(I)$ y el cociente entre estos es 1, satisfaciendo la ecuación.

Si hay más de un objeto en $I$, podemos considerar que el algoritmo aproximado calculó $A(I)$ envases y el óptimo $z(I)$ envases.
* Si $A(I) < z(I)$, el algoritmo aproximado estaría encontrando una solución mejor que la óptima, lo cual no es lo deseado. En consecuencia, $r(A)$ debe ser mayor o igual que 1.

