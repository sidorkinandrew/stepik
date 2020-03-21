class Neuron:

    def __init__(self, w, f = lambda x: x):
        self.w = w
        self.f = f
        self.x = None

    def forward(self, x):
        self.x = x
        return self.f(sum(wi*xi for wi, xi in zip(self.w, self.x)))

    def backlog(self):
        return self.x