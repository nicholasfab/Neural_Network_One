import numpy as np


def sigmoid(x):

    return 1 / (1 + np.exp(-x))

    
inputs = np.array([[0, 0, 1],
                   [0, 1, 1],
                   [1, 0, 1],
                   [1, 1, 1]])

output = np.array([[0, 0, 0, 1]]).T


weight = 2 * np.random.random((3, 1)) - 1




#training
for i in range(100):
    l1 = np.dot(inputs, weight)
    out = inputs * l1

    sigout = sigmoid(output)

    err2 = sigout * (1 - sigout)

    weight -= err2*weight

print(err2)
print(l1)
