def printMatrix(matrix, matrixSize):
    for i in range(matrixSize):
        print(matrix[i])

def countMatrix(matrix, matrixSize, testMatrixSolution, iter):
    """
    matrix = macierz
    matrixSize = wielkosc macierzy
    i = ilosc iteracji
    testMatrixResult = wartosci macierzy | moze by tak to połączyć z matrix ?
    """

    output = [0] * matrixSize
    bufor = 0

    for i in range(iter):               #ilosc iteracji
        """
        print(output)
        print ("i: " + str(i))
        """
        for j in range(matrixSize):     #przejscie po wszystkich zmiennych
            """
            print("j: " + str(j))
            """
            for c in range(matrixSize): #przelatuje po wszystkich bufforach
                if c ==j:               #z pominięciej obliczanej
                    continue
                bufor = bufor + matrix[j][c] * output[c]
                """
                print ("bufor: " + str(bufor) + " = " + str(matrix[j][c]) + " * " + str(output[c]))
                """
            output[j] = (testMatrixSolution[j] - bufor) / matrix[j][j]
            """
            print ("output = (" + str(testMatrixResult[j]) + " - " + str(bufor) + ") / " + str(matrix[j][j]))
            """
            bufor = 0
    print (output)
    return 0

#by chatGPT
def gauss_seidel(A, b, x0, max_iter):
    """
    Metoda iteracyjna Gaussa-Seidla do rozwiązywania układów równań liniowych Ax = b.

    :param A: macierz współczynników
    :param b: wektor prawych stron
    :param x0: wektor początkowy
    :param max_iter: maksymalna liczba iteracji
    :param tol: tolerancja
    :return: wektor x będący rozwiązaniem układu równań
    """
    n = len(b)
    x = x0.copy()
    for k in range(max_iter):
        for i in range(n):
            s = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x[i] = (b[i] - s) / A[i][i]
    print(x)
    return x

def determinant(matrix):        #NOT TESTED

    n = len(matrix)

    # definicja warunku stopu
    if n == 1:
        return matrix[0][0]

    # wyznaczenie wyznacznika rekurencyjnie
    det = 0
    sign = 1
    for i in range(n):
        # wyznaczanie podmacierzy
        submatrix = []
        for j in range(1, n):
            row = []
            for k in range(n):
                if k != i:
                    row.append(matrix[j][k])
            submatrix.append(row)
        # wywołanie rekurencyjne dla podmacierzy
        det += sign * matrix[0][i] * determinant(submatrix)
        sign *= -1

    return det

def checkDeterminant(matrix):
    if determinant(matrix) == 0:
        print("hyba cie pojebalo")
    else:
        print("przystepuje do pracy nad macierza")
