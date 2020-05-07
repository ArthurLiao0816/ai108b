# 擴展到複數上的"root2"

## code
'''
import cmath

def root2(a,b,c):
    t = b*b - 4*a*c
    t2 = cmath.sqrt(t)
    return [(-b+t2)/(2*a), (-b-t2)/(2*a)]

print("root of 4x^2+ 1x+ 1=", root2(4, 1, 1))
'''

## 想法
* 利用"cmath"模組提供的複數運算，在判別式小於零時，能夠回傳複數解

## 結果
'''
PS C:\Users\ldhsi\Desktop\人工智慧\ai108b\homework\Scientific Algebra> py .\CPNroot2.py
root of 4x^2+ 1x+ 1= [(-0.125+0.4841229182759271j), (-0.125-0.4841229182759271j)]
'''