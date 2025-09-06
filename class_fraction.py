class Fraction:
    def __init__(self, a: int, b: int):
        if b == 0:
            raise ValueError("denominator cannot be 0")
        self.a: int = a
        self.b: int = b


    def add(self, other):
        return Fraction(self.a * other.b + other.a * self.b, self.b * other.b)

    def subtract(self, other):
        return Fraction(self.a * other.b - other.a * self.b, self.b * other.b)

    def multiply(self, other):
        return Fraction(self.a * other.a, self.b * other.b)

    def divide(self, other):
        if other.a == 0:
            raise ZeroDivisionError("division by zero")
        return Fraction(self.a * other.b, self.b * other.a)