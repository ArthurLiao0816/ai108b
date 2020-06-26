# 科學計算ㄟ練習
---

## 目錄
1. [擴展到複數上的"root2"](#擴展到複數上的"root2")
2. [改進"diffn.py"，讓 4 次以上微分的誤差縮小或幾乎消失](#改進"diffnpy"讓-4-次以上微分的誤差縮小或幾乎消失)
3. [用 sympy 去求解 RC 電路的微分方](#用-sympy-去求解-rc-電路的微分方程)
4. [改寫 fftRandom.py 程式在不存取 freq 的情況下，透過 ifft 的結果，印出真正的 freq](#改寫-fftrandompy-程式在不存取-freq-的情況下透過-ifft-的結果印出真正的-freq)

## 擴展到複數上的"root2"

### code
```
import cmath

def root2(a,b,c):
    t = b*b - 4*a*c
    t2 = cmath.sqrt(t)
    return [(-b+t2)/(2*a), (-b-t2)/(2*a)]

print("root of 4x^2+ 1x+ 1=", root2(4, 1, 1))
```

### 想法
* 利用"cmath"模組提供的複數運算，在判別式小於零時，能夠回傳複數解

### 結果
```
PS C:\Users\ldhsi\Desktop\人工智慧\ai108b\homework\Scientific Algebra> py .\CPNroot2.py
root of 4x^2+ 1x+ 1= [(-0.125+0.4841229182759271j), (-0.125-0.4841229182759271j)]
```

## 改進"diffn.py"，讓 4 次以上微分的誤差縮小或幾乎消失

### code
```
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
```

### 想法
* 考慮到"round-off error"，增加"step"的值
* 考慮到"truncation error"，增加"h"的係數

### 結果
```
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
```

## 用 sympy 去求解 RC 電路的微分方程

### code
```
from sympy import Function, dsolve, Eq, Derivative, symbols
from sympy.abc import C, V, R, t
V = Function('V')
sol = dsolve(Derivative(V(t), t, 1)*C + V(t)/R, V(t))
print('dsolve(Derivative(V(t), t), V(t))=', sol.doit())
```

### 想法
* 將要微分方程式:C*V'(t) + V(t)/R，放入desolve函式中求解
* V(t)  = exp((C1 - t/R)/C)
        = exp((C1/(R*C))*exp(-t/(R*C))
        = V0*exp(-t/(R*C))

### 結果
```
PS C:\Users\ldhsi\Desktop\人工智慧\ai108b\homework\diffeqRC> py .\diffeq1.py
dsolve(Derivative(V(t), t), V(t))= Eq(V(t), exp((C1 - t/R)/C))
```

## 改寫 fftRandom.py 程式在不存取 freq 的情況下，透過 ifft 的結果，印出真正的 freq

### code
```
import random
import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(precision=4, suppress=True)
freq = random.randint(0,4)
t = np.arange(0, 10, 0.1)
ft = 10*np.cos(2*np.pi*freq*t) #10*cos(2*pi*f*t)
n = len(ft)
t1 = t[range(int(n/2))]
fi = np.fft.fft(ft)

fi1 = fi[range(int(n/2))]
print('ft=', ft)
print('fi=', fi)
print('freq= ', freq)

fig, ax = plt.subplots(2, 1)

ax[0].plot(t,ft, color="red", linewidth=2)
ax[0].set_xlabel('x')
ax[0].set_ylabel('y')
 
ax[1].plot(t1,fi1, color="blue", linewidth=2)
ax[1].set_xlabel('freq')
ax[1].set_ylabel('y')

plt.show()

```

### 想法
* 把pi由t移置ft，使其成為10cos(2pi*ft)，看起來跟傅立葉分析公式比較像，增加可讀性
* 發現freq在圖上會有對稱性，也就是會印出兩個freq，所以將freq由[0, 1, ..., 10]這幾種可能值調成[0, 1, ..., 4]、同時將圖的x軸長度調成原本的一半，去除對稱性，這樣印在圖上的freq就是唯一且正確的值
### result
```
PS C:\Users\ldhsi\Desktop\人工智慧\ai108b\homework\fftfreq> py .\fftfreq.py
ft= [ 10.       8.0902   3.0902  -3.0902  -8.0902 -10.      -8.0902  -3.0902
   3.0902   8.0902  10.       8.0902   3.0902  -3.0902  -8.0902 -10.
  -8.0902  -3.0902   3.0902   8.0902  10.       8.0902   3.0902  -3.0902
  -8.0902 -10.      -8.0902  -3.0902   3.0902   8.0902  10.       8.0902
   3.0902  -3.0902  -8.0902 -10.      -8.0902  -3.0902   3.0902   8.0902
  10.       8.0902   3.0902  -3.0902  -8.0902 -10.      -8.0902  -3.0902
   3.0902   8.0902  10.       8.0902   3.0902  -3.0902  -8.0902 -10.
  -8.0902  -3.0902   3.0902   8.0902  10.       8.0902   3.0902  -3.0902
  -8.0902 -10.      -8.0902  -3.0902   3.0902   8.0902  10.       8.0902
   3.0902  -3.0902  -8.0902 -10.      -8.0902  -3.0902   3.0902   8.0902
  10.       8.0902   3.0902  -3.0902  -8.0902 -10.      -8.0902  -3.0902
   3.0902   8.0902  10.       8.0902   3.0902  -3.0902  -8.0902 -10.
  -8.0902  -3.0902   3.0902   8.0902]
fi= [  0.+0.j   0.+0.j   0.-0.j   0.+0.j   0.+0.j   0.+0.j   0.+0.j   0.-0.j
  -0.-0.j   0.+0.j 500.+0.j  -0.+0.j  -0.+0.j  -0.-0.j  -0.-0.j  -0.+0.j
  -0.-0.j  -0.-0.j   0.-0.j   0.+0.j  -0.+0.j  -0.-0.j  -0.+0.j  -0.+0.j
   0.-0.j  -0.-0.j  -0.+0.j  -0.+0.j  -0.+0.j  -0.-0.j  -0.-0.j   0.-0.j
   0.+0.j   0.+0.j  -0.+0.j   0.-0.j  -0.+0.j  -0.+0.j  -0.+0.j  -0.-0.j
  -0.-0.j  -0.-0.j   0.-0.j   0.-0.j   0.+0.j  -0.-0.j   0.-0.j   0.+0.j
   0.+0.j  -0.-0.j   0.+0.j  -0.+0.j   0.-0.j   0.-0.j   0.+0.j  -0.+0.j
   0.-0.j   0.+0.j   0.+0.j  -0.+0.j  -0.+0.j  -0.+0.j  -0.-0.j  -0.-0.j
  -0.-0.j   0.+0.j  -0.-0.j   0.-0.j   0.-0.j   0.+0.j  -0.+0.j  -0.+0.j
  -0.-0.j  -0.-0.j   0.+0.j  -0.+0.j   0.+0.j  -0.-0.j  -0.-0.j  -0.+0.j
  -0.-0.j   0.-0.j  -0.+0.j  -0.+0.j  -0.+0.j  -0.-0.j  -0.+0.j  -0.+0.j
  -0.-0.j  -0.-0.j 500.-0.j   0.-0.j  -0.+0.j   0.+0.j   0.-0.j   0.-0.j
   0.-0.j   0.-0.j   0.+0.j   0.-0.j]
freq=  1
```
![1](https://github.com/ArthurLiao0816/ai108b/blob/master/homework/fftfreq/result.png)