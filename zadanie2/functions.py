from filesOperactions import loadSamplesAnswers
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

    if iter == 0:
        method = 1
    else:
        method = 0

    answers = loadSamplesAnswers()

    output = [0] * matrixSize
    bufor = 0

    while method != iter:
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

            if iter!=0:
                method = method + 1


    print (output)

def determinant(matrix):

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
        print("badana macierz jest nieoznaczona lub sprzeczna")
        return 0
    else:
        return 1
