from lagrange import *
from print import *
from functions import *

print("hello world")


def exampleFunction(x):
    return np.sin(x)

plotInterpolation(exampleFunction, 0, 2*np.pi, 10)
plotFunction(absoluteFunction, -10, 10)