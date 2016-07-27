import numpy
from random import random, shuffle
from math import exp, floor, log

def ejercicio1 (n):

    exitos = 0
    exitos_cuadra = 0

    for _ in xrange(n):
        baraja = range(1, 101)
        shuffle(baraja)
        permutar(baraja)

        for i in xrange(1, 101):
            if i == baraja[i-1]:
                exitos += 1

    exitos_cuadra = exitos ** 2
    print exitos, exitos_cuadra
    return (exitos/float(n), (exitos_cuadra/float(n))-(exitos/float(n))**2)


def permutar (baraja):

    k = len(baraja) - 1

    while k > 1:

        U = random()
        I = int(floor(U * k))
        baraja[k],baraja[I] = baraja[I], baraja[k]
        k -= 1

#print "(E[numero de exitos], V[num de exitos])con n:1000 = ", ejercicio1(1000)


def ejercicio2 (n):

    suma_parcial = 0

    for _ in xrange(n):

        U = random()
        X = floor(10000 * U) + 1
        suma_parcial += exp(U/10000)

    return suma_parcial/float(n)

#print "aproximacion para 100 num aleatorios: ", ejercicio2(100)


def ejercicio3 (n):

    num_tiradas = 0
    for _ in xrange(n):
        sumas = range(2, 13)

        while sumas != []:

            D1 = int(random() * 6) + 1
            D2 = int(random() * 6) + 1
            suma = D1 + D2
            num_tiradas += 1

            if suma in sumas:
                sumas.remove(suma)

    esperanza = num_tiradas/float(n)
    varianza = (num_tiradas ** 2/float(n)) - (esperanza ** 2)

    return (round(esperanza), round(varianza, 2))

#print "E[num_tiradas], V[num_tiradas] con n: 100 = ", ejercicio3(100)
#print "E[num_tiradas], V[num_tiradas] con n: 1000 = ", ejercicio3(1000)
#print "E[num_tiradas], V[num_tiradas] con n: 10000 = ", ejercicio3(10000)
#print "E[num_tiradas], V[num_tiradas] con n: 100000 = ", ejercicio3(100000)


def ejer4ex():
    # generar variable aleatorea U en (0, 1)
    U = random()
    if U < 0.5:

        # generamos V unif(0,1)
        V = random()
        j = 1
        # para generar X1
        P = (1 / float(2))

        while V >= P:
            j += 1
            P += 0.5**j # Es equivalente a P += 0.5**j

    else:
        # generamos V unif(0,1)
        V = random()
        j = 1

        P = (1 / float(2)) * (2 / float(3))

        while V >= P:
            j += 1
            P += (2/float(3))**j*(1 / float(2))

    return j


# otra forma de hacerlo
def ejer4ex2():
    '''
    CON GEOMETRICA
    '''
    # simular uniforme en ~(0,1)
    U = random()

    if U < 0.5:
        # generamos otra V v.a uniforme en (0,1)
        V = random()
        # X geometrica
        X = int(log(V) / log(1 / float(2))) + 1

    else:
        # generamos otra V v.a uniforme en (0,1)
        V = random()
        # X geometrica P = 1/3
        X = int(log(V) / log(2 / float(3))) + 1

    return X

def ejer5a(lam, k):
    '''
    METODO DE TRANSFORMACION INVERSA
    '''
    # genero el denominador
    r = exp(-lam)
    denomi = r

    for j in xrange(1, k + 1):
        r = r * (lam / float(j))
        denomi += r

    # genero U~u(0,1)
    U = random()
    p = exp(-lam) / denomi
    F = p

    i = 0
    while U >= F:
        i += 1
        p *= lam / float(i)
        F += p

    return i

def ejer5b(lam, k):
    '''
    METODO DE ACEPTACION y RECHAZO
    '''
    X = poisson(lam)
    while X >= k:
        X = poisson(lam)
    return X

def ejer5c(lam, k):
    '''
    METODO DE ACEPTACION y RECHAZO
    '''
    while True:
        X = poisson(lam)
        U = random()
        if X <= k:
            break
    return X


