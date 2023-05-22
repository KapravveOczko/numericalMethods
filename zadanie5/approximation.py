import numpy as np
from scipy.special import hermite
from scipy.integrate import quad


def calculate_approximation(n, f, a, b, x_values):
    coefficients = calculate_hermite_coefficients(n, f, a, b)
    values = []

    for x in x_values:
        approximation = 0
        for i in range(n + 1):
            approximation += coefficients[i] * hermite(i)(x)
        values.append(approximation)

    return values


def calculate_hermite_coefficients(n, f, a, b):
    coefficients = []

    for i in range(n + 1):
        integrand = lambda x: f(x) * hermite(i)(x)
        numerator, _ = quad(integrand, a, b)
        denominator = calculate_hermite_norm(i, a, b)
        coefficients.append(numerator / denominator)

    return coefficients


def calculate_hermite_norm(k, a, b):
    integrand = lambda x: hermite(k)(x) ** 2
    norm, _ = quad(integrand, a, b)

    return norm
