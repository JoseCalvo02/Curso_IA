import sys # Importar el módulo sys para realizar ajustes en el sistema y manipular la ruta de búsqueda de módulos
sys.path.append("..") # Agregar un directorio al sistema de rutas para permitir la importación de módulos desde un directorio superior

# Importar clases específicas desde módulos
from clustering.kmeans_clustering import KMeansClustering
from clustering.spectral_clustering import SpectralClusteringModel

import tkinter as tk # Importar la biblioteca tkinter para construir interfaces gráficas
import pandas as pd # Importar la biblioteca pandas para manipulación y análisis de datos
import plotly.express as px # px proporciona una interfaz de alto nivel para la creación de gráficos
import plotly.graph_objects as go # go proporciona una interfaz de bajo nivel para la creación de gráficos

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Movie Recommendation System")

        # Obtener las dimensiones de la pantalla
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Calcular la posición para centrar la ventana
        x_position = (screen_width - 600) // 2  # Ancho de la ventana principal
        y_position = (screen_height - 400) // 2  # Altura de la ventana principal

        # Establecer la posición de la ventana en el centro
        self.root.geometry(f"600x400+{x_position}+{y_position}")

        # Agregar un componente Listbox para mostrar la lista de películas
        self.movie_listbox = tk.Listbox(root, selectmode=tk.SINGLE, height=10, width=40)
        self.movie_listbox.grid(row=0, column=1, padx=10, pady=10, rowspan=2, sticky="nsew")

        # Cargar la lista de películas al iniciar la interfaz
        self.load_movie_list()

        # Agregar botones, etiqueta de resultados y contenedor de gráficos usando grid
        self.kmeans_button = tk.Button(root, text="Aplicar K-medios", command=self.apply_kmeans, width=12, height=2, bg="blue", fg="white", font=("Helvetica", 10))
        self.kmeans_button.grid(row=0, column=0, pady=10, sticky="nsew") # Ubicar el botón en la fila 0 y columna 0 de la cuadrícula

        # Crear botón para aplicar Agrupamiento Espectral
        self.spectral_button = tk.Button(root, text="Aplicar Agrupamiento Espectral", command=self.apply_spectral, width=12, height=2, bg="green", fg="white", font=("Helvetica", 10))
        self.spectral_button.grid(row=1, column=0, pady=10, sticky="nsew") # Ubicar el botón en la fila 1 y columna 0 de la cuadrícula

        # Crear etiqueta para mostrar resultados
        self.result_label = tk.Label(root, text="")
        self.result_label.grid(row=2, column=0, padx=10, sticky="nsew") # Ubicar la etiqueta en la fila 2 y columna 0 de la cuadrícula con un relleno horizontal de 10 píxeles

        # Crear un contenedor para gráficos
        self.graph_container = tk.Frame(root)
        self.graph_container.grid(row=3, column=0, padx=10, sticky="nsew") # Ubicar el contenedor en la fila 3 y columna 0 de la cuadrícula con un relleno horizontal de 10 píxeles

        # Configurar la expansión de las columnas y filas
        root.grid_rowconfigure(0, weight=1)
        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)
        root.grid_columnconfigure(1, weight=1)

    def load_movie_list(self):
        # Cargar los datos del archivo movies.csv y agregarlos a la Listbox
        movie_data = pd.read_csv('../../data/movies.csv')
        for index, row in movie_data.iterrows():
            movie_info = f"{row['Title']} ({row['Year']}), Genre: {row['Genre']}, Rating: {row['Rating']}"
            self.movie_listbox.insert(tk.END, movie_info)

    def apply_kmeans(self):
        """
        Aplica el algoritmo de K-medios al conjunto de datos de películas.

        Crea una instancia de la clase KMeansClustering, que utiliza el algoritmo de K-medios
        para agrupar películas basadas en sus características. Muestra los resultados y genera
        un gráfico interactivo.

        Args:
        - num_clusters (int): Número de clústeres a formar.

        Returns:
        None
        """
        kmeans_model = KMeansClustering('../../data/movies.csv')
        clustered_data, cluster_centers = kmeans_model.apply_kmeans(num_clusters=3)

        # Mostrar los resultados
        self.display_results(clustered_data, cluster_centers)

        # Mostrar gráfico interactivo
        self.display_interactive_graph(clustered_data)

    def apply_spectral(self):
        """
        Aplica el algoritmo de Agrupamiento Espectral al conjunto de datos de películas.

        Crea una instancia de la clase SpectralClusteringModel, que utiliza el algoritmo de
        Agrupamiento Espectral para clasificar películas en clústeres. Muestra los resultados y
        genera un gráfico interactivo.

        Args:
        - num_clusters (int): Número de clústeres a formar.

        Returns:
        None
        """
        spectral_model = SpectralClusteringModel('../../data/movies.csv')
        clustered_data = spectral_model.apply_spectral_clustering(num_clusters=3)

        # Mostrar los resultados
        self.display_results(clustered_data)

        # Mostrar gráfico interactivo
        self.display_interactive_graph(clustered_data)

    def display_results(self, clustered_data, cluster_centers=None):
        # Puedes personalizar esta función según tus necesidades
        # En este ejemplo, solo se muestra la información en la etiqueta de resultados
        result_text = f"Resultados del Clustering:\n{clustered_data[['Title', 'cluster']]}"
        self.result_label.config(text=result_text)

        # Si estás utilizando K-medios, también puedes mostrar los centros de los clusters
        if cluster_centers is not None:
            result_text += f"\nCentros de Clusters:\n{cluster_centers}"
            self.result_label.config(text=result_text)

    def display_interactive_graph(self, clustered_data):
        # Crear un gráfico interactivo utilizando Plotly Express
        fig = px.scatter(clustered_data, x='Rating', y='Year', color='cluster', hover_data=['Title'])

        # Convertir el gráfico de Plotly Express a un gráfico de Plotly Graph Objects
        plotly_fig = go.Figure(fig)

        # Mostrar el gráfico en la interfaz gráfica
        self.display_plotly_graph(plotly_fig)

    def display_plotly_graph(self, plotly_fig):
        # Crear un nuevo contenedor para cada gráfico
        plotly_container = tk.Toplevel(self.root)

        # Mostrar el gráfico Plotly en la interfaz gráfica
        plotly_container.title("Interactive Graph")
        plotly_container.geometry("800x600")

        # Utilizar el método show() de Plotly para mostrar el gráfico
        plotly_fig.show()

if __name__ == "__main__":
    root = tk.Tk() # Crear una instancia de la clase Tk de tkinter, que representa la ventana principal de la interfaz gráfica
    app = MainWindow(root) # Crear una instancia de la clase MainWindow, que define la estructura y comportamiento de la interfaz
    root.mainloop() # Iniciar el bucle principal de la interfaz gráfica, que espera eventos del usuario