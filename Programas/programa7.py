"""
Funciones
"""
def cuadrado(x):
    return x*x

def cuadrado2(x):
    return x**2

def varios(x):
    return x**2, x**3, True


print(cuadrado(6))
print(cuadrado2(6))

x1, x2, x3 = varios(2)
print("{} {} {}".format(x1, x2, x3))

a, _, b = varios(3)
_, a, b = varios(3)
_,_, b= varios(3)