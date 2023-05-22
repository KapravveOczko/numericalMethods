from functions import *

"""
    Algorytm metody bisekcji można opisać następująco:

#0.0  Wybieramy przedział [a, b], w którym szukamy rozwiązania lub wartości funkcji.
#0.1  sprawdzamy czy  funkcja f(x) jest ciągła w przedziale domkniętym [a;b],
#0.2 sprawdzamy czy funkcja przyjmuje różne znaki na krańcach przedziału.

#1  Sprawdzamy wartość funkcji w punkcie środkowym przedziału c=(a+b)/2.
#2  Jeśli wartość funkcji w punkcie c jest dostatecznie bliska zeru, to kończymy działanie algorytmu i zwracamy punkt c jako rozwiązanie.
#3  W przeciwnym razie wybieramy przedział 
    [a, c], jeśli wartość funkcji w punkcie c ma znak przeciwny do wartości w punkcie a, lub przedział 
    [c, b], jeśli wartość funkcji w punkcie c ma znak przeciwny do wartości w punkcie b.
#4  Powtarzamy kroki 2-4, aż wartość funkcji w punkcie środkowym przedziału będzie dostatecznie bliska zeru.

cpłosć testowana jest na: 5*x^3+2*x^2-x+5
oraz na skończonej ilości iteracji: 30


funkcja przyjmuje:

f -> wybór usera, którą funkcję rozpatrujemy
a -> początek przedziału
b -> koniec przedziału
i -> ilość iteracji podana przez usera
polly -> specjalnie dla wielomianu, wartości potęg, potrzebne tylko do hornera
eps -> dokładność


funkcja zwraca:

-> miejsce 0 w przypadku jego znalezienia
-> informację o tym że operacja się nie powiodła

  print("----------------")
        print(iterations)
        print("c: " + str(c))
        print("a: " + str(a))
        print("b: " + str(b))
        print("f(c): " + str(getValue(f, c ,polly)))
        print("f(a): " + str(getValue(f, a ,polly)))
        print("f(b): " + str(getValue(f, b ,polly)))
        

"""

def calculateBisection(f, a, b, polly, i, eps):
    if checkMarks(getValue(f, b ,polly), getValue(f, a ,polly)) == False:
        return "w podanym przedziale funkcja ma takie same znaki, niemożliwe jest zastosowanie metody"
    if isContinuous(f, a, b, polly) == True:
        return "funkcja nie jest ciągła, niemożliwe jest zastosowanie metody"
    return bisection(f, a, b, polly, i,eps)



def bisection(f, a, b, polly, i, eps):

    if i == 0:
        iterations = 1
    else:
        iterations = 0
    """#4"""
    powt =0

    while (iterations != i):
        """#1"""
        c = (a + b) / 2
        value = getValue(f, c ,polly)
        """#2"""
        if nearZero(value, eps):
            print(powt)
            return c
        else:
            """#3"""
            if checkMarks(getValue(f, c ,polly), getValue(f, a ,polly)):
                b = c
            if checkMarks(getValue(f, c ,polly), getValue(f, b ,polly)):
                a = c
        powt = powt +1
        if i!=0:
            iterations = iterations + 1

    return "nie udało się znaleźć miejsca zerowego"
