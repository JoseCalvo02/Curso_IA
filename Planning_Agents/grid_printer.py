def print_grid_with_path(grid_size, path):
    # Itera sobre las filas del tablero
    for i in range(grid_size):
        # Imprime el borde superior de las celdas de la fila actual
        print("+---" * grid_size + "+")

        # Itera sobre las columnas del tablero
        for j in range(grid_size):
            # Verifica si la celda actual está en el camino del agente (marcada con 'X')
            if (i, j) in path:
                # Si está en el camino, imprime 'X' en la celda
                print(f"| X ", end="")
            else:
                # Si la celda no está en el camino, imprime '0' en lugar de los números
                print(f"| 0 ", end="")
        # Imprime el borde derecho de las celdas de la fila actual y pasa a la siguiente línea
        print("|")

    # Imprime el borde inferior de las celdas y termina la cuadrícula
    print("+---" * grid_size + "+")