import math

class Neuron:
    def __init__(self, num_inputs):
        # Inicializamos los pesos y el sesgo de manera aleatoria
        self.weights = [0.0] * num_inputs
        self.bias = 0.0

    def _sigmoid(self, x):
        # Función de activación sigmoide
        return 1 / (1 + math.exp(-x))

    def activate(self, inputs):
        # Realiza la suma ponderada de las entradas y los pesos, y luego suma el sesgo
        calculation = sum(w * x for w, x in zip(self.weights, inputs)) + self.bias
        # Aplica la función de activación sigmoide
        return self._sigmoid(calculation)

    def train(self, inputs, target_output, learning_rate=0.1):
        # Calcula la salida actual de la neurona
        output = self.activate(inputs)
        # Calcula el error
        error = target_output - output
        # Ajusta los pesos y el sesgo usando el algoritmo de descenso de gradiente
        self.weights = [w + learning_rate * error * x for w, x in zip(self.weights, inputs)]
        self.bias += learning_rate * error

# Datos de entrenamiento para la operación XOR
training_data = [
    ([0, 0], 0),
    ([0, 1], 1),
    ([1, 0], 1),
    ([1, 1], 0)
]

# Creamos una neurona con 2 entradas
neuron = Neuron(2)

# Entrenamos la neurona usando los datos de entrenamiento
for _ in range(10000):
    for inputs, target_output in training_data:
        neuron.train(inputs, target_output)

# Probamos la neurona entrenada
print("Resultado para [0, 0]:", neuron.activate([0, 0]))
print("Resultado para [0, 1]:", neuron.activate([0, 1]))
print("Resultado para [1, 0]:", neuron.activate([1, 0]))
print("Resultado para [1, 1]:", neuron.activate([1, 1]))