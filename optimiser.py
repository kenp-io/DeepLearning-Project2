import torch
import parameter

class SGD(object):

<<<<<<< HEAD
    def __init__(self, parameters, lr=0.005):
=======
    def __init__(self, parameters, lr=0.01):
>>>>>>> Changerd names and added optimiser and parameters
        self.parameters = parameters
        self.lr = lr


    def zero_grad(self):
        for param in self.parameters:
            param.zero_grad()

<<<<<<< HEAD
    def step(self):
        for param in self.parameters:
            param.value -= self.lr * param.grad
=======

    def step():
        for param in self.parameters:
            param -= self.lr * param.grad

p = parameter.Parameter((1,2,3))

s = SGD(p)

p.zero_grad()
>>>>>>> Changerd names and added optimiser and parameters