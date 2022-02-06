from fractions import Fraction
a = 0.6/10
b=Fraction(str(a))
print('Valor de b: ',b)

c=Fraction(str(a)).limit_denominator()
print('Valor de c: ',c)
