def lagrangePolynomialinternal(x, n, i, tabX):
    """
    wyznacza wartość L (wielomian bazowy)
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

def lagrangePolynomial(x,n,tabX,tabY):
    """
    funkcja wyznacza wartość wielomianu interpolacyjnego
    :param x: wartość zmiennej x
    :param n: ilość iteracji
    :param tabX:
    :param tabY:
    :return: wartość wielomianu interpolacyjnego dla zmiennej x
    """
    polymonial = 0
    for i in range(n):
        polymonial += tabY[i]*lagrangePolynomialinternal(x,n,i,tabX)
    return polymonial