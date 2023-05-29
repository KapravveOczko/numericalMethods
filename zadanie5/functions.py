import numpy

def linealFunction(x):
    return 5*x-8

def absoluteFunction(x):
    x = abs(x)
    return 5*x-8
    # return x
def polynomialFunction(x):
    return 2*x**3-5*x**2-3*x+6
    # return 2*x**2+x-2
def trigonometricFunction(x):
    return -3*numpy.sin(x)+6*numpy.cos(x)
    # return numpy.sin(x)
def complexFunction(x):
    return -2*numpy.cos(x)-3*x**2+x**3
    # return numpy.cos(2*x**2+1)

def horner(poly, x):
    result = poly[0]
    for i in range(1, len(poly)):
        result = result * x + poly[i]
    return result