# 梯度下降法 ( 實作 AND Gate )
---

## target
AND gate
x  |  y | o |= and(x,y)
---|----|---|---
0  | 0  | 0 |x0 y0 o0
0  | 1  | 0 |x1 y1 o1
1  | 0  | 0 |x2 y2 o2
1  | 1  | 1 |x3 y3 o3

## thought
* 設一個矩陣A作為線性方程組的係數
    ```
    sig(w1*0 + w2*0 + b) = o0
    sig(w1*0 + w2*1 + b) = o1
    sig(w1*1 + w2*0 + b) = o2
    sig(w1*1 + w2*1 + b) = o3
    ```
* 設矩陣p為[w1, w2, b]並定下初始值
* 設矩陣B為標準答案
* f(x,y,w1,w2,b) = (o0-0)^2 + (o1-0)^2 + (o2-0)^2 + (o3-1)^2
* 藉由梯度下降法找到w1, w2, b的最小值，使其帶入線性方程組後的結果符合AND閘
* 印出結果

## code
    ```
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
    print("\t----|--")
    for i in range(len(result)):
        print("\t{} {} | {}".format(A[i][0], A[i][1], result[i]))
    ```

## result
    ```
    PS C:\Users\ldhsi\Desktop\人工智慧\ai108b\homework\AND Gate> py .\ANDg.py
    1:p=[0. 0. 0.] f(p)=1.000 gp=[-1.98 -1.98 -1.96] glen=3.41795
    2:p=[0.0198 0.0198 0.0196] f(p)=0.889 gp=[-1.7828 -1.7828 -1.6448] glen=3.01034
    3:p=[0.037628 0.037628 0.036048] f(p)=0.802 gp=[-1.61004  -1.61004  -1.370592] glen=2.65763
                            ...
    427:p=[ 0.49824199  0.49824199 -0.25291475] f(p)=0.250 gp=[-0.00220708 -0.00220708  0.0026179 ] glen=0.00407
    428:p=[ 0.49826406  0.49826406 -0.25294093] f(p)=0.250 gp=[-0.00217937 -0.00217937  0.00258504] glen=0.00402
    429:p=[ 0.49828585  0.49828585 -0.25296678] f(p)=0.250 gp=[-0.00215201 -0.00215201  0.00255258] glen=0.00397


    w1 = 0.49828585024747285, w2 = 0.49828585024747285, b = -0.25296677727839717
            x y | o
            ----|--
            0 0 | 0
            0 1 | 0
            1 0 | 0
            1 1 | 1
    ```