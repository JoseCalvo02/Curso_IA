1. **Instalación de Dependencias**: Antes de ejecutar el código, utilizar el archivo `requirements.txt` para instalar las dependencias:

    # Instala las dependencias desde el archivo requirements.txt
    pip install -r requirements.txt


## Cómo Funciona el Algoritmo

**Método de Agrupación:**

*K-medios:* Utiliza un enfoque iterativo para asignar puntos de datos a clusters basándose en la distancia entre los puntos y los centroides de los clusters. Se actualizan los centroides y las asignaciones de puntos en cada iteración.
*Agrupamiento Espectral:* Utiliza técnicas de álgebra lineal y la estructura de la matriz de afinidad para agrupar los puntos de datos. Se basa en la descomposición espectral de la matriz de afinidad para obtener los vectores propios, y luego utiliza k-means para asignar los puntos a clusters.

**Manejo de la Estructura de Datos:**

*K-medios:* Trabaja directamente con los datos y utiliza la distancia entre puntos para formar clusters.
*Agrupamiento Espectral:* Considera la estructura global de los datos mediante la construcción y análisis de la matriz de afinidad.

**Tipo de Datos:**

*K-medios:* Adecuado para datos numéricos y categóricos.
*Agrupamiento Espectral:* Puede manejar datos complejos, incluyendo relaciones no lineales.