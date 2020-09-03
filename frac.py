class Fraction(object):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @staticmethod
    def gcd(x, y):
        if x < y:
            y, x = x, y

        while y > 0:
            x, y = y, x % y
        return x

    def __add__(self, other):
        x = self.a * other.b + self.b * other.a
        y = self.b * other.b
        r = self.gcd(x, y)
        return Fraction(x / r, y / r)

    def __sub__(self, other):
        other = Fraction(0 - other.a, other.b)
        return self.__add__(other)

    def __mul__(self, other):
        x = self.a * other.a
        y = self.b * other.b
        r = self.gcd(x, y)
        return Fraction(x // r, y // r)

    def __truediv__(self, other):
        other = Fraction(other.b, other.a)
        return self.__mul__(other)

    def val(self):
        return self.a / self.b

    def __repr__(self):
        return f'Fraction({self.a}, {self.b})'


n1 = Fraction(1, 1)
n2 = Fraction(7, 1)
n3 = Fraction(4, 1)
n4 = Fraction(5, 1)
val = (n2 * n3) - n4 + n1
print(val.val() == 24)

x = Fraction(7, 1)
y = Fraction(1, 1)
print(x - y)
