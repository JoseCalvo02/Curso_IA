import random
import networkx as nx

class AntColony:
    def __init__(self, graph, n_ants, n_best, n_iterations, decay, alpha=1, beta=1):
        """
        Inicializa el objeto AntColony.

        Args:
        graph (nx.Graph): Grafo sobre el cual se realizará la búsqueda.
        n_ants (int): Número de hormigas.
        n_best (int): Número de mejores soluciones a seguir.
        n_iterations (int): Número de iteraciones.
        decay (float): Tasa de evaporación de feromona.
        alpha (int, optional): Ponderación de la feromona. Default es 1.
        beta (int, optional): Ponderación de la visibilidad. Default es 1.
        """
        self.graph = graph
        self.n_ants = n_ants
        self.n_best = n_best
        self.n_iterations = n_iterations
        self.decay = decay
        self.alpha = alpha
        self.beta = beta
        self.best_path = None
        self.best_path_cost = float('inf')

    def run(self):
        """
        Ejecuta el algoritmo de Enfoque de Colonia de Hormigas.
        """
        for _ in range(self.n_iterations):
            solutions = self._generate_solutions()
            self._update_pheromone(solutions)
            best_solution = min(solutions, key=lambda x: x[1])
            if best_solution[1] < self.best_path_cost:
                self.best_path = best_solution[0]
                self.best_path_cost = best_solution[1]
        return self.best_path, self.best_path_cost

    def _generate_solutions(self):
        """
        Genera soluciones candidatas.

        Returns:
        list: Lista de tuplas (ruta, costo) de las soluciones generadas.
        """
        solutions = []
        for _ in range(self.n_ants):
            path = self._ant_run()
            cost = self._calculate_path_cost(path)
            solutions.append((path, cost))
        return solutions

    def _ant_run(self):
        """
        Ejecuta una hormiga para construir una solución.

        Returns:
        list: Ruta construida por la hormiga.
        """
        path = []
        start_node = random.choice(list(self.graph.nodes))
        path.append(start_node)

        while len(path) < len(self.graph.nodes):
            current_node = path[-1]
            unvisited_neighbors = [n for n in self.graph.neighbors(current_node) if n not in path]
            if not unvisited_neighbors:
                break
            probabilities = self._calculate_probabilities(current_node, unvisited_neighbors)
            next_node = random.choices(unvisited_neighbors, weights=probabilities)[0]
            path.append(next_node)
        return path

    def _calculate_probabilities(self, current_node, unvisited_neighbors):
        probabilities = []
        total_pheromone = 0
        for neighbor in unvisited_neighbors:
            pheromone = self.graph[current_node][neighbor]['pheromone']
            visibility = 1 / self.graph[current_node][neighbor]['weight']  # Inversamente proporcional a la longitud de la arista
            total_pheromone += (pheromone ** self.alpha) * (visibility ** self.beta)

        for neighbor in unvisited_neighbors:
            pheromone = self.graph[current_node][neighbor]['pheromone']
            visibility = 1 / self.graph[current_node][neighbor]['weight']
            probability = ((pheromone ** self.alpha) * (visibility ** self.beta)) / total_pheromone
            probabilities.append(probability)

        return probabilities

    def _calculate_path_cost(self, path):
        """
        Calcula el costo de una ruta.

        Args:
        path (list): Ruta para calcular el costo.

        Returns:
        float: Costo total de la ruta.
        """
        cost = 0
        for i in range(len(path) - 1):
            cost += self.graph[path[i]][path[i + 1]]['weight']
        return cost

    def _update_pheromone(self, solutions):
        """
        Actualiza la feromona en las aristas del grafo.

        Args:
        solutions (list): Lista de tuplas (ruta, costo) de las soluciones generadas.
        """
        for node1, node2, attrs in self.graph.edges(data=True):
            pheromone = attrs['pheromone']
            # Aplicar evaporación
            pheromone *= (1.0 - self.decay)
            self.graph[node1][node2]['pheromone'] = pheromone

        # Depositar feromona en las aristas de las mejores soluciones
        for path, cost in solutions[:self.n_best]:
            for i in range(len(path) - 1):
                node1, node2 = path[i], path[i + 1]
                self.graph[node1][node2]['pheromone'] += 1.0 / cost