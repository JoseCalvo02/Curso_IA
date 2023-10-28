import matplotlib.pyplot as plt
import networkx as nx

def plot_graph(graph, edge_colors):
    """
    Visualiza el grafo con colores específicos para las aristas.

    Args:
    graph (nx.Graph): Grafo a visualizar.
    edge_colors (dict): Diccionario de colores para las aristas.
    """
    fig = plt.figure()
    pos = nx.circular_layout(graph)  # Posiciona los nodos utilizando un algoritmo de resorte

    nx.draw_networkx_nodes(graph, pos, node_size=700, node_color='skyblue')
    nx.draw_networkx_labels(graph, pos, font_size=12, font_weight='bold')

    for (u, v), color in edge_colors.items():
            labels = {f"Costo: {graph[u][v]['weight']:.2f}"}
            nx.draw_networkx_edges(graph, pos, edgelist=[(u, v)], edge_color=color, width=2, alpha=0.8)
            nx.draw_networkx_edge_labels(graph, pos, edge_labels={(u, v): f"Costo: {graph[u][v]['weight']:.2f}"}, font_size=10, font_color=color)

    plt.title("Grafo con Feromonas y Costos")
    plt.axis("off")
    plt.show(block=False)  # No bloquea la ejecución del código

def plot_results(best_path, best_cost, graph):
    """
    Visualiza la mejor ruta encontrada junto con su costo.

    Args:
    best_path (list): Mejor ruta encontrada.
    best_cost (float): Costo de la mejor ruta.
    graph (nx.Graph): Grafo original.
    """
    fig = plt.figure()
    pos = nx.circular_layout(graph)
    #edge_labels = {(best_path[i], best_path[i + 1]): f"Costo Total: {best_cost:.2f}" for i in range(len(best_path) - 1)}

    # Colorea los nodos inicial y final
    node_colors = ['red' if node == best_path[0] else 'green' if node == best_path[-1] else 'skyblue' for node in graph.nodes]

    nx.draw_networkx_nodes(graph, pos, node_size=700, node_color=node_colors)
    nx.draw_networkx_labels(graph, pos, font_size=12, font_weight='bold')
    nx.draw_networkx_edges(graph, pos, width=1, edge_color='gray', alpha=0.5)  # Aristas del grafo original

    # Dibuja el mejor camino como una línea verde
    nx.draw_networkx_edges(graph, pos, edgelist=best_path_edges(graph, best_path), width=2, edge_color='green')

    # Agrega los costos individuales de las aristas al gráfico
    for u, v in best_path_edges(graph, best_path):
        edge_label = f"Costo: {graph[u][v]['weight']:.2f}"
        nx.draw_networkx_edge_labels(graph, pos, edge_labels={(u, v): edge_label}, font_size=10)

    plt.title("Mejor Ruta Encontrada")
    plt.text(0.5, -0.05, f"Costo Total: {best_cost:.2f}", horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes, color='blue')
    plt.text(0.5, -0.1, "Nodo Rojo = inicio | Nodo Verde = final", horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes)

    plt.axis("off")
    plt.show(block=False)  # No bloquea la ejecución del código
    input("Presiona Enter para finalizar...")

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