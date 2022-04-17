# import fractions
#
# fract = fractions.Fraction(122, 124) + fractions.Fraction(1, 2)
# print("Numerator: {}".format(fract.numerator))
# print("Denominator: {}".format(fract.denominator))
#
#
# fract = fractions.Fraction(122, 124) - fractions.Fraction(1, 2)
# print("Numerator: {}".format(fract.numerator))
# print("Denominator: {}".format(fract.denominator))
#
#
# fract = fractions.Fraction(122, 124)  *fractions.Fraction(1, 2)
# print("Numerator: {}".format(fract.numerator))
# print("Denominator: {}".format(fract.denominator))
#
#
# fract = fractions.Fraction(122, 124) / fractions.Fraction(1, 2)
# print("Numerator: {}".format(fract.numerator))
# print("Denominator: {}".format(fract.denominator))
#
#
# fract = fractions.Fraction(122, 124) // fractions.Fraction(1, 2)
# print("Numerator: {}".format(fract.numerator))
# print("Denominator: {}".format(fract.denominator))
s = input()
l_s=len(s)
r_s=""

for i in range(l_s-1,-1,-1):
    r_s+=s[i]

print("Reuslt is: ",r_s)
if(r_s==s):
    print("PALINDROME")
else:
    print("NOT PALINDROME")