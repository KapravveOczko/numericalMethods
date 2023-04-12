import numpy
def lagrangePolynomialinternal(x, n, i, tabX):
    """
    funkcja wyznacza wartość L (wielomian bazowy)
    :param tabX: tablica wartości X
    :param x: wartość zmiennej x
    :param n: ilość iteracji
    :param i: numer iteracji z wielomianu
    :return: wartość L z uwzglęnieniem zmiennej x
    """
    counter = 1
    denominator = 1
    for j in range(n):
        if j != i:
            counter *= (x - tabX[j])
            denominator *= (tabX[i] - tabX[j])
    return (counter / denominator)

def lagrangePolynomial(x, n, a, b, y):
    """
    funkcja wyznacza wartość wielomianu interpolacyjnego
    :param x: wartość zmiennej x
    :param n: ilość węzłów interpolacji
    :param a: początek przedziału interpolacji
    :param b: koniec przedziału interpolacji
    :param y: tablica wartości funkcji y dla węzłów interpolacji
    :return: wartość wielomianu interpolacyjnego dla zmiennej x
    """
    tabX = numpy.linspace(a, b, n) # wyznaczenie węzłów równoległych
    polymonial = 0
    for i in range(n):
        L = 1
        for j in range(n):
            if j != i:
                L *= (x - tabX[j]) / (tabX[i] - tabX[j])
        polymonial += y[i] * L
    return polymonial