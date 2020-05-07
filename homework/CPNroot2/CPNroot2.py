# Complex Number root2
import cmath

def root2(a,b,c):
    t = b*b - 4*a*c
    t2 = cmath.sqrt(t)
    return [(-b+t2)/(2*a), (-b-t2)/(2*a)]

print("root of 4x^2+ 1x+ 1=", root2(4, 1, 1))
# print("root of 4x^2+ 1x+ 1=", root2(1, 4, 1))