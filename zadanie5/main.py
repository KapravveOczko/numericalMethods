from approximation import *
import numpy as np

print("hello world")

# Definicja funkcji aproksymowanej
def f(x):
    return x**3 + 2*x**2 - x + 1

# Parametry aproksymacji
n = 5
a = -10
b = 10
xValues = np.linspace(a, b, 10)

# Obliczanie aproksymacji
approximation = calculate_approximation(n, f, a, b, xValues)

# Wyświetlanie wyników
for i in range(len(xValues)):
    print("x =", xValues[i], ", f(x) =", f(xValues[i]), ", approximation =", approximation[i])
