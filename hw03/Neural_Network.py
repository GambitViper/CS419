import random
import math

class Perceptron():

    def initRandomWeight(self, num_weights):
        weights = []
        for _ in range(num_weights):
            weights.append(random.random())
        return weights

    def __init__ (self, num_inputs):
        self.num_weights = num_inputs + 1
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

    def __repr__(self):
        return '\n\t\tPerceptron(Num_Weights= %s)' % (self.num_weights)
        

class Layer():

    def initPercpectrons(self, layer_size, input_len, isIn):
        perceptrons = []
        if isIn == "input":
            for _ in range(layer_size):
                p = 0
                perceptrons.append(p)
        else:
            for _ in range(layer_size):
                p = Perceptron(input_len)
                perceptrons.append(p)
        return perceptrons

    def __init__ (self, layer_size, input_length, output_length, isIn):
        self.input_length = input_length
        self.isIn = isIn
        self.layer_size = layer_size
        self.output_length = output_length
        self.output = 0
        self.deltas = []
        self.perceptrons = self.initPercpectrons(layer_size, input_length, isIn)

    def __repr__(self):
        return '\nLayer(InputLen=%s,\tLayerSize=%s,\tOutputLen=%s, \n\tPerceptrons=%s)' % (self.input_length, self.layer_size, self.output_length, self.perceptrons)

class DataWithClass:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def classification_index(self):
        for x in range(len(self.y)):
            if self.y[x] == 1:
                return x
    
    def __repr__(self):
        return '\nData(\n\tx=%s,\n\ty=%s)' % (self.x, self.y)

class NeuralNetwork(object):

    def initLayers(self, input_layer_size, num_layers, hidden_layer_sizes):
        layers = []
        for x in range(num_layers):
            if x == 0:
                l = Layer(input_layer_size, input_layer_size, input_layer_size, "input")
                layers.append(l)
            elif x == num_layers - 1:
                l = Layer(14, layers[x - 1].layer_size, 14, "non")
                layers.append(l)
            else:
                layer_size = hidden_layer_sizes.pop(0)
                l = Layer(layer_size, layers[x - 1].layer_size, layer_size, "non")
                layers.append(l)
        return layers
    
    def __init__ (self, resolution, input_layer_size, num_layers, hidden_layer_sizes):
        self.resolution = resolution
        self.num_layers = num_layers
        self.hidden_layer_sizes = hidden_layer_sizes
        self.layers = self.initLayers(input_layer_size, num_layers, hidden_layer_sizes)

    def backProp(self, examples):
        # Propagate inputs forward to compute outputs
        for e in range(len(examples)):
            self.layers[0].output = examples[e].x
            for l in range(1, self.num_layers):
                # Calculate layer output from previous layer output
                toutputs = []
                for p in self.layers[l].perceptrons:
                    tout = p.calcOutput(self.layers[l - 1].output)
                    toutputs.append(tout)
                self.layers[l].output = toutputs
            # Propagate deltas backward from output layer to input layer
            deltas = []
            oidx = len(self.layers) - 1
            for d in range(len(self.layers[oidx].output)):
                prev_out = self.layers[oidx - 1].output[d]
                curr_out = self.layers[oidx].output[d]
                delt =  (prev_out * (1 - prev_out)) * (examples[e].y[d] - curr_out)
                deltas.append(delt)
            self.layers[oidx].deltas = deltas
            for k in range(oidx - 1, 0, -1):
                middeltas = []
                for m in range(len(self.layers[k].perceptrons)):
                    my_out = self.layers[k].output[m]
                    gprime = (my_out * (1 - my_out))
                    
