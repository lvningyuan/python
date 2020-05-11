class Iter:
    def __init__(self, n =100):
        self.a = 0
        self.b = 1
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > self.n:   #停止迭代
            raise StopIteration
        return self.a
