import numpy

def polynomialFunction(x):
    return 2*x**3-5*x**2-3*x+6

def trigonometricFunction(x):
    return -3*numpy.sin(x)+6*numpy.cos(x)

def exponentialFunction(x):
    return 5**x-2**x-2

def complexFunction(x):
    return -2*numpy.cos(x)-x**3+x**2-1

def horner(poly, x):
    """
    Funkcja oblicza wartość wielomianu o współczynnikach `poly`
    w punkcie `x` przy pomocy schematu Hornera.
    zwraca wynik
    """
    result = poly[0]
    for i in range(1, len(poly)):
        result = result * x + poly[i]
    return result

def power(input, x):
    """
    Funkcja oblicza wartość potęgi x stopnia liczby input
    uwzględniając x=0 oraz x<0
    niewykożystane teraz ale może przydac się w dalszych zadaniach
    """
    if x == 1:
        return input
    if x== -1:
        return 1/input
    if x == 0:
        return 1
    if x<0:
        input = 1/input
        x=x*-1
    result = input
    while x>1:
        result = result * input
        x=x-1
        return result