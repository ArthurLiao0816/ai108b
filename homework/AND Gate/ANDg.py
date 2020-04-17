import gd2
import numpy as np

def sig(t):
    return 1/(1+np.exp(-t))

def f(p):
    X = p
    Y = np.dot(A, X)
    for i in Y:
        i = sig(i)
        i = 1 if i >= 0.5 else 0
    return (np.linalg.norm(Y - B, 2))**2
A = np.array([[0, 0, 1],  # A矩陣為輸入
            [0, 1, 1],
            [1, 0, 1],
            [1, 1, 1]])
                
B = np.array([[0.0, 0, 0, 1]])  # B矩陣為標準答案

p = np.array([0.0, 0 ,0])   # 設定 w1、w2、b 的初始值

p = gd2.gradientDescendent(f, p)  # 用梯度下降法找最低點

print("\n\nw1 = {}, w2 = {}, b = {}" .format(p[0], p[1], p[2]))

C = np.dot(A, p)
result = []
for i in C:
    result.append(1) if i >= 0.5 else result.append(0)

print("\tx y | o")
for i in range(len(result)):
    print("\t{} {} | {}".format(A[i][0], A[i][1], result[i]))