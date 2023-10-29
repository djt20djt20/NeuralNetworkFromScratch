from src.Neuron import Neuron

class Layer:
    def __init__(self,input_length, layer_size):
        self.neurons = [Neuron(input_length) for _ in range(layer_size)]
    
    def __call__(self,x):
        return [n(x) for n in self.neurons]
    
    def parameters(self):
        return [p for n in self.neurons for p in n.parameters()]

