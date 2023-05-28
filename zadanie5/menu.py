from approximation import *
from printer import *
from functions import *
def menu():
    next = True
    choseA = -2
    choseB = 2
    nodes = 0

    print("wybierz funkcje:")
    print("[A] - 5x-8")
    print("[B] - |5x|-8")
    print("[C] - 2x^3-5x^2-3x+6")
    print("[D] - -3sin(x)+6cos(x)")
    print("[E] - -2cos(x)-3x^2+x^3")

    while next:
        choseFunction = str(input("twoj wybor: "))
        if choseFunction not in ["A", "B", "C", "D", "E"]:
            print("niepoprawyn wybor")
        else:
            next = False


    next = True
    print("wyboerz początek i koniec przedziału: ")
    while next:
        while True:
            try:
                choseA = int(input("początek przedziału: "))
                break
            except ValueError:
                print("niepoprawyn wybor [=/= int]")
        while True:
            try:
                choseB = int(input("koniec przedziału: "))
                break
            except ValueError:
                print("niepoprawyn wybor [ =/= int]")
        if choseB > choseA:
            next = False
        else:
            print("niepoprawyn wybor [A>B]")

    next = True
    print("podaj ilosc wezlow")
    while True:
        try:
            nodes = int(input("twoj wybor: "))
            if nodes > 0:
                break
            print("niepoprawyn wybor [nodes > 0]")
        except ValueError:
            print("niepoprawyn wybor [ =/= int]")

    next = True
    print("podaj stopien wielomianu")
    while True:
        try:
            grade = int(input("twoj wybor: "))
            if grade > 0:
                break
            print("niepoprawyn wybor [grade > 0]")
            if grade < 10:
                print("niepoprawyn wybor [grade max == 10]")
        except ValueError:
            print("niepoprawyn wybor [ =/= int]")


    if choseFunction == "A":
        f = linealFunction
    elif choseFunction == "B":
        f = absoluteFunction
    elif choseFunction == "C":
        f = polynomialFunction
    elif choseFunction == "D":
        f = trigonometricFunction
    elif choseFunction == "E":
        f = complexFunction


    xValues = np.linspace(choseA, choseB, nodes)
    approximation = calculate_approximation(grade, f, choseA, choseB, xValues)
    fApro = []
    fBaze = []
    xBazeValues = np.linspace(choseA, choseB, 100)

    print()
    for i in range(len(xValues)):
        fi = f(xValues[i])
        fa = approximation[i]
        print("x =", xValues[i], ", f(x) =", fi, ", approximation =", fa)
        fApro.append(fa)

    for i in range(len(xBazeValues)):
        fi = f(xBazeValues[i])
        # print(fi)
        fBaze.append(fi)

    rysuj_wykres(xValues, fApro, xBazeValues, fBaze, -5, 10)

    return 0