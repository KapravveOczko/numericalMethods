from functions import *

print("hello world")

testMatrix = [[3, 3, 1], [2, 5, 7], [2, 3, 2]]
testMatrixSize = 3
testMatrixResult = [12, 33, 8]

printMatrix(testMatrix, testMatrixSize)
countMatrix(testMatrix,testMatrixSize,testMatrixResult,30)
gauss_seidel(testMatrix,testMatrixResult,[0,0,0],30)