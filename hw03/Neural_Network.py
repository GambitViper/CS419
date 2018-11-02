import random
import math

class Perceptron():

    def initRandomWeight(self, num_weights):
        weights = []
        for _ in range(num_weights):
            weights.append(random.random())
        return weights

    def __init__ (self, num_inputs):
        self.num_weights = num_inputs + 1,
        self.weights = self.initRandomWeight(num_inputs + 1)

    def g(self, val):
        epow = math.pow(math.e, (-1 * val))
        return 1 / (1 + epow)
    
    def calcOutput(self, inputs):
        acc = self.weights[0]
        for x in range(1, len(self.weights)):
            acc += self.weights[x] * inputs[x - 1]
        return self.g(acc)
        
    def updateWeights(self, delta, inputs):
        # w(i,j) <- w(i,j) + α X a(i) X Δ[j]
        self.weights[0] += delta
        for x in range(1, len(self.weights)):
            self.weights[x] += (inputs[x - 1] * delta)
        

class Layer():

    def initPercpectrons(self, layer_size, input_len):
        perceptrons = []
        for _ in range(input_len):
            p = Perceptron(input_len)
            perceptrons.append(p)
        return perceptrons

    def __init__ (self, layer_size, input_length, output_length):
        self.input_length = input_length,
        self.layer_size = layer_size,
        self.output_length = output_length,
        self.perceptrons = self.initPercpectrons(layer_size, input_length)

class NeuralNetwork(object):
    
    def __init__ (self, resolution, num_layers, hidden_layer_sizes):
        self.resolution = resolution,
        self.num_layers = num_layers,
        self.hidden_layer_sizes = hidden_layer_sizes

    def learn(self, examples):
        pass
