from grid_printer import print_grid_with_path
from get_neighbors import get_neighbors
import heapq

# Definición de la clase Node para representar los nodos en el espacio de búsqueda
class Node:
    def __init__(self, state, parent=None, action=None, cost=0, heuristic=0):
        self.state = state  # Estado del nodo en la cuadrícula
        self.parent = parent  # Nodo padre en el árbol de búsqueda
        self.action = action  # Acción que llevó al nodo actual desde el nodo padre
        self.cost = cost  # Costo acumulado para llegar a este nodo desde el nodo inicial
        self.heuristic = heuristic  # Valor heurístico estimado desde este nodo al nodo objetivo

    def __lt__(self, other):
        # Método para comparar nodos basado en la suma de costos y heurísticas
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

# Algoritmo de búsqueda A*
def astar_search(initial_state, goal_state, heuristic_func): # como entrada el estado inicial, el estado objetivo y una función heurística
    open_list = []  # Lista de nodos por explorar
    heapq.heappush(open_list, Node(initial_state, None, None, 0, heuristic_func(initial_state, goal_state)))
    closed_set = set()  # Conjunto de nodos explorados

    while open_list:
        current_node = heapq.heappop(open_list)  # Nodo actual a explorar

        if current_node.state == goal_state:
            path = []
            while current_node: # continuará hasta que open_list esté vacía, lo que significa que todos los nodos posibles han sido explorados o que se encontró una solución.
                # Reconstructa el camino desde el nodo objetivo hasta el nodo inicial
                path.append((current_node.state, current_node.action))
                current_node = current_node.parent
            return list(reversed(path))  # Devuelve el camino en orden desde el inicio al objetivo

        closed_set.add(current_node.state)  # Marca el nodo actual como explorado

        # Expandir nodos vecinos
        neighbors = get_neighbors(current_node.state)  # Obtiene los vecinos del nodo actual
        for neighbor, action, cost in neighbors:
            if neighbor not in closed_set:
                # Calcula el costo acumulado y la heurística para el nuevo nodo
                new_cost = current_node.cost + cost
                new_node = Node(neighbor, current_node, action, new_cost, heuristic_func(neighbor, goal_state))
                heapq.heappush(open_list, new_node)  # Agrega el nuevo nodo a la lista de nodos por explorar

    return None  # No se encontró una solución

# Función heurística: Distancia Manhattan entre dos puntos en la cuadrícula
def manhattan_distance(state, goal_state):
    return abs(state[0] - goal_state[0]) + abs(state[1] - goal_state[1])

# Ejemplo de uso
initial_state = (0, 0)  # Estado inicial del agente
goal_state = (2, 3)  # Estado objetivo al que el agente debe llegar
path = astar_search(initial_state, goal_state, manhattan_distance)  # Realiza la búsqueda A* para encontrar el camino
print("Camino encontrado:", path)  # Imprime el camino encontrado por el agente

# Después de encontrar el camino, imprime la cuadrícula con los movimientos del agente
print("Cuadrícula con Pasos del Agente:")
print_grid_with_path(4, [step[0] for step in path]) # Imprime la cuadrícula con el camino del agente