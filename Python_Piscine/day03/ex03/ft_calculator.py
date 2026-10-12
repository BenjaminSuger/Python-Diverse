class calculator:
    """calculator allowing to manipulate objects"""
    def __init__(self, input):
        """calculator constructor"""
        if not isinstance(input, list):
            raise TypeError("Calculator need a list to be built")
        self.list = input

    def __add__(self, object) -> None:
        """addition"""
        for i in range(0, len(self.list)):
            self.list[i] += object
        print(self.list)

    def __mul__(self, object) -> None:
        """multiplication"""
        for i in range(0, len(self.list)):
            self.list[i] *= object
        print(self.list)

    def __sub__(self, object) -> None:
        """sub"""
        for i in range(0, len(self.list)):
            self.list[i] -= object
        print(self.list)

    def __truediv__(self, object) -> None:
        """true division"""
        if object == 0:
            raise ZeroDivisionError("Division by 0")
        for i in range(0, len(self.list)):
            self.list[i] /= object
        print(self.list)
