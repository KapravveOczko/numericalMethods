from functions import *
from print import *
def menu():

    '''
    f = wybór funkcji
    start, end = kolejno początek i koniec przedziału dla interpolacji
    n = ilość węzłów
    :return:
    '''

    next = True

    print("")
    print("wybierz funkcje:")
    print("[A] -> 5*x-8")
    print("[B] -> 5*|x|-8")
    print("[C] -> 2*x^3-5*x^2-3*x+6")
    print("[D] -> -3*sin(x)+6*cos(x)")
    print("[E] -> 2*cos(x)-x*3-1")

    while next:
        f = str(input("---> "))
        if f not in ["A", "B", "C", "D", "E"]:
            print("niepoprawyn wybor")
        else:
            next = False
    next = True

    #///////////////////////////////

    print("")
    print("czy chcesz zobaczyć wykres funkcji?")
    print("wybierz: ")
    print("[A] -> tak")
    print("[B] -> nie")

    while next:
        show = str(input("---> "))
        if show not in ["A", "B"]:
            print("niepoprawyn wybor")
        else:
            next = False
    next = True

    if show == "A":
        plotFunction(getFunction(f), -100, 100)

    #//////////////////////////////

    print("")
    print("podaj przedział dla interpolacji")

    while next:
        while True:
            try:
                print("podaj początek przedziału")
                start = int(input("---> "))
                break
            except ValueError:
                print("niepoprawyn wybor [=/= int]")
        while True:
            try:
                print("podaj koniec przedziału")
                end = int(input("---> "))
                break
            except ValueError:
                print("niepoprawyn wybor [ =/= int]")
        if end > start:
            next = False
        else:
            print("niepoprawyn wybor [A>B]")
    next = True

    #//////////////////////////////

    print("")
    print("podaj ilość węzłów")

    while next:
        while True:
            try:
                n = int(input("---> "))
                break
            except ValueError:
                print("niepoprawyn wybor [ =/= int]")
        next = False
    next = True

    plotInterpolation(getFunction(f),start,end,n)

    return 0; #tmp

def getFunction(f):

    if f == "A":
        return linearFunction
    elif f == "B":
        return absoluteFunction
    elif f == "C":
        return polynomialFunction
    elif f == "D":
        return trigonometricFunction
    elif f == "E":
        return complexFunction