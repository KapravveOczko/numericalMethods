e = 2.7182818284585634
from numpy import cos
def functionOne(x):
    return x**2+7*x+100
def functionTwo(x):
    return x ** 4 - x ** 3 - x ** 2 - x + 1

def functionThree(x):
    return cos(x) - x**3

def functionFour(x):
    return x**3 - 2 * x + abs(x - 5)


"""
=======================================================================
"""

def simpson(a, b, f):
    return (e**(- a) * f(a)+ 4 * e**(- (a + b) / 2) * f(((a + b) / 2)) + e**(- b) * f(b)) * (b - a) / 2 / 3

def extendedSimpsona(a, b, f, eps):

    result = simpson(a, b, f)
    n = 2

    while 1:

        newResult = 0
        h = (b - a) / (2 * n)
        newA = a
        newB = newA + 2 * h

        for i in range(n):
            i = simpson(newA, newB, f)
            newResult += i
            newA = newB
            newB += 2 * h
        if abs(newResult - result) < eps:
            result = newResult
            break
        else:
            result = newResult
            n += 1

    return result


def newtonCotes(f, eps):
    a = 0
    delta = 1
    sum = 0

    while 1:
        result = extendedSimpsona(a, a + delta, f, eps)
        sum += result
        a += delta
        if abs(result) <= abs(eps):
            break
    return sum


"""
=======================================================================
"""

def Laguerre(f,grade):
    result = 0
    xi = xiLib[grade]
    wi = wiLib[grade]

    for i in range(grade):
        result += wi[i] * f(xi[i])
    return result


xiLib = {
  1:  [1.0],
  2:  [0.585786, 3.41421],
  3:  [0.415775, 2.29428, 6.28995],
  4:  [0.322548, 1.74576, 4.53662, 9.39507],
  5:  [ 0.26356,  1.4134,  3.59643, 7.08581, 12.6408],
  6:  [0.222847, 1.18893, 2.99274, 5.77514, 9.83747, 15.9829],
  7:  [0.193043, 1.02656, 2.56788, 4.90035, 8.18216, 12.7348, 19.3957],
  8:  [0.170279, 0.903701, 2.25109, 4.2667, 7.04591, 10.7585, 15.7407, 22.8636],
  9:  [0.152322, 0.807204, 2.00513, 3.78377, 6.20496, 9.37298, 13.4662, 18.8336, 26.3741],
 10:  [0.137793, 0.729454, 1.80834, 3.40143, 5.5525, 8.33015, 11.8436, 16.2793, 21.9966, 29.9205]
}

wiLib = {
  1:  [1.0],
  2:  [0.853553, 0.146447],
  3:  [0.711093, 0.278518, 0.0103893],
  4:  [0.603155, 0.357419, 0.0388879, 0.000539295],
  5:  [0.521756, 0.398667, 0.0759424, 0.00361176, 2.33699e-05],
  6:  [0.458964, 0.417001, 0.113373, 0.0103992, 0.000261017, 1.67955e-07],
  7:  [0.404831, 0.391724, 0.136872, 0.0255174, 0.00214697, 7.51582e-05, 7.6472e-08],
  8:  [0.358526, 0.359079, 0.157448, 0.0330415, 0.00393068, 0.000233581, 5.74621e-06, 2.70992e-08],
  9:  [0.318204, 0.32737, 0.177211, 0.0474494, 0.00760734, 0.000764767, 4.22512e-05, 1.04669e-06, 6.33286e-09],
 10:  [0.287828, 0.308459, 0.176999, 0.059448, 0.0129531, 0.00180144, 0.000157379, 8.42404e-06, 1.98145e-07, 1.19217e-09]
}