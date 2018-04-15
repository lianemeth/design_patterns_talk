class OldBorg:
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state

class NewBorg:
    __state = {}

    def __new__(cls, *args, **kwargs):
        self = super().__new__(cls, *args, **kwargs)
        self.__dict__ = cls.__state
        return self

class TestBorg(NewBorg):

    def __init__(self):
        super().__init__()
        self.a = 1
        self.b = 2

if __name__ == "__main__":
    te1 = TestBorg()
    te2 = TestBorg()
    te2.a = 10
    assert te1.a == te2.a and te1.a == 10
    assert te1.b == te2.b and te2.b == 2
