from bisection import *
from secantMethod import *
from printer import *

"""
funkcja zbiera input od usera i przekazuje go do funkcji processMenu()
odporna jest (mam nadzieję) na wszystkie próby jej zepsucia
"""

def showMenu():
    next = True
    choseFunction = 0
    # choseMetod = 0
    choseCondition = 0
    choseA = 0 # początek przedziału
    choseB = 0 # koniec przedziału
    choseIter = 0 # ilość iteracji | w przypadku wybrania opcji B ustawiona na 0 i przekazana dalej
    choseEps = 1e-6 # dokładność

    print("wybierz funkcje:")
    print("[A] - 2x^3-5x^2-3x+6")
    print("[B] - -3sin(x)+6cos(x)")
    print("[C] - 5^x-2^x-2")
    print("[D] -2cos(x)-x^3+x^2-1")

    while next:
        choseFunction = str(input("twoj wybor: "))
        if choseFunction not in ["A", "B", "C", "D"]:
            print("niepoprawyn wybor")
        else:
            next = False

    # next = True
    # print("wybierz metode:")
    # print("[A] - bisekcja")
    # print("[B] - siecznych")
    #
    # while next:
    #     choseMetod = input("twoj wybor: ")
    #     if choseMetod not in ["A", "B"]:
    #         print("niepoprawyn wybor")
    #     else:
    #         next = False

    if choseFunction == "A":
        choseFunction = 1
    elif choseFunction == "B":
        choseFunction = 2
    elif choseFunction == "C":
        choseFunction = 3
    elif choseFunction == "D":
        choseFunction = 4

    drawSimplePlot(choseFunction, [2, -5, -3, 6])

    print("wyboerz początek i koniec przedziału: ")
    next = True
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
    print("wybierz warunek:")
    print("[A] - ilość iteracji")
    print("[B] - przybliżenie")

    while next:
        choseCondition = input("twoj wybor: ")
        if choseCondition not in ["A", "B"]:
            print("niepoprawyn wybor")
        else:
            next = False

    if choseCondition == "A":
            while True:
                try:
                    choseIter = int(input("ilość iteracji: "))
                    if choseIter > 0:
                        choseEps = 1e-6
                        break
                    print("niepoprawyn wybor [iter > 0]")
                except ValueError:
                    print("niepoprawyn wybor [ =/= int]")
    if choseCondition == "B":
        choseIter = 0
        while True:
            try:
                choseEps = float(input("przyblizenie: "))
                if choseEps > 0:
                    break
                print("niepoprawyn wybor [eps > 0]")
            except ValueError:
                print("niepoprawyn wybor [ =/= float]")
                print("przykladowe przylizenie: 0.0001")

    processMenu( choseFunction, choseA, choseB, choseIter, choseEps)


def processMenu( choseFunction, choseA, choseB, choseIter, choseEps):


    """

    ma zazadanie obsłużyć wybory usera z poprzedniej funkcji oraz przekazać wynik dalej

    funkcja przyjmuje:

     -> choseFunction: wybór funkcji
     -> choseMetod: wybór metody
     -> choseA: początek przedziału
     -> choseB: koniec przedziału
     -> choseIter: ilość iteracji
     -> choseEps: dokładność

    funkcja zwraca:

    -> przekazuje miejsce zerowe do funkcji rysującej wykres
    -> jesli nie możliwe jest znalezienie miejsca 0, zwraca kod błędu
    """


    # przetworzenie wyboru funkcji na zrozumiały dla funkcji getValue
    # narusza zasadę DRY ale działa


    polly = [2, -5, -3, 6] # jedyne miejsce gdzie trzeba zmienic polly przy zmianie funkcji wielomianowej (A)

    # if choseMetod == "A":
    #     try:
    #         x0 = calculateBisection(choseFunction, choseA, choseB, polly,choseIter, choseEps)
    #         x0 = float(x0)
    #         drawPlot(choseFunction, choseA, choseB, polly, x0, choseEps)
    #     except ValueError:
    #         print(x0)
    #
    # elif choseMetod =="B":
    #
    #     try:
    #         x0 = calculateSecantMethod(choseFunction, choseA, choseB, polly,choseIter, choseEps)
    #         x0 = float(x0)
    #         drawPlot(choseFunction, choseA, choseB, polly, x0, choseEps)
    #     except ValueError:
    #         print(x0)


    try:
        x0b = calculateBisection(choseFunction, choseA, choseB, polly,choseIter, choseEps)
        x0b = float(x0b)
        x0s = calculateSecantMethod(choseFunction, choseA, choseB, polly,choseIter, choseEps)
        x0s = float(x0s)
        drawPlot(choseFunction, choseA, choseB, polly, x0b,x0s, choseEps)
    except ValueError:
        print(x0b)
        print(x0s)

    return 0