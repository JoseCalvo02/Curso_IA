# Problema del Viajante de Comercio con Colonia de Hormigas

Este proyecto implementa el Algoritmo de Colonia de Hormigas (ACO) para resolver el Problema del Viajante de Comercio (TSP).

## Cómo Usar el Código

1. **Instalación de Dependencias**: Antes de ejecutar el código, utilizar el archivo `requirements.txt` para instalar las dependencias:

   # Instala las dependencias desde el archivo requirements.txt
   pip install -r requirements.txt

## Cómo Funciona el Algoritmo

**Problema del Viajante de Comercio con Colonia de Hormigas**:
    Este proyecto resuelve el Problema del Viajante de Comercio (TSP) utilizando el Algoritmo de Colonia de Hormigas (ACO). El TSP implica encontrar la ruta más corta que visita todos los nodos en un grafo exactamente una vez. La solución encontrada por el ACO es una aproximación a la solución óptima del TSP.

**Algoritmo de Colonia de Hormigas (ACO)**:
    El ACO es una técnica heurística basada en el comportamiento de las hormigas reales. Las hormigas construyen rutas aleatorias y luego depositan feromonas en las aristas que recorren. Otras hormigas prefieren seguir las rutas con feromonas más fuertes, lo que guía al algoritmo hacia una solución que representa una ruta corta que visita todos los nodos.

    En el algoritmo de la colonia de hormigas, la feromona en las aristas se utiliza como una forma de comunicación entre las hormigas. Cuando una hormiga encuentra una solución (es decir, una ruta completa), deposita feromona en las aristas que forman esa ruta. Las otras hormigas, al elegir su camino, tienden a seguir las aristas con una mayor concentración de feromona, ya que esto indica que esa ruta ha sido elegida por otras hormigas y podría conducir a una solución.

    Sin embargo, para evitar que el algoritmo se quede atrapado en una solución subóptima y para permitir la exploración de nuevas rutas, la feromona en las aristas se somete a un proceso de evaporación. Esto significa que con el tiempo, la feromona en las aristas disminuye gradualmente. Al disminuir la feromona con el tiempo, se reduce la influencia de las rutas encontradas previamente, lo que permite a las hormigas explorar nuevas rutas y encontrar soluciones potencialmente mejores.

## Cómo Funciona el Código (archivos)

ant_colony.py: Contiene la implementación del algoritmo ACO en la clase AntColony. Aquí se generan soluciones candidatas, se ejecutan las hormigas para construir rutas y se actualizan las feromonas en las aristas del grafo.

visualizer.py: Proporciona funciones para visualizar el grafo y los resultados. plot_graph muestra el grafo con feromonas y asigna colores a las aristas según su origen. plot_results muestra la mejor ruta encontrada con el costo asociado.

main.py: Aquí se crea el grafo del problema, se configuran los parámetros del algoritmo (número de hormigas, número de iteraciones, tasa de evaporación, etc.) y se ejecuta el algoritmo ACO.