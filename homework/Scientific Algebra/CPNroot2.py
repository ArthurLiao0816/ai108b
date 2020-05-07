# Complex Number root2
import cmath
import math

def root2(a,b,c):
    t = b*b - 4*a*c
    if t<0:
        t2 = cmath.sqrt(t)
    else:
        t2 = math.sqrt(t)
    return [(-b+t2)/(2*a), (-b-t2)/(2*a)]

print("root of 4x^2+ 1x+ 1=", root2(4,1,1))
