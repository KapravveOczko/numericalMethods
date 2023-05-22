import numpy

def linealFunction(x):
    return 5*x-8

def absoluteFunction(x):
    x = abs(x)
    return 5*x-8

def polynomialFunction(x):
    return 2*x**3-5*x**2-3*x+6

def trigonometricFunction(x):
    return -3*numpy.sin(x)+6*numpy.cos(x)

def complexFunction(x):
    return -2*numpy.cos(x)-3*x**2+x**3

def horner(poly, x):
    result = poly[0]
    for i in range(1, len(poly)):
        result = result * x + poly[i]
    return result