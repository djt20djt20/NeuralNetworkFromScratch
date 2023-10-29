import math

class Value:
  def __init__(self,data, parents = (), parents_operation = '', label = ''):
    self.data = data
    self.parents = parents
    self.parents_operation = parents_operation
    self.label = label
    self.grad = 0

  def __repr__(self):
    return f'Value(data={self.data})'

  def __add__(self, other):
    if (type(other) is int) or (type(other) is float):
       other = Value(other)
    return Value(
        self.data + other.data, 
        parents = (self, other), 
        parents_operation = '+'
    )
  
  def __neg__(self):
     return self * -1
  
  def __sub__(self, other):
     return self + (-other)
  
  def __rsub__(self, other):
     return other + (-self)

  def __radd__(self, other):
     return self + other

  def __mul__(self,other):
    if (type(other) is int) or (type(other) is float):
       other = Value(other)
    return Value(
        self.data * other.data,
        parents = (self, other),
        parents_operation = '*')
  
  def __rmul__(self, other):
     return self * other
  
  def tanh(self):
    return Value(
        (math.exp(2*self.data)-1) / (math.exp(2*self.data) + 1),
        (self,),
        'tanh')
  
  def calculate_gradient(self, first = True):
    if first:
       self.grad = 1
    if self.parents != ():
      if len(self.parents) == 1:
        if self.parents_operation == 'tanh':
           parent = self.parents[0]
           parent.grad += (1 - ((math.exp(2*parent.data)-1) / (math.exp(2*parent.data) + 1))**2) * self.grad
        parent.calculate_gradient(False)
      elif len(self.parents) == 2:
        parent_1 = self.parents[0]
        parent_2 = self.parents[1]
        if self.parents_operation == '*':
          parent_1.grad += parent_2.data * self.grad
          parent_2.grad += parent_1.data * self.grad
        if self.parents_operation == '+':
          parent_1.grad += self.grad
          parent_2.grad += self.grad
        parent_1.calculate_gradient(False)
        parent_2.calculate_gradient(False)