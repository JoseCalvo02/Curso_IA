# kmeans_clustering.py
from sklearn.cluster import KMeans
import pandas as pd

class KMeansClustering:
    def __init__(self, data_path):
        self.data = pd.read_csv(data_path)

    def apply_kmeans(self, num_clusters):
        # Selecciona solo las características relevantes (ajusta según tu conjunto de datos)
        features = self.data[['Rating', 'Year']]

        # Crea una instancia del modelo de K-medios y establece n_init explícitamente
        kmeans_model = KMeans(n_clusters=num_clusters, random_state=42, n_init=10)

        # Aplica el algoritmo de K-medios
        self.data['cluster'] = kmeans_model.fit_predict(features)

        # Devolver el conjunto de datos con la asignación de clústeres y los centros de los clusters
        return self.data, kmeans_model.cluster_centers_