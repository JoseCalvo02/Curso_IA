# spectral_clustering.py
from sklearn.cluster import SpectralClustering
import pandas as pd

class SpectralClusteringModel:
    def __init__(self, data_path):
        # Leer los datos del archivo CSV y almacenarlos en el atributo 'data'
        self.data = pd.read_csv(data_path)

    def apply_spectral_clustering(self, num_clusters):
        """
        Aplica el algoritmo de Agrupamiento Espectral a los datos de películas.

        Args:
        - num_clusters (int): Número de clústeres a formar.

        Returns:
        - DataFrame: Conjunto de datos con asignación de clústeres.
        """
        # Selecciona solo las características relevantes
        features = self.data[['Rating', 'Year']]  # Ajusta estas columnas según tu conjunto de datos

        # Crea una instancia del modelo de Agrupamiento Espectral
        spectral_model = SpectralClustering(n_clusters=num_clusters, random_state=42)

        # Aplica el algoritmo de Agrupamiento Espectral
        self.data['cluster'] = spectral_model.fit_predict(features)

        # Devuelve el conjunto de datos con la asignación de clústeres
        return self.data