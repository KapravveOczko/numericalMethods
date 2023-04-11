import numpy as np
import matplotlib.pyplot as plt
from lagrange import *

def plotInterpolation(f, a, b, n):
    """
    funkcja rysuje wykres funkcji i wykres interpolowany
    :param f: funkcja do interpolacji
    :param a: początek przedziału interpolacji
    :param b: koniec przedziału interpolacji
    :param n: liczba węzłów interpolacji
    """

    x = np.linspace(a, b, 1000)         # 1000 punktów na wykresie
    y = f(x)                            # wartości funkcji dla tych punktów
    fig, ax = plt.subplots()            # tworzymy obiekt figury i osi
    ax.plot(x, y, label='funkcja')      # rysujemy wykres funkcji

    tabX = np.linspace(a, b, n)         # wyznaczamy węzły interpolacji
    tabY = f(tabX)                      # wartości funkcji dla węzłów interpolacji
    xi = np.linspace(a, b, 1000)        # punkty dla interpolacji
    yi = np.zeros_like(xi)              # wartości interpolowane

    for i in range(1000):
        yi[i] = lagrangePolynomial(xi[i], n, a, b, tabY)                        # obliczamy wartości interpolowane
    ax.plot(xi, yi, label='interpolacja')                                       # rysujemy wykres interpolowany
    ax.scatter(tabX, tabY, label='węzły interpolacji', color='red')             # rysujemy węzły interpolacji

    ax.legend()          # dodajemy legendę
    plt.show()           # wyświetlamy wykresy

def plotFunction(func, start, end):
    x = np.linspace(start, end, 1000)
    y = func(x)
    plt.plot(x, y, color='b')
    plt.show()
