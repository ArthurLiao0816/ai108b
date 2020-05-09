# 用 sympy 去求解 RC 電路的微分方程

## code
'''
from sympy import Function, dsolve, Eq, Derivative, symbols
from sympy.abc import C, V, R, t
V = Function('V')
sol = dsolve(Derivative(V(t), t, 1)*C + V(t)/R, V(t))
print('dsolve(Derivative(V(t), t), V(t))=', sol.doit())
'''

## 想法
* 將要微分方程式:C*V'(t) + V(t)/R，放入desolve函式中求解
* V(t)  = exp((C1 - t/R)/C)
        = exp((C1/(R*C))*exp(-t/(R*C))
        = V0*exp(-t/(R*C))

## 結果
'''
PS C:\Users\ldhsi\Desktop\人工智慧\ai108b\homework\diffeqRC> py .\diffeq1.py
dsolve(Derivative(V(t), t), V(t))= Eq(V(t), exp((C1 - t/R)/C))
'''