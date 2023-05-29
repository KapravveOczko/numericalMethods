import numpy as np
from aproximaction import *

# Przykładowa funkcja do aproksymacji
def my_function(x):
    return np.cos(2*x**2+1)

# Ilość węzłów, stopień wielomianów Hermite'a, początek i koniec przedziału
num_nodes = 5
degree = 3
a = -1
b = 1

# Generowanie losowych węzłów
nodes = np.random.uniform(a, b, size=(num_nodes, 2))
nodes[:, 1] = my_function(nodes[:, 0])

# Aproksymacja
hermite_approximation(nodes, degree, my_function, a, b)
