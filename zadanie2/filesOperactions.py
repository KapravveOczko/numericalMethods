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

    print("przystępuje do ładowania przykładu:")
    print(matrixPath)
    print(matrixSolutionPath)
    print("ładowanie zakończone")

    return matrixPath, matrixSolutionPath

def getSampleToLoad(sample):
    matrixPath = sample + ".txt"
    matrixSolutionPath = "S" + matrixPath
    matrixPath = "./przyklady/" + matrixPath
    matrixSolutionPath = "./przyklady/" + matrixSolutionPath

    print("przystępuje do ładowania przykładu:")
    print(matrixPath)
    print(matrixSolutionPath)
    print("ładowanie zakończone")

    return matrixPath, matrixSolutionPath