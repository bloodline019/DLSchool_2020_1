class Neuron:

    def __init__(self, w, f = lambda x: x):
        self.w = w
        self.f = f

    def forward(self, x):
        self.x = x
        i = sum(self.w[i] * x[i] for i in range(len(x)))
        return self.f(i)

    def backlog(self):
        return self.x

