import numpy
from numpy.random import random
from math import exp

def ejercicio2 (n):

    exitos = 0

    for _ in xrange(n):

        Up = random()

        if Up < 0.5:
            x = random() + random()

        else:
            x = random() + random() + random()

        if x >= 1.0:
            exitos += 1


    return float(exitos)/n

#print "prob de ganar con n: 100000, P(X)=", ejercicio2(100000)


def ejercicio3(flag, n):

    suma = 0

    for _ in xrange(n):

        if flag == "a":
            U = random()
            aux = (1-(U**2))**(1.5)
            suma += aux

        elif flag == "b":
            U = random()
            aux = (((1/U) + 1) * ((1 + ((1/U) + 1) ** 2) ** (-2)))/ U ** 2
            suma += aux

        elif flag == "c":
            U = random()
            aux = 2 * ((exp(-((1/U) + 1) ** 2)) / U ** 2)
            suma += aux

        elif flag == "d":
            U = random()
            U2 = random()
            aux = exp((U + U2) ** 2)
            suma += aux

        else:
            U = random()
            U2 = random()
            aux = (exp(-(2 * U * (1/U2) + 2)))/ (U2 ** 2)
            suma += aux

    return float(suma)/n

#print "integral a = ", ejercicio3('a', 1000000)
#print "integral b = ", ejercicio3('b', 1000000)
#print "integral c = ", ejercicio3('c', 1000000)
#print "integral d = ", ejercicio3('d', 1000000)
#print "integral e = ", ejercicio3('e', 1000000)


def ejercicio4 (n):

    N = 0
    U = 0.0

    for _ in xrange(n):

        while U <= 1.0:

            U += random()
            N += 1

        U = 0.0

    return float(N)/n

#print "E[N] con n: 100 =", ejercicio4(100)
#print "E[N] con n: 10000 =", ejercicio4(10000)
#print "E[N] con n: 1000000 =", ejercicio4(1000000)

def ejercicio5 (n):

    N = 0
    U = random()

    for _ in xrange(n):
        while U >= exp(-3):
            U = U * random()
            N += 1

        U = 0.0

    return float(N)/n

#print "E[N](pi) con n: 100 =", ejercicio5(100)
#print "E[N](pi) con n: 10000 =", ejercicio5(10000)
#print "E[N](pi) con n: 1000000 =", ejercicio5(1000000)


