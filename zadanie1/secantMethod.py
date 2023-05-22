from functions import *

"""
Aby zastosować metodę siecznych, należy wykonać następujące kroki:

#0 warunki konieczne są tożsame z tymi do bisekcji
    wyliczone są równierz w ten sam sposób

#1 Wybrać dwa punkty początkowe x0 i x1, takie że f(x0) * f(x1) < 0, czyli funkcja ma różne znaki w tych punktach.
#2 Obliczyć wartości funkcji w tych punktach: f(x0) i f(x1).
#3 Wyznaczyć kolejny punkt na siecznej przechodzącej przez punkty x0 i x1, korzystając ze wzoru:
    x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
#4 Obliczyć wartość funkcji w punkcie x2: f(x2).
#5 Przesunąć punkty x0 i x1 o jeden krok w kierunku miejsca zerowego, tj. przypisać x1 wartość x2, a x2 wartość x1.
#6 Jeśli f(x2) jest dostatecznie blisko zera, czyli |f(x2)| < epsilon, 
#7 W przeciwnym razie, powtarzać kroki 3-6 aż do znalezienia wartości dostatecznie bliskiej zeru.



funkcja przyjmuje:

f -> wybór usera, którą funkcję rozpatrujemy
x0 -> początek przedziału
x1 -> koniec przedziału
i -> ilość iteracji podana przez usera
polly -> specjalnie dla wielomianu, wartości potęg, potrzebne tylko do hornera 
eps -> dokładność


funkcja zwraca:

-> miejsce 0 w przypadku jego znalezienia
-> informację o tym że operacja się nie powiodła
-> informacje o niemożliwości dizlenia przez 0 w przypadku kiedy funkcja natrafi na taki problem

"""

def calculateSecantMethod(f, a, b, polly, i,eps):
    if checkMarks(getValue(f, b ,polly), getValue(f, a ,polly)) == False:
        return "w podanym przedziale funkcja ma takie same znaki, niemożliwe jest zastosowanie metody"
    if isContinuous(f, a, b, polly) == True:
        return "funkcja nie jest ciągła, niemożliwe jest zastosowanie metody"
    return secantMethod(f,a,b,polly,i,eps)


def secantMethod(f, x0, x1, polly, max_iter, eps):


    if max_iter == 0:
        iterations = 1
    else:
        iterations = 0
    powt = 0
    while (iterations != max_iter):
        fx0 = getValue(f,x0,polly)
        fx1 = getValue(f,x1,polly)
        if fx1 - fx0 == 0:
            print(powt)
            return "niemożliwe jest zastosowanie metody, funkcja wymaga dzielenia przez 0"
        x = x1 - fx1 * ((x1 - x0) / (fx1 - fx0))
        fx = getValue(f,x,polly)
        if nearZero(fx,eps):
            print(powt)
            return x
        x0, x1 = x1, x
        powt = powt +1
        if max_iter != 0:
            iterations = iterations + 1

    return "nie udało się znaleźć miejsca zerowego"