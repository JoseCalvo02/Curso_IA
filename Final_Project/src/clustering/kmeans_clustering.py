# kmeans_clustering.py
from sklearn.cluster import KMeans
import pandas as pd

class KMeansClustering:
    def __init__(self, data_path):
        # Leer los datos del archivo CSV y almacenarlos en el atributo 'data'
        self.data = pd.read_csv(data_path)

    def apply_kmeans(self, num_clusters):
        """
        Aplica el algoritmo de K-medios a los datos de películas.

        Args:
        - num_clusters (int): Número de clústeres a formar.

        Returns:
        - Tuple: Conjunto de datos con asignación de clústeres y centros de clústeres.
        """
        # Selecciona solo las características relevantes
        features = self.data[['Rating', 'Year']]

        # Crea una instancia del modelo de K-medios y establece n_init explícitamente
        kmeans_model = KMeans(n_clusters=num_clusters, random_state=42, n_init=10)

        # Aplica el algoritmo de K-medios
        self.data['cluster'] = kmeans_model.fit_predict(features)

        # Devolver el conjunto de datos con la asignación de clústeres y los centros de los clusters
        return self.data, kmeans_model.cluster_centers_