from math import *

r = 3
step = 0.01
def df(f, x, h=step):
    return (f(x+r*h)-f(x-r*h))/(2*r*h)

def dfn(f, x, n, h=step):
    if (n == 0): return f(x)
    if (n == 1): return df(f,x,h)
    return (dfn(f, x+r*h, n-1) - dfn(f, x-r*h, n-1))/(2*r*h)

print('df(sin, pi/4)=', df(sin, pi/4))

for i in range(10):
    print('dfn(sin,', i, 'pi/4)=', dfn(sin, pi/4, i))
