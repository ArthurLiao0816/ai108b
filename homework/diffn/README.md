# 改進"diffn.py"，讓 4 次以上微分的誤差縮小或幾乎消失

## code
'''
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
'''

## 想法
* 考慮到"round-off error"，增加"step"的值
* 考慮到"truncation error"，增加"h"的係數

## 結果
'''
PS C:\Users\ldhsi\Desktop\人工智慧\ai108b\homework\diffn> py .\diffn.py
df(sin, pi/4)= 0.7070007199422376
dfn(sin, 0 pi/4)= 0.7071067811865476
dfn(sin, 1 pi/4)= 0.7070007199422376
dfn(sin, 2 pi/4)= -0.7068946746064139
dfn(sin, 3 pi/4)= -0.7067886451754084
dfn(sin, 4 pi/4)= 0.7066826316590169
dfn(sin, 5 pi/4)= 0.7065766327652175
dfn(sin, 6 pi/4)= -0.706470658422707
dfn(sin, 7 pi/4)= -0.7063633774336147
dfn(sin, 8 pi/4)= 0.7062631803376259
dfn(sin, 9 pi/4)= 0.7047745295023075
'''