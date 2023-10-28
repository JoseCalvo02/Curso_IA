import random
import networkx as nx
from ant_colony import AntColony
from visualizer import plot_graph, plot_results

# Número de nodos en el grafo
num_nodos = 5

# Crea un grafo de ejemplo con nodos y aristas
graph = nx.Graph()
graph.add_nodes_from(range(1, num_nodos + 1))

# Función para generar aristas aleatorias con pesos entre 1 y 10
def generar_aristas(num_nodos):
    return [(i, j, {'weight': random.randint(1, 10)}) for i in range(1, num_nodos + 1) for j in range(i + 1, num_nodos + 1)]

# Agrega aristas aleatorias al grafo con pesos entre 1 y 10
edges = generar_aristas(num_nodos)
graph.add_edges_from(edges)
nx.set_edge_attributes(graph, 1.0, 'pheromone')  # Inicializa todas las aristas con feromona 1.0

# Define colores para las aristas basándose en los nodos de origen
colores_aristas = {(i, j): 'red' if i == 1 else 'blue' if i == 2 else 'green' for i, j, attrs in edges}

# Parámetros del algoritmo
n_ants = 5
n_best = 1
n_iterations = 100
decay = 0.6

# Crea una instancia de AntColony y ejecuta el algoritmo
ant_colony = AntColony(graph, n_ants, n_best, n_iterations, decay)
best_path, best_cost = ant_colony.run()

# Visualiza el grafo con feromonas y la mejor ruta encontrada
plot_graph(graph, edge_colors=colores_aristas)
plot_results(best_path, best_cost, graph)