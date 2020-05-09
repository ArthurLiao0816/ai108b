from sympy import Function, dsolve, Eq, Derivative, symbols
from sympy.abc import C, V, R, t
V = Function('V')
sol = dsolve(Derivative(V(t), t, 1)*C + V(t)/R, V(t))
print('dsolve(Derivative(V(t), t), V(t))=', sol.doit())
