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
        self.best_path = None # Mejor ruta encontrada.
        self.best_path_cost = float('inf') # Costo de la mejor ruta, inicializado en infinito.

    def run(self):
        """
        Ejecuta el algoritmo de Enfoque de Colonia de Hormigas.
        """
        for _ in range(self.n_iterations):
            solutions = self._generate_solutions()  # Genera soluciones candidatas.
            self._update_pheromone(solutions)  # Actualiza la feromona en las aristas.
            best_solution = min(solutions, key=lambda x: x[1])  # Encuentra la mejor solución.

            # Comprueba si la solución actual es mejor que la mejor encontrada hasta ahora.
            if best_solution[1] < self.best_path_cost:
                self.best_path = best_solution[0]  # Actualiza la mejor ruta.
                self.best_path_cost = best_solution[1]  # Actualiza el costo de la mejor ruta.

        # El bucle for en run() se repite n_iterations veces, luego termina.
        # Devuelve la mejor ruta y su costo al final de todas las iteraciones.
        return self.best_path, self.best_path_cost

    def _generate_solutions(self):
        """
        Genera soluciones candidatas.

        Returns:
        list: Lista de tuplas (ruta, costo) de las soluciones generadas.
        """
        solutions = []  # Almacena las soluciones generadas.
        for _ in range(self.n_ants):
            path = self._ant_run()  # Ejecuta una hormiga para construir una solución.
            cost = self._calculate_path_cost(path)  # Calcula el costo de la ruta.
            solutions.append((path, cost))  # Agrega la ruta y su costo a la lista de soluciones.
        return solutions  # Devuelve la lista de soluciones.

    def _ant_run(self):
        """
        Ejecuta una hormiga para construir una solución.

        Returns:
        list: Ruta construida por la hormiga.
        """
        path = []  # Ruta construida por la hormiga.
        start_node = random.choice(list(self.graph.nodes))  # Nodo de inicio aleatorio.
        path.append(start_node)  # Agrega el nodo de inicio a la ruta.

        # Repite hasta que la hormiga visite todos los nodos en el grafo.
        while len(path) < len(self.graph.nodes):
            current_node = path[-1]  # Último nodo agregado a la ruta.
            unvisited_neighbors = [n for n in self.graph.neighbors(current_node) if n not in path]  # Vecinos no visitados.

            # Si la hormiga no tiene vecinos no visitados, termina la construcción de la ruta.
            if not unvisited_neighbors:
                break
            probabilities = self._calculate_probabilities(current_node, unvisited_neighbors)  # Calcula las probabilidades de movimiento.
            next_node = random.choices(unvisited_neighbors, weights=probabilities)[0]  # Elige el próximo nodo basándose en las probabilidades.
            path.append(next_node)  # Agrega el próximo nodo a la ruta.
        return path  # Devuelve la ruta construida por la hormiga.

    def _calculate_probabilities(self, current_node, unvisited_neighbors):
        """
        Calcula las probabilidades de movimiento a los nodos vecinos.

        Args:
        current_node (int): Nodo actual.
        unvisited_neighbors (list): Lista de nodos vecinos no visitados.

        Returns:
        list: Lista de probabilidades de movimiento a los nodos vecinos.
        """
        probabilities = []  # Almacena las probabilidades de movimiento.
        total_pheromone = 0  # Suma total de feromonas en las aristas vecinas.

        # Calcula la suma total de feromonas y visibilidad en las aristas vecinas.
        for neighbor in unvisited_neighbors:
            pheromone = self.graph[current_node][neighbor]['pheromone']
            visibility = 1 / self.graph[current_node][neighbor]['weight']  # Inversamente proporcional a la longitud de la arista.
            total_pheromone += (pheromone ** self.alpha) * (visibility ** self.beta)

        # Calcula las probabilidades de movimiento a los nodos vecinos.
        for neighbor in unvisited_neighbors:
            pheromone = self.graph[current_node][neighbor]['pheromone']
            visibility = 1 / self.graph[current_node][neighbor]['weight']
            probability = ((pheromone ** self.alpha) * (visibility ** self.beta)) / total_pheromone
            probabilities.append(probability)  # Agrega la probabilidad a la lista de probabilidades.

        return probabilities  # Devuelve la lista de probabilidades de movimiento a los vecinos no visitados.

    def _calculate_path_cost(self, path):
        """
        Calcula el costo de una ruta.

        Args:
        path (list): Ruta para calcular el costo.

        Returns:
        float: Costo total de la ruta.
        """
        cost = 0  # Costo total de la ruta.

        # Calcula el costo sumando los pesos de las aristas en la ruta.
        for i in range(len(path) - 1):
            cost += self.graph[path[i]][path[i + 1]]['weight']  # Suma los pesos de las aristas en la ruta.
        return cost  # Devuelve el costo total de la ruta.

    def _update_pheromone(self, solutions):
        """
        Actualiza la feromona en las aristas del grafo.

        Args:
        solutions (list): Lista de tuplas (ruta, costo) de las soluciones generadas.
        """
        # Devuelve la lista de probabilidades de movimiento a los vecinos no visitados.
        for node1, node2, attrs in self.graph.edges(data=True):
            pheromone = attrs['pheromone']  # Feromona en la arista actual.
            # Aplicar evaporación: disminuye la feromona existente.
            pheromone *= (1.0 - self.decay)
            self.graph[node1][node2]['pheromone'] = pheromone  # Actualiza la feromona en la arista.

        # Deposita feromona en las aristas de las mejores soluciones generadas por las hormigas.
        for path, cost in solutions[:self.n_best]:
            for i in range(len(path) - 1):
                node1, node2 = path[i], path[i + 1]
                self.graph[node1][node2]['pheromone'] += 1.0 / cost  # Aumenta la feromona en las aristas de la ruta.