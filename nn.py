import numpy as np
from numpy import array, exp
import math
import random

def sigmoid(x):
  return 1 / (1 + math.exp(-x))


#training

inputs = [0,  1]
expected = [1, 0]

weights = [0, 0]

output = []

for i in expected:
  output.append(0)

for h in range(0, 10):

  inputs = output

  x = 0
  
  for i in inputs:
    error = (sigmoid(expected[inputs.index(i)]) - sigmoid(i))
    weights[inputs.index(i)] = error
  
  for i in output:
    i = inputs[output.index(i)] + weights[output.index(i)]
    output[x] = i
    x += 1

print(output)
