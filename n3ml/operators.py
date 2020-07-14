import numpy as np


class Operator(object):
    def __init__(self):
        pass


class Init(Operator):
    def __init__(self, tensor, initializer=None):
        # TODO: 오버로딩으로 구현
        self.tensor = tensor
        self.initializer = initializer

        pass

    def run_step(self):
        pass


class Matmul(Operator):
    def __init__(self, y, x, W):
        self.y = y
        self.x = x
        self.W = W

    def run_step(self):
        self.y = np.matmul(self.x, self.W.transpose())


class Add(Operator):
    def __init__(self, z, x, y):
        self.z = z
        self.x = x
        self.y = y

    def make_step(self):
        self.z = self.x + self.y


class Mul(Operator):
    def __init__(self, z, x, y):
        self.z = z
        self.x = x
        self.y = y

    def make_step(self):
        self.z = self.x * self.y


class Div(Operator):
    def __init__(self, z, x, y):
        self.z = z
        self.x = x
        self.y = y

    def make_step(self):
        self.z = self.x / self.y
