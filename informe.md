# Teoría De Algortimos I

### Alumnos

- Martina Victoria Lozano: 106267
- Martin Ugarte: 107870

**Aclaración**:

$T$ = arreglo original

$n$ = cantidad de elementos del arreglo original.

$r$ = valor de restriccion de un paquete

$k$ = un valor menor a $n$.

$h$ = largo de la solución parcial en la recursividad de backtracking/fuerza bruta.


> 1. Demostrar que el problema de empaquetamiento es NP-Completo.
4

Para reducir Vertex Cover al problema de empaquetamiento, tomamos que cada vértice del gráfico original representa un posible paquete, y cada arista un elemento de ese paquete. Para que las aristas puedan ser consideradas un elemento del paquete, debe asignarseles un peso, y este debe ser igual a 1 que es la restricción de valor de cada paquete. De esta forma, se puede puede formar un arreglo T con todas las aristas, y resolver el problema con el algoritmo de empaquetamiento.

Cada envase obtenido representa uno de los vértices de la solución. Para encontrar los vértices, hace falta recorrer el grafo pesado y determinar qué vértice se corresponde con dicho paquete. Los vértices solución pueden tener aristas en común pero las aristas se incluyen en el arreglo T de forma única, lo cual hay que tener en cuenta al buscar el vértice solución. Si el vértice es solución, pero no coincide con el paquete por $i$ aristas, eso significa que hay i vertices solución que comparten una arista con el vértice.

En el siguiente ejemplo, tenemos un conjunto $T = [0.8, 0.2, 0.4, 0.6]$, donde la solución óptima es $[[0.2, 0.8], [0.4, 0.6]]$. Tras resolver el problema de Vertex Cover, se puede observar que se necesitan dos vértices para cubrir todas las aristas, que coincide con la cantidad mínima de envases necesarias para empaquetar todos los elementos.

# Agregar foto del grafo

El procedimiento sería el siguiente: 

1. Asignarle pesos a las aristas 

    Restricciones:

- $\sum aristas_v\ $ = $r$. Si $\sum aristas_v$ < $r$ se corre el riesgo que el algoritmo de backtracking encuentre una solución con la cantidad correcta de envases, pero las aristas no se correspondan a vértices del grafo. 
            

2. Armar un arreglo T con los pesos de cada arista (puede hacerse al mismo tiempo que 1).

3. Aplicar el algoritmo de backtracking

4. Para recuperar los vértices a partir de los envases hay que tener en cuenta las siguientes situaciones:

- El valor de la arista $a_k$ puede ser igual a la suma de los valores de las aristas $a_i$ y $a_j$.
- Los vértices solución pueden compartir aristas entre sí. Si un envase coincide con un vértice menos $i$ elementos, este vértice es solución si existen $i$ vértices, cada uno con uno de los elementos faltantes.  

Además por ser NP, el problema puede validarse en tiempo polinomial. Simplemente bastaría con recorrer el arreglo de envases y verificar que la suma de sus elementos no exceda 1 y que estén presentes todos los elementos del arreglo original.

> 2. Programar un algoritmo por Backtracking/Fuerza Bruta que busque la solución exacta del problema. Indicar la complejidad del mismo. Realizar mediciones del tiempo de ejecución, y realizar gráficos en función de n. 

Por un lado, nuestro algoritmo comienza utilizando una solución de un algoritmo aproximado como cota, cuya complejidad es $O(n^2 * (n+h))$ (explicada en el punto 4). Luego, pensando a las llamadas recursivas como un árbol el cual comienza teniendo como raíz un solo envase que contiene el primer elemento de T, cada nodo se divide en $h$ + 1 ramas, probando poner el elemento del nivel recursivo correspondiente en cada envase de la solución parcial, y demás probar el caso de agregar a la solución parcial un envase nuevo que únicamente contiene ese elemento. La complejidad por ende sería $O((h+1)^n)$

La complejidad, teniendo en cuenta que las demás operaciones son de tiempo constante, quedará determinada por $O(n^2 * (n+h)) + O((h+1)^n)$, tomando como mayor peso el exponente $n$, entonces la complejidad es $O((h+1)^n)$. 

> 3. Implementar dicho algoritmo, analizar su complejidad, y analizar cuán buena aproximación es. Para esto, considerar lo siguiente: Sea I una instancia cualquiera del problema de empaquetamiento, y z(I) una solución óptima para dicha instancia, y sea A(I) la solución aproximada, se define $\frac{A(I)}{z(I)}\leq r(A)$  para todas las instancias posibles. Calcular r(A) para el algoritmo dado, demostrando que la cota está bien calculada. Realizar mediciones utilizando el algoritmo exacto y la aproximación, con el objetivo de verificar dicha relación.

La complejidad del algoritmo propuesto es O(n) ya que básicamente se recorre todo el arreglo de objetos una vez, y en cada iteración se realizan consultas de tiempo constante para chequear si el elemento actual entra o no en el envase acumulado hasta el momento.

Sea $I$ una instancia cualquiera del problema de empaquetamiento, y $z(I)$ una solución óptima para dicha instancia, y sea $A(I)$ la solución aproximada.

Se define $\frac{A(I)}{z(I)}\leq r(A)$ para todas las instancias posibles. Para calcular la cota $r(A)$, se necesita demostrar que esta ecuación siempre se cumple.

La $\sum a_i\leq z(I)$ con $0\leq i\leq n$, ya que todos los eleentos deben ser puestos en algun envase y cada envase tiene una capacidad maxima de $1$. Entonces necesitamos tanta cantidad de envases igual a la sumatoria de los valores de los elementos.

Si tenemos $A(I)$ envases, sabemos que los $A(I)-1$ van a tener al menos la mitad de la capacidad completa. Esto nos perite expresar $\frac{A(I) -1}{2}<\sum a_i$. 

$\frac{A(I) -1}{2}<\sum a_i\leq z(I)$

$\frac{A(I) -1}{2}\leq z(I)$

$A(I)\leq 2\cdot Z(I)$

$\frac{A(I)}{z(I)}\leq 2 = r(A)$

De esta forma queda demostrado que $r(A)$ es igual a $2$, por lo tanto la aproximacion propuesta se trata de una $2-\text{Aproximacion}$.

> 4. [Opcional] Implementar alguna otra aproximación (u algoritmo greedy) que les parezca de interés. Comparar sus resultados con los dados por la aproximación del punto 3. Indicar y justificar su complejidad.

La función itera todos los elementos del arreglo original en $O(n)$, luego forma arreglos auxiliares y los itera en O(n + k), donde k representa la cantidad de elementos que son reinsertados en el arreglo auxiliar. Cada reinserción aumenta la cantidad de iteraciones restantes. En cada iteración del arreglo auxiliar hace uso de una funcion auxiliar, cuya complejidad es $O(n-1)$.

$O(n^2 * (n+k))$ 