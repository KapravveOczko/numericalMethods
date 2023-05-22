from approximation import *
import numpy as np
from printer import *

print("hello world")

# Definicja funkcji aproksymowanej
def f(x):
    return 2*x**2+x-2

# Parametry aproksymacji
n = 2
a = -2
b = 2
xValues = np.linspace(a, b, 3)

# Obliczanie aproksymacji
approximation = calculate_approximation(n, f, a, b, xValues)

fBaze = []
xBazeValues = np.linspace(a, b, 20)
fApro = []

# Wyświetlanie wyników
for i in range(len(xValues)):
    fi = f(xValues[i])
    fa = approximation[i]
    print("x =", xValues[i], ", f(x) =", fi, ", approximation =", fa)
    fApro.append(fa)

for i in range(len(xBazeValues)):
    fi = f(xBazeValues[i])
    print(fi)
    fBaze.append(fi)


rysuj_wykres(xValues,fApro,xBazeValues,fBaze,-5,10)