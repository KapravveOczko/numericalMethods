import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from numpy.polynomial.hermite import hermval

def hermite_approximation(nodes, degree, function, a, b):
    def objective(coefficients):
        x_values = nodes[:, 0]
        y_values = nodes[:, 1]
        approximated_function = np.sum([hermval((x_values-a)/(b-a), [0] + list(coefficients[degree*i:degree*(i+1)])) for i in range(len(x_values))], axis=0)
        return np.sum((approximated_function - y_values) ** 2)

    # Początkowe wartości współczynników
    initial_coefficients = np.zeros(degree * len(nodes))

    # Optymalizacja współczynników przy użyciu metody najmniejszych kwadratów
    result = minimize(objective, initial_coefficients)

    # Ostateczne współczynniki aproksymacji
    final_coefficients = result.x

    # Wartości x dla aproksymacji
    x_values = np.linspace(a, b, 100)

    # Wartości y dla aproksymacji
    approximated_function = np.sum([hermval((x_values-a)/(b-a), [0] + list(final_coefficients[degree*i:degree*(i+1)])) for i in range(len(x_values))], axis=0)

    # Wyświetlanie wyników
    print("x, f(x), wynik aproksymacji, różnica między aproksymacją a funkcją:")
    for i in range(len(x_values)):
        f_x = function(x_values[i])
        approx_value = approximated_function[i]
        diff = approx_value - f_x
        print(f"{x_values[i]:.2f}, {f_x:.2f}, {approx_value:.2f}, {diff:.2f}")

    # Wykres
    plt.figure()
    plt.plot(x_values, function(x_values), label='Funkcja oryginalna')
    plt.plot(x_values, approximated_function, label='Aproksymacja')
    plt.scatter(nodes[:, 0], nodes[:, 1], color='red', label='Węzły')
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Aproksymacja za pomocą węzłów Hermitea')
    plt.show()
