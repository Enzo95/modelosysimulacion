from random import random, shuffle
from math import log, exp
from parcialVariables import varianzaEsperanza, poisson

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
ejercicio 1
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def ejer1ex():
    '''
    EJERCICIO CON METODO DE LA INVERSA
    '''
    # simulo U~u(0,1)
    U = random()
    if U > 1/float(4):
        X = 6 - 6 * sqrt((1-U)/ 3.0)

    else:
        X = 2 + 2 * sqrt(U)

    return X

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
ejercicio 2 / metodo inversa
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def ejer2ex1(alpha, beta):
    '''
    EJERCICIO CON METODO 1
    '''
    # simulamos U~u(0,1)
    U = random()
    X = -log(U) / alpha

    return X**(1 / float(beta))

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
ejercicio 6
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def ejer6a(n):
    # lis of uniforms
    uniforms = [random() for _ in xrange(n)]
    return max(uniforms)

def ejer6b(n):
    # simulate a uniform
    while U >= n*(X**(n - 1)):
        U = random()
        X = random()

    X = U
    return X

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
ejercicio 7
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def ejer7a():
    # constantes
    e = exp(1)

    while True:
        # Generar V ~ exp
        Z = random()
        X = -2 * log(Z)
        # Generar U
        U = random()

        if U < (e * X * exp(-X / 2)) / 2:
            break

    return X

print (varianzaEsperanza(ejer7a,100))


def ejer10(lamb, T):
    n = poissonExt(lamb * T)
    arrival = [random() * T for _ in xrange(n)]
    arrival.sort()

    return arrival

"""""""""""""""""
--Ejercicio 10-- 
"""""""""""""""""

def generaEventos(lamb,T):
    t = 0
    I = 0
    S = []
    while True:
        U = random()

        lamb = 1/float(lamb)
        if t - lamb*log(U) > T:
            break
        else:
            t = t -lamb*log(U)
            I += 1
            S.append(t)
    return S



"""""""""""""""""""""""""""""""""
--Lambda = 5 -----Ejercicio 11---
"""""""""""""""""""""""""""""""""
def Poisson(lamb,t):
    suma = random()
    i = 0
    # N(T)=min(n|x1,x2...,xn < e^-lambda*t) - 1
    while suma > exp(-lamb*t):
        i += 1
        suma *= random()
    # i es la cantidad de variables a generar (bondis)
    return i

def ejercicio11(T):
    n = Poisson(5,T)
    S = []
    for i in range(n):
        u = random()
        temp = u*T
        S.append(temp)
    S.sort()
    sumab= 0
    for i in xrange(n):
        t = random()
        t = int(t*20) + 20
        sumab += t

    return sumab

def a(t):
    return 3 + 4/(t+1)

def adelgazamiento(lamb, T):
    t, i = 0, 0
    S = []

    while True:
        # generar U uniform(0, 1)
        U = random()

        if t - log(U) / lamb > T:
            break

        else:
            t = t - log(U) / lamb
            # generar V
            V = random()

            if V < a(t) / lamb:
                i += 1
                S.append(t)

    return i

def esperanza(n = 100):
    X = 0
    Y = 0
    Z = 0
    for _ in xrange(n):
        X += adelgazamiento(7,10)

    return X / float(n)

print (esperanza(100))
