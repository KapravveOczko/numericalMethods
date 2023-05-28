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

# from scipy.special import hermite
# import numpy as np

#
# def calculate_approximation(n, f, a, b, x_values):
#     coefficients = calculate_hermite_coefficients(n, f, a, b)
#     values = []
#
#     for x in x_values:
#         approximation = 0
#         for i in range(n + 1):
#             approximation += coefficients[i] * hermite_poly(i, x)
#         values.append(approximation)
#
#     return values
#
#
# def calculate_hermite_coefficients(n, f, a, b):
#     coefficients = []
#
#     for i in range(n + 1):
#         integrand = lambda x: f(x) * hermite_poly(i, x)
#         numerator = Laguerre(integrand, grade=10)
#         denominator = calculate_hermite_norm(i, a, b)
#         coefficients.append(numerator / denominator)
#
#     return coefficients
#
#
# def calculate_hermite_norm(k, a, b):
#     integrand = lambda x: hermite_poly(k, x) ** 2
#     norm = Laguerre(integrand, grade=10)
#
#     return norm
#
#
# def Laguerre(f, grade=10):
#     result = 0
#     xi = xiLib[grade]
#     wi = wiLib[grade]
#
#     for i in range(grade):
#         result += wi[i] * f(xi[i])
#     return result
#
#
# def hermite_poly(n, x):
#     if n == 0:
#         return 1
#     elif n == 1:
#         return 2 * x
#     else:
#         return 2 * x * hermite_poly(n - 1, x) - 2 * (n - 1) * hermite_poly(n - 2, x)
#
#
# xiLib = {
#   1:  [1.0],
#   2:  [0.585786, 3.41421],
#   3:  [0.415775, 2.29428, 6.28995],
#   4:  [0.322548, 1.74576, 4.53662, 9.39507],
#   5:  [0.26356,  1.4134,  3.59643, 7.08581, 12.6408],
#   6:  [0.222847, 1.18893, 2.99274, 5.77514, 9.83747, 15.9829],
#   7:  [0.193043, 1.02656, 2.56788, 4.90035, 8.18216, 12.7348, 19.3957],
#   8:  [0.170279, 0.903701, 2.25109, 4.2667, 7.04591, 10.7585, 15.7407, 22.8636],
#   9:  [0.152322, 0.807204, 2.00513, 3.78377, 6.20496, 9.37298, 13.4662, 18.8336, 26.3741],
#  10:  [0.137793, 0.729454, 1.80834, 3.40143, 5.5525, 8.33015, 11.8436, 16.2793, 21.9966, 29.9205]
# }
#
# wiLib = {
#   1:  [1.0],
#   2:  [0.853553, 0.146447],
#   3:  [0.711093, 0.278518, 0.0103893],
#   4:  [0.603155, 0.357419, 0.0388879, 0.000539295],
#   5:  [0.521756, 0.398667, 0.0759424, 0.00361176, 2.33699e-05],
#   6:  [0.458964, 0.417001, 0.113373, 0.0103992, 0.000261017, 1.67955e-07],
#   7:  [0.404831, 0.391724, 0.136872, 0.0255174, 0.00214697, 7.51582e-05, 7.6472e-08],
#   8:  [0.358526, 0.359079, 0.157448, 0.0330415, 0.00393068, 0.000233581, 5.74621e-06, 2.70992e-08],
#   9:  [0.318204, 0.32737, 0.177211, 0.0474494, 0.00760734, 0.000764767, 4.22512e-05, 1.04669e-06, 6.33286e-09],
#  10:  [0.287828, 0.308459, 0.176999, 0.059448, 0.0129531, 0.00180144, 0.000157379, 8.42404e-06, 1.98145e-07, 1.19217e-09]
# }