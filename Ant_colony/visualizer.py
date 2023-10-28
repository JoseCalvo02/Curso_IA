import matplotlib.pyplot as plt
import networkx as nx

def plot_graph(graph, edge_colors):
    """
    Visualiza el grafo con colores específicos para las aristas.

    Args:
    graph (nx.Graph): Grafo a visualizar.
    edge_colors (dict): Diccionario de colores para las aristas.
    """
    pos = nx.circular_layout(graph)  # Posiciona los nodos utilizando un algoritmo de resorte

    nx.draw_networkx_nodes(graph, pos, node_size=700, node_color='skyblue')
    nx.draw_networkx_labels(graph, pos, font_size=12, font_weight='bold')

    for (u, v), color in edge_colors.items():
            labels = {f"Costo: {graph[u][v]['weight']:.2f}"}
            nx.draw_networkx_edges(graph, pos, edgelist=[(u, v)], edge_color=color, width=2, alpha=0.8)
            nx.draw_networkx_edge_labels(graph, pos, edge_labels={(u, v): f"Costo: {graph[u][v]['weight']:.2f}"}, font_size=10, font_color=color)

    plt.title("Grafo con Feromonas y Costos")
    plt.axis("off")
    plt.show()

def plot_results(best_path, best_cost, graph):
    """
    Visualiza la mejor ruta encontrada junto con su costo.

    Args:
    best_path (list): Mejor ruta encontrada.
    best_cost (float): Costo de la mejor ruta.
    graph (nx.Graph): Grafo original.
    """
    pos = nx.circular_layout(graph)
    edge_labels = {(best_path[i], best_path[i + 1]): f"Costo Total: {best_cost:.2f}" for i in range(len(best_path) - 1)}

    nx.draw_networkx_nodes(graph, pos, node_size=700, node_color='skyblue')
    nx.draw_networkx_labels(graph, pos, font_size=12, font_weight='bold')
    nx.draw_networkx_edges(graph, pos, width=1, edge_color='gray', alpha=0.5)  # Aristas del grafo original

    # Dibuja el mejor camino como una línea verde
    nx.draw_networkx_edges(graph, pos, edgelist=best_path_edges(graph, best_path), width=2, edge_color='green')

    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_size=10)

    plt.title("Mejor Ruta Encontrada")
    plt.axis("off")
    plt.show()

def best_path_edges(graph, best_path):
    """
    Genera las aristas correspondientes al mejor camino.

    Args:
    graph (nx.Graph): Grafo original.
    best_path (list): Mejor ruta encontrada.

    Returns:
    list: Lista de aristas correspondientes al mejor camino.
    """
    return [(best_path[i], best_path[i + 1]) for i in range(len(best_path) - 1)]