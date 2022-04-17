# реализовать операцию над дробью, то есть создать класс Fraction у него будет 2 атрибута (numertor, denumerator)
# сделать add, sub, mul, floordiv (Dunder Methods)
# по правилам математики!)
# class Frac:
#     def __int__(self,numerator,denominator):
#         self.numerator=numerator
#         self.denominator=denominator
#
#     def _get_frac(self):
#             print(self.numerator)
#             print(self.denominator)
#
#     def __add__(self,numerator,denominator):
#             print("It is Donder method__add__")
#             self.numerator +=self.denominator
#             self._get_frac()
#
#     def __sub__(self,numerator,denominator ):
#             print("It is Donder method __sub__")
#             self.numerator =self.denominator
#             self._get_frac()
#
#     def __mul__(self,numerator,denominator ):
#             print("It is Donder method__mul__")
#             self.numerator *= numerator,denominator
#             self._get_frac()
#
#     def __floordiv__(self,numerator,denominator):
#             print("It is Donder method__floordiv__")
#             self.numerator //=denominator
#             self._get_frac()
#
#     def __truediv__(self,numerator,denominator ):
#             print("It is Donder method__truediv__")
#             self.numerator /= denominator
#             self._get_frac()
import fractions

fract = fractions.Fraction(122, 124) + fractions.Fraction(1, 2)
print("Numerator: {}".format(fract.numerator))
print("Denominator: {}".format(fract.denominator))


fract = fractions.Fraction(122, 124) - fractions.Fraction(1, 2)
print("Numerator: {}".format(fract.numerator))
print("Denominator: {}".format(fract.denominator))


fract = fractions.Fraction(122, 124)  *fractions.Fraction(1, 2)
print("Numerator: {}".format(fract.numerator))
print("Denominator: {}".format(fract.denominator))


fract = fractions.Fraction(122, 124) / fractions.Fraction(1, 2)
print("Numerator: {}".format(fract.numerator))
print("Denominator: {}".format(fract.denominator))


fract = fractions.Fraction(122, 124) // fractions.Fraction(1, 2)
print("Numerator: {}".format(fract.numerator))
print("Denominator: {}".format(fract.denominator))