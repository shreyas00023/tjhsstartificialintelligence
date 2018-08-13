import math


def parabola(x):
    return x**2

def trig(x):
    return math.sin(x)+math.sin(2*x)+math.sin(5*x)

def find_min(func, a, b, e):
    while abs(a - b) > e:
        c = (b - a) / 3 + a
        d = b - (b - a) / 3
        if func(c) < func(d):
            b = d
        else:
            a = c
    return a, func(a)

#print(find_min(trig, -10, 10, 1*10**-60))
