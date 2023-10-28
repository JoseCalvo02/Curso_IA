import networkx as nx
from ant_colony import AntColony
from visualizer import plot_graph, plot_results

# Crea un grafo de ejemplo con nodos y aristas
graph = nx.Graph()
graph.add_nodes_from(range(1, 6))
edges = [(1, 2, {'weight': 2}), (2, 3, {'weight': 3}), (3, 4, {'weight': 1}), (4, 5, {'weight': 4}), (5, 1, {'weight': 5})]
graph.add_edges_from(edges)
nx.set_edge_attributes(graph, 1.0, 'pheromone')  # Inicializa todas las aristas con feromona 1.0

# Parámetros del algoritmo
n_ants = 5
n_best = 1
n_iterations = 100
decay = 0.6

# Crea una instancia de AntColony y ejecuta el algoritmo
ant_colony = AntColony(graph, n_ants, n_best, n_iterations, decay)
best_path, best_cost = ant_colony.run()

# Visualiza el grafo con feromonas y la mejor ruta encontrada
plot_graph(graph)
plot_results(best_path, best_cost)