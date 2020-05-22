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