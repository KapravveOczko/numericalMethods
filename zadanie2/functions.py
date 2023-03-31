def printMatrix(matrix, matrixSize):
    for i in range(matrixSize):
        print(matrix[i])

def countMatrix(matrix, matrixSize, testMatrixResult, iter):

    #matrix = macierz
    #matrixSize = wielkosc macierzy
    #i = ilosc iteracji
    #testMatrixResult = wartosci macierzy | moze by tak to połączyć z matrix ?

    output = [0] * matrixSize
    bufor = 0

    for i in range(iter):               #ilosc iteracji
        print ("i: " + str(i))
        for j in range(matrixSize):     #przejscie po wszystkich zmiennych
            print("j: " + str(j))


            for c in range(matrixSize):
                if 1 + c == matrixSize:
                    break
                bufor = bufor + matrix[j][c+1] * output[c+1]
                print ("bufor: " + str(bufor) + " = " + str(matrix[j][c+1]) + " * " + str(output[c+1]))



            output[j] = (testMatrixResult[j] - bufor)/matrix[j][0]



            bufor = 0

            #output[j] = (testMatrixResult[j] - matrix[j][1] * output[1+j] - matrix[j][2] * output[2+j])/matrix[j][0]
    print (output)
    return 0