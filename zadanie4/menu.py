from integrals import *

def menu():

    choseFun = ""
    choseEps = 0.0
    choseGrd = 0

    next = True

    print("")
    print("wybierz funkcje:")
    print("[A] -> x^2+7*x+100")
    print("[B] -> x^4-x^3-x^2-x+1")
    print("[C] -> cos(x)-x^3")
    print("[D] -> x^3-2*x+|x-5|")

    while next:
        choseFun = str(input("---> "))
        if choseFun not in ["A", "B", "C", "D", "E"]:
            print("niepoprawyn wybor")
        else:
            next = False

    next = True

    print("podaj stopień dla Gauss-Laugerre:")
    while next:
        while True:
            try:
                choseGrd = int(input("---> "))
                break
            except ValueError:
                print("niepoprawyn wybor [=/= int]")
        if choseGrd < 0 or choseGrd > 10:
            print("maksymalny stopień to 10, minimalny to 1")
        else:
            next = False
    next = True

    print("podaj przybliżenie dla Newton-Cotes:")
    while next:
        while True:
            try:
                choseEps = float(input("---> "))
                if choseEps > 0:
                    break
                print("niepoprawyn wybor [eps > 0]")
            except ValueError:
                print("niepoprawyn wybor [ =/= float]")
                print("przykladowe przylizenie: 0.0001")
        next = False

    if choseFun == "A":
        f = functionOne
    elif choseFun == "B":
        f = functionTwo
    elif choseFun == "C":
        f = functionThree
    else:
        f = functionFour

    a = Laguerre(f,choseGrd)
    b = newtonCotes(f,choseEps)

    print()
    print("Wyniki:")
    print("Gauss-Laugerre : " + str(round(a,5)))
    print("Newton-Cotes   : " + str(round(b,5)))
    print("różnica wyników: " + str(round(abs(a-b),5)))