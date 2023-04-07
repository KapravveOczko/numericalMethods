def LagrangePolynomial(x, n, i):
    counter = 1
    denominator = 1
    '''wyznaczenie wartości pojedyńczego L'''
    for j in range(n+1):
        if j != i:
            counter *= (x - j)
            denominator *= (i - j)
    return (counter / denominator)

def LagrangePolynomial():

    return 0