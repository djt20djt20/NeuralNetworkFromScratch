from src.Value import Value
import random
class Neuron:
    def __init__(self, input_size):
        self.w = [Value(random.uniform(-1,1)) for _ in range(input_size)]
        self.b = Value(random.uniform(-1,1))
    
    def __call__(self,x):
        output = self.b
        for wi, xi in zip(x,self.w):
            output += wi * xi
        return output.tanh()
    
    def parameters(self):
        return self.w + [self.b]