
class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def add_(self, other):
        addition_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        addition_denominator = self.denominator * other.denominator
        print("Сумма", addition_numerator, "/", addition_denominator)
        return (addition_numerator, addition_denominator)
    def __sub__(self, other):
        subtraction_numerator = self.numerator * other.denominator - self.numerator * other.denominator
        subtraction_denominator = self.denominator - other.denominator
        print("разность", subtraction_numerator, "/", subtraction_denominator)
        return (subtraction_numerator, subtraction_denominator)
    def __floordiv__(self, other):
        floordiv_numerator = self.numerator * other.denominator//other.numerator * self.denominator
        floordiv_denominator = self.denominator // other.numerator
        print("Частное равно: ", floordiv_numerator, "/", floordiv_denominator)
        return (floordiv_numerator, floordiv_denominator)

    def __mul__(self,other):
        multiplication_numerator = self.numerator * other.numerator*other.numerator * self.denominator
        multiplication_denominator = self.denominator * other.denominator
        print("Произведение равно: ", multiplication_numerator, "/", multiplication_denominator)
        return (multiplication_numerator, multiplication_denominator)


if __name__ == "__main__":
    r1 = Fraction(5, 2)
    r2 = Fraction(3, 4)
    r1.add_(r2)
if __name__ == "main":
    r1 = Fraction(4,2)
    r2 = Fraction(8, 4)
    r1.__sub__(r2)
if __name__ == "__main__":
    r1 = Fraction(6, 2)
    r2 = Fraction(5, 4)
    r1.__floordiv__(r2)

if __name__ == "__main__":
    r1 = Fraction(1, 2)
    r2 = Fraction(3, 4)
    r1.__mul__(r2)