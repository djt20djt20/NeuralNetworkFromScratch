from src.Layer import Layer

class MLP:
    def __init__(self, input_length, list_of_layers):
        total_list_of_layers = [input_length] + list_of_layers
        self.layers = [Layer(total_list_of_layers[i],total_list_of_layers[i+1]) for i in range(len(total_list_of_layers)-1)]
    
    def __call__(self, x):
        for layer in self.layers:
            x = layer(x)
        return x[0] if len(x) == 1 else x
    
    def parameters(self):
        return [p for l in self.layers for p in l.parameters()]
    
    def zero_grad(self):
        for p in self.parameters():
            p.grad = 0