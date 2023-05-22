import numpy

"""
przykładowe funkcje do wybrania przez użytkownika
funkcje wpisane są na sztywno
zmiana funkcji wielomianowej wymaga ręcznego zmienienia wartości polly w menu
"""

def polynomialFunction(x):
    return 2*x**3-5*x**2-3*x+6

def trigonometricFunction(x):
    return -3*numpy.sin(x)+6*numpy.cos(x)

def exponentialFunction(x):
    return 5**x-2**x-2

def complexFunction(x):
    return -2*numpy.cos(x)-x**3+x**2-1

"""
funkcje do ustalenia którą funkcję wybrał user
"""

def getValue(choise, x, polly):
    if (choise == 1):
        return horner(polly,x)
    if (choise == 2):
        return trigonometricFunction(x)
    if (choise == 3):
        return exponentialFunction(x)
    if (choise == 4):
        return complexFunction(x)


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

def isContinuous(f, a, b, polly, eps=1e-6):
    """
    Sprawdza, czy funkcja `f` jest ciągła na przedziale [a,b].
    zwraca true jesli funkcja jest ciągła
    """
    x = a
    while x <= b:
        y1 = getValue(f, x, polly)
        y2 = getValue(f, x+eps, polly)
        if abs(y1 - y2) > eps:
            return False
        x += eps
    return True

def nearZero(value, eps=1e-6):
    """
     Sprawdza, czy wartość value jest bliska 0
     true w przypadku w którym tak jest
     """
    if -1*eps<value and value<eps:
        return True
    return False

def checkMarks(a, c):
    """
     funkcja zwraca true jeśli a i c mają przeciwne znaki
     """
    if a * c < 0:
        return True
    else:
        return False
