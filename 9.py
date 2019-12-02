import math

def rownanie(a, b, c):
    delta = (b**2) - (4*a*c)
    x1 = (-b - math.sqrt(delta))/(2*a)
    x2 = (-b + math.sqrt(delta))/(2*a)
    return x1, x2

print(rownanie(1, 2, -1))