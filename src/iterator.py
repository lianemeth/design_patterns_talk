class Fibonacci:

    def __init__(self, n):
        self.a = 0
        self. b = 1
        self.n = n
        self.ii = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.ii > self.n:
            raise StopIteration
        else:
            self.ii += 1
            res = self.a
            self.a, self.b = self.b, self.a + self.b
            return res


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    for i in Fibonacci(10):
        print(i)

