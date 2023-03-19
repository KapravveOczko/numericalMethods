import matplotlib.pyplot as plt
from functions import *

def drawPlot(f,a,b,polly,x0,eps):

    """
    funkcja rysuje wykres jeśli znalezione zostało miejsce 0

    f -  wybór funkcji
    a, b - przedział rozważany
    x0 - miejsce zerwoe

    """

    print("poszukiwane miejsce zerowe: " + str(x0))

    # Tworzenie danych do wykresu
    x = numpy.linspace(a, b, 100)  # rozpiętość osi x i ilość punktów
    y = getValue(f,x,polly)

    # Rysowanie wykresu
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.axhline(0, color='gray', linewidth=0.5)
    ax.axvline(0, color='gray', linewidth=0.5)
    ax.set_xlabel('x')
    ax.set_ylabel('y')

    ax.plot(x0, getValue(f,x0,polly), 'o')

    ax.set_ylim(-1*abs(getValue(f,a,polly)), abs(getValue(f,b,polly))) # zasadniczo działa ale miewa problemy

    # dostosowanie tytułu dla poszczegulnych wykresów
    if f==1:
        plt.title('Wykres funkcji 2x^3-5x^2-3x+6')
    elif f==2:
        plt.title('Wykres funkcji -3sin(x)+6cos(x)')
    elif f==3:
        plt.title('Wykres funkcji 5^x-2^x-2')
    elif f==4:
        plt.title('Wykres funkcji -2cos(x)-x^3+x^2-1')

    plt.show()