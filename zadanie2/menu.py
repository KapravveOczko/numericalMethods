import filesOperactions
import functions
from functions import *
from filesOperactions import *

def menu():

    next = True
    testChoice = ""
    test = ""
    validSamples = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j"}
    iter = 0

    print("program przedstawia metodę iteracyjną Gaussa-Seidla")
    print("")

    #wybór przykłądu
    while next:
        print("wybierz:")
        print("a -> przykłady z zadania")
        print("b -> własna macierz")
        testChoice = input("--> ")
        if testChoice not in ["a", "b"]:
            print("niepoprawyn wybor")
        else:
            next = False
    next = True

    #wybór przykładu dla macierzy z zadania
    if testChoice == "a":
        while next:
            print("wybierz przykład [a-j]")
            test = input("--> ")
            if test not in validSamples:
                print("niepoprawyn wybor")
            else:
                a, b = filesOperactions.getSampleToLoad(test)
                matrix, matrixSize, matrixSolution = filesOperactions.loadMatrix(a,b)
                next = False
    next = True

    #wybór pliku dla macierzy własnej
    if testChoice == "b":
        a, b = filesOperactions.getMatrixToLoad()
        matrix, matrixSize, matrixSolution = filesOperactions.loadMatrix(a,b)
    next = True

    print("podaj ilosc iteracji")
    while next:
        while True:
            try:
                iter = int(input("--> "))
                next = False
                break
            except ValueError:
                print("niepoprawyn wybor [=/= int]")

    #obliczenia
    print("przystępuje do pracy nad macierzą")

    test = checkDeterminant(matrix)
    if test != 0:
        functions.countMatrix(matrix,matrixSize,matrixSolution,iter)