from Neural_Network import Perceptron, Layer, NeuralNetwork

p = Perceptron(4)

out = p.calcOutput([0.1,0.3,0.5,0.2])

print(p.weights)

print(out)