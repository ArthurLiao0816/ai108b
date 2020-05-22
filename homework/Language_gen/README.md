# 請寫一個可以產生文章或語句的程式
***

## thought
* 做出可以描述基本排球動作的程式

## code
```
import random

position = ["大砲", "二傳", "副攻", "自由"]
work = [["組織進攻", "舉球", "扣球", "吊球", "接球", "攔網"],   # second
        ["接球"],                                             # libero
        ["接球", "扣球", "攔網"],                              # ace
        ["接球", "扣球", "攔網"]                               # co-att
        ]

def command():
    p = random.choice(position)
    if p == "大砲":
        w = random.choice(work[2])
    elif p == "二傳":
        w = random.choice(work[0])
    elif p == "副攻":
        w = random.choice(work[3])
    else:
        w = random.choice(work[1])
    return print(p + "! " + w)
    
def Position():
    return random.choice(position)
# main
command()
```

## result
```
PS C:\Users\ldhsi\Desktop\人工智慧\ai108b\homework\Language_gen> py .\Language_gen.py
自由! 接球
PS C:\Users\ldhsi\Desktop\人工智慧\ai108b\homework\Language_gen> py .\Language_gen.py
副攻! 攔網
PS C:\Users\ldhsi\Desktop\人工智慧\ai108b\homework\Language_gen> py .\Language_gen.py
自由! 接球
PS C:\Users\ldhsi\Desktop\人工智慧\ai108b\homework\Language_gen> py .\Language_gen.py
副攻! 接球
PS C:\Users\ldhsi\Desktop\人工智慧\ai108b\homework\Language_gen> py .\Language_gen.py
二傳! 組織進攻
PS C:\Users\ldhsi\Desktop\人工智慧\ai108b\homework\Language_gen> py .\Language_gen.py
大砲! 扣球
PS C:\Users\ldhsi\Desktop\人工智慧\ai108b\homework\Language_gen> py .\Language_gen.py
大砲! 扣球
```