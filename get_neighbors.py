# Función get_neighbors(state) toma una posición (state) en la cuadrícula y devuelve los vecinos válidos.
def get_neighbors(state):
    row, col = state
    neighbors = []

    # Mover arriba
    if row > 0:
        neighbors.append(((row - 1, col), 'UP', 1))

    # Mover abajo
    if row < 3:
        neighbors.append(((row + 1, col), 'DOWN', 1))

    # Mover izquierda
    if col > 0:
        neighbors.append(((row, col - 1), 'LEFT', 1))

    # Mover derecha
    if col < 3:
        neighbors.append(((row, col + 1), 'RIGHT', 1))

    return neighbors