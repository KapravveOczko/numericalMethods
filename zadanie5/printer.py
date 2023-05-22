import numpy as np
import matplotlib.pyplot as plt


def rysuj_wykres(x_aprox, y_aprox, x_base, y_base, ymin, ymax):

    plt.plot(x_base, y_base, color='red', label='Funkcja bazowa')
    plt.plot(x_aprox, y_aprox, color='blue', linestyle='dashed', label='Funkcja aproksymowana')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Wykres funkcji bazowej i aproksymowanej')
    plt.ylim(ymin, ymax)
    plt.legend()
    plt.grid(True)  # Dodanie linii siatki

    ax = plt.gca()  # Pobranie bieżącej osi

    # Pogrubienie linii osi x i y
    ax.axhline(0, color='black', linewidth=1.5)
    ax.axvline(0, color='black', linewidth=1.5)

    plt.show()