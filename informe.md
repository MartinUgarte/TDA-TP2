# Teoría De Algortimos I

### Alumnos

- Martina Victoria Lozano: 106267
- Martin Ugarte: 107870

### Notaciones

$T$ = arreglo original

$n$ = cantidad de elementos del arreglo original.

$k$ = un valor menor a $n$.

$h$ = largo de la solución parcial en la recursividad del algoritmo de backtracking.

## Ejercicio 1

> Demostrar que el problema de empaquetamiento es NP-Completo.

Para que un algoritmo sea NP-Completo, tiene que poder reducirse otro algoritmo NP-Completo a este.

El `Partition Problem` consiste en determinar si es posible dividir un conjunto $S$ dado de números en dos subconjuntos disjuntos $S_1$ y $S_2$, de manera que la suma de los elementos en ambos subconuntos sea la misma, $\sum S_1 == \sum S_2$. Este problema es NP-Completo, y es el que vamos a reducir a nuestro problema de `Empaquetamiento`. 

Para lograrlo, se puede dividir todos los elementos de tal forma que queden ajustados en el intervalo $(0,1]$.

Los bins en empaquetamiento son de capacidad máxima $1$, entonces debemos reescalar los valores de $S$ tal que cada $s_i\in (0,1]$, y esto lo conseguimos dividiendo los valores por la $\sum S$. Hacer solo la división haría que la suma de los nuevos valores sea $1$ y guardaría todos los elementos en un solo envase, pero queremos ver si entran en dos de ellos cuya suma sea la misma. Por esto multiplicamos cada valor por $2$, asi la suma de todos los valores sería $2$. Esto significa que si pudimos meter todo (la mitad en un bin y la otra en otro) estaría dando $1+1=2$. Como condición entonces se debe cumplir que todos los elementos queden entre $0$ y $1$. De no serlo, entonces el problema de decisión dará False, ya que un elemento estaría ocupando más de la mitad de la suma de todos los elemetos y no habría solución.

$s_i=\frac{2c_i}{\sum_{j=1}^n c_j}$ donde $s_i\in(0,1]$ para $i=1,...,n$.

Un problema es NP si su solución se puede validar en tiempo polinomial. En este caso, validar que la solución es correcta podría hacerse creando una copia de $T$, y recorrer la solución una vez, y por cada elemento visto quitarlo del arreglo copia, si el elemento no se encuentra en la copia la solución no es válida. El arreglo copia debe quedar vacio, y todos los valores de la solución deben haber sido vistos, de no ser asi, la solución es inválida. Si al vaciar el arreglo $T$, quedan elementos sin ver, la solución es inválida. Por supuesto al iterar cada envase, también hay verificar que la suma de los elementos no exceda $1$ en cada uno de ellos.

## Ejercicio 2

> Programar un algoritmo por Backtracking/Fuerza Bruta que busque la solución exacta del problema. Indicar la complejidad del mismo. Realizar mediciones del tiempo de ejecución, y realizar gráficos en función de n. 

Por un lado, nuestro algoritmo comienza utilizando una solución de un algoritmo aproximado como cota, cuya complejidad es $O(\space n^3\space)$ (explicada en el punto $4$). Luego, pensando a las llamadas recursivas como un árbol el cual comienza teniendo como raíz un solo envase que contiene el primer elemento de $T$, cada nodo se divide en $h + 1$ ramas, probando poner el elemento del nivel recursivo correspondiente en cada envase de la solución parcial, y demás probar el caso de agregar a la solución parcial un envase nuevo que únicamente contiene ese elemento. Por ende sería $O((h+1)^n)$.

Hasta el momento tenemos $O(n^3 + (h+1)^n)$. Sin embargo, $h$ no es parámetro del problema, asi que no puede ser tomado en cuenta para formular la complejidad del mismo. La complejidad final, teniendo en cuenta que las demás operaciones son de tiempo constante, y reemplazando $(\space h+1\space)$ por una constante $b$ la cual es acotada por $n$ (ya que en el peor caso todos los elementos quedan separados en distintos envases) quedará determinada por $O(\space b^n\space)$.

A continuación se muestra un gráfico de los tiempos de ejecución (en segundos) en función del tamaño de la entrada. Por cuestiones de tiempo y recursos, se realizaron mediciones con $len(T)\in(5, 10, 15, 20)$ con slices de un mismo arreglo.

![](/graficos/tiempos_ejecucion.png)

Aproximadamente, para un $5$ elementos el algoritmo tarda $50$ microsegundos, para $10$ elementos tarda $0.005$ segundos, para $15$ elementos tarda $5$ segundos, y para $20$ elementos tarda $7$ horas.

## Ejercicio 3

> Implementar el algoritmo, analizar su complejidad, y analizar cuán buena aproximación es. Para esto, considerar lo siguiente: Sea I una instancia cualquiera del problema de empaquetamiento, y z(I) una solución óptima para dicha instancia, y sea A(I) la solución aproximada, se define $\frac{A(I)}{z(I)}\leq r(A)$  para todas las instancias posibles. Calcular r(A) para el algoritmo dado, demostrando que la cota está bien calculada. Realizar mediciones utilizando el algoritmo exacto y la aproximación, con el objetivo de verificar dicha relación.

La complejidad del algoritmo propuesto por el curso es $O(n)$ ya que básicamente se recorre todo el arreglo de objetos una vez, y en cada iteración se realizan consultas de tiempo constante para chequear si el elemento actual entra o no en el envase acumulado hasta el momento.

Sea $I$ una instancia cualquiera del problema de empaquetamiento, y $z(I)$ una solución óptima para dicha instancia, y sea $A(I)$ la solución aproximada.

Se define $\frac{A(I)}{z(I)}\leq r(A)$ para todas las instancias posibles. Para calcular la cota $r(A)$, se necesita demostrar que esta ecuación siempre se cumple.

Por un lado

$$
\begin{gather*}
\sum a_i\leq z(I)
\end{gather*}
$$

con

$$
\begin{gather*}
0\leq i\leq n
\end{gather*}
$$

ya que todos los elementos deben ser puestos en algun envase y cada envase tiene una capacidad máxima de $1$. Entonces necesitamos tanta cantidad de envases igual a la sumatoria de los valores de los elementos.

Si tenemos $A(I)$ envases, sabemos que los $A(I)-1$ van a tener al menos la mitad de la capacidad completa. Esto nos permite expresar:

$$
\begin{gather*}
\frac{A(I) -1}{2}<\sum a_i
\end{gather*}
$$

Finalmente, relacionando estas ecuaciones

$$
\begin{gather*}
\frac{A(I) -1}{2}<\sum a_i\leq z(I)
\end{gather*}
$$

$$
\begin{gather*}
\frac{A(I) -1}{2}\leq z(I)
\end{gather*}
$$

$$
\begin{gather*}
A(I)\leq 2\cdot Z(I)
\end{gather*}
$$

$$
\begin{gather*}
\frac{A(I)}{z(I)}\leq 2
\end{gather*}
$$

De esta forma queda demostrado que $r(A)=2$, por lo tanto la aproximación propuesta se trata de una $2-\text{Aproximación}$.

Para corroborar esta relación, realizamos un gráfico que muestra claramente la tendencia y el crecimiento del resultado.

![](/graficos/punto_3.png)


## Ejercicio 4

> [Opcional] Implementar alguna otra aproximación (u algoritmo greedy) que les parezca de interés. Comparar sus resultados con los dados por la aproximación del punto 3. Indicar y justificar su complejidad.

La función itera todos los elementos del arreglo original en $O(n)$, luego forma arreglos auxiliares y los itera $(n + k)$ veces, donde $k$ representa la cantidad de elementos que son reinsertados en el arreglo auxiliar. Cada reinserción aumenta la cantidad de iteraciones restantes. En cada iteración del arreglo auxiliar hace uso de una funcion auxiliar, cuya complejidad es $O(n-1)$. 

De esta forma, quedaría $O(n^2\cdot (n+k))$. En realidad la complejidad total de esta aproximación es $O(\space n^2 \cdot n\space)=O(n^3)$. Por no ser entrada del algoritmo y siendo $k<n$ (como mucho $k=n-1$) el parámetro $k$ no forma parte de la complejidad.

Para finalizar, se muestran gráficos adicionales para terminar de comparar los tres algoritmos desarrollados y ver como se comportan las aproximaciones contra la solución óptima.

Utilizando el mismo arreglo del ejercicio $2$:

![](/graficos/cantidad_envases.png)

Utilizando distintos datasets brindados por la cátedra, incluyendo nuevos datasets construidos a partir de la unión de alguno de ellos:

![](/graficos/tiempos_aprox.png)

![](/graficos/envases_aprox.png)