import torch
import parameter

class SGD(object):

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    def __init__(self, parameters, lr=0.005):
=======
    def __init__(self, parameters, lr=0.01):
>>>>>>> Changerd names and added optimiser and parameters
=======
    def __init__(self, parameters, lr=0.005):
>>>>>>> Optimisatino debug
=======
    def __init__(self, parameters, lr=0.005):
>>>>>>> b5a787b4618340bb03d5ef9efd504ff08192613f
        self.parameters = parameters
        self.lr = lr


    def zero_grad(self):
        for param in self.parameters:
            param.zero_grad()

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    def step(self):
        for param in self.parameters:
            param.value -= self.lr * param.grad
<<<<<<< HEAD
=======

    def step():
=======
    def step(self):
>>>>>>> Optimiser works
        for param in self.parameters:
            param.value -= self.lr * param.grad

p = parameter.Parameter((1,2,3))

s = SGD(p)

p.zero_grad()
>>>>>>> Changerd names and added optimiser and parameters
=======
>>>>>>> Optimisatino debug
=======
    def step(self):
        for param in self.parameters:
            param.value -= self.lr * param.grad
>>>>>>> b5a787b4618340bb03d5ef9efd504ff08192613f
