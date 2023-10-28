import matplotlib.pyplot as plt
import networkx as nx

def plot_graph(graph):
    """
    Visualiza el grafo con el grosor de las aristas basado en la feromona depositada.

    Args:
    graph (nx.Graph): Grafo a visualizar.
    """
    pos = nx.spring_layout(graph, seed=42)  # Posiciona los nodos utilizando un algoritmo de resorte
    edge_labels = {(u, v): f"Feromona: {attrs['pheromone']:.2f}" for u, v, attrs in graph.edges(data=True)}
    edge_widths = [attrs['pheromone'] for _, _, attrs in graph.edges(data=True)]

    nx.draw_networkx_nodes(graph, pos, node_size=700, node_color='skyblue')
    nx.draw_networkx_labels(graph, pos, font_size=12, font_weight='bold')
    nx.draw_networkx_edges(graph, pos, width=edge_widths, edge_color='gray', alpha=0.5)
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_size=10)

    plt.title("Grafo con Feromonas")
    plt.axis("off")
    plt.show()


def plot_results(best_path, best_cost):
    """
    Visualiza la mejor ruta encontrada junto con su costo.

    Args:
    best_path (list): Mejor ruta encontrada.
    best_cost (float): Costo de la mejor ruta.
    """
    edges = [(best_path[i], best_path[i + 1]) for i in range(len(best_path) - 1)]
    best_path_graph = nx.Graph(edges)

    pos = nx.spring_layout(best_path_graph, seed=42)
    edge_labels = {(best_path[i], best_path[i + 1]): f"Costo: {best_cost:.2f}" for i in range(len(best_path) - 1)}

    nx.draw_networkx_nodes(best_path_graph, pos, node_size=700, node_color='skyblue')
    nx.draw_networkx_labels(best_path_graph, pos, font_size=12, font_weight='bold')
    nx.draw_networkx_edges(best_path_graph, pos, width=2, edge_color='green', alpha=0.8)
    nx.draw_networkx_edge_labels(best_path_graph, pos, edge_labels=edge_labels, font_size=10)

    plt.title("Mejor Ruta Encontrada")
    plt.axis("off")
    plt.show()