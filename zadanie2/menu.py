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
    testStop = ""

    print("program przedstawia metodę iteracyjną Gaussa-Seidla")
    print("")

    #wybór przykłądu
    while next:
        print("wybierz:")
        print("[a] -> przykłady z zadania")
        print("[b] -> własna macierz")
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


    print("podaj warunek stopu:")
    print("[a] -> ilość iteracji")
    print("[b] -> przybliżenie")

    while next:
        testStop = input("--> ")
        if testStop not in ["a", "b"]:
            print("niepoprawyn wybor")
        else:
            next = False
    next = True

    if testStop == "a":
        print("podaj ilosc iteracji")
        while next:
            while True:
                try:
                    iter = int(input("--> "))
                    next = False
                    eps=1e-3
                    break
                except ValueError:
                    print("niepoprawyn wybor [=/= int]")

    if testStop == "b":
        while True:
            try:
                eps = float(input("--> "))
                if eps > 0:
                    break
                print("niepoprawyn wybor [eps > 0]")
            except ValueError:
                print("niepoprawyn wybor [ =/= float]")
                print("przykladowe przylizenie: 0.01")

    #obliczenia
    print("przystępuje do pracy nad macierzą")

    test = checkDeterminant(matrix)
    if test != 0:
        functions.countMatrix(matrix,matrixSize,matrixSolution,iter,eps)