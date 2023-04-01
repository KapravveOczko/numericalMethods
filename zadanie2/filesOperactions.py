import numpy

def loadMatrix(filePathMatrix,filePathMatrixSolution):


    data = numpy.loadtxt(filePathMatrix, delimiter=',')
    matrix = numpy.array(data)
    dataS = numpy.loadtxt(filePathMatrixSolution, delimiter=',')
    matrixSolution = dataS
    matrixSize=matrix.shape[1]

    # print(matrix)
    # print(matrixSize)
    # print(matrixSolution)

    return matrix,matrixSize,matrixSolution

def getMatrixToLoad():
    matrixPath = input("podaj nazwe pliku: ") + ".txt"
    matrixSolutionPath = "S" + matrixPath
    matrixPath = "./przyklady/" + matrixPath
    matrixSolutionPath = "./przyklady/" + matrixSolutionPath

    print(matrixPath)
    print(matrixSolutionPath)

    return matrixPath, matrixSolutionPath