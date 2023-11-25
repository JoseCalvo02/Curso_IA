import sys
sys.path.append("..")

import tkinter as tk
from clustering.kmeans_clustering import KMeansClustering
from clustering.spectral_clustering import SpectralClusteringModel
import plotly.express as px
import plotly.graph_objects as go

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Movie Recommendation System")

        self.kmeans_button = tk.Button(root, text="Aplicar K-medios", command=self.apply_kmeans)
        self.kmeans_button.pack(pady=10)

        self.spectral_button = tk.Button(root, text="Aplicar Agrupamiento Espectral", command=self.apply_spectral)
        self.spectral_button.pack(pady=10)

        # Agregar un componente para mostrar los resultados del clustering
        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)

        # Agregar un componente para mostrar gráficos interactivos
        self.graph_container = tk.Frame(root)
        self.graph_container.pack(pady=10)

    def apply_kmeans(self):
        kmeans_model = KMeansClustering('../../data/movies.csv')
        clustered_data, cluster_centers = kmeans_model.apply_kmeans(num_clusters=3)

        # Mostrar los resultados
        self.display_results(clustered_data, cluster_centers)

        # Mostrar gráfico interactivo
        self.display_interactive_graph(clustered_data)

    def apply_spectral(self):
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
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()