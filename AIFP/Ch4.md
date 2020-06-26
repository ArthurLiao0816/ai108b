# 圖形搜尋 ( 實作 《狼、羊、甘藍菜》過河的問題 )
---

## 想法
1. 先明白問題的規定(如狼跟羊不能獨處...)

2. 將所有的可能走法列出來，然後判斷符不符合規則

3. 符合規則的走法不能重複走，所以設一個函式將其記錄下來

4. 一開式跑還不知道有兩組答案，所以加了個變數 "slnCnt" 幫他們標號

5. 把結果用函式印的美美噠

## code
```
# initial data
obj = ["Human", "Wolf", "Sheep", "Kale"]       # Obviously, these are objects.    (Kale : 甘藍菜
status = [False, False, False, False]          # This is all initial status of the former objects.
htySta = [status]                              # This variable could help recording which step we've gone to.
sltCnt = 0                                     # And this is ..., no offense, just number of solutions.   (not a discrimination


# successful condition : all members are alive
def alive(sta):
    if(sta[1] == sta[2]) & (sta[1] != sta[0]):    # Sheep's dead.
        return False
    if(sta[2] == sta[3]) & (sta[2] != sta[0]):    # Kale's eaten.
        return False
    return True                                   # They're all alive.

# generate the next status
def generate(sta):
    nextStaList = []                    # returning variable 
    
    for i in range(0, 4):
        if(sta[0] != sta[i]):           # If there's anyone who's at the opposite of Human,
            continue                    # keep generating the next status.

        nextSta = sta[:]                # copy of current status
        nextSta[0] = not nextSta[0]     # Human goes across the river.
        nextSta[i] = nextSta[0]         # Appointed animal goes accompany with Human.

        if(alive(nextSta)):             # If next status we about to move in fits successful condition, 
            nextStaList.append(nextSta) # upgrade returning status.
        
    return nextStaList                  # end of "generate()"

# Find the solution of this question while distiguish if we've gone to the current step.
def solution(htySta):
    global sltCnt
    curSta = htySta[len(htySta) - 1]
    nextStaList = generate(curSta)                  # "nextStaList" stores all possible status groups of current status.

    for nextSta in nextStaList:
        if nextSta in htySta:                       # Check current group of status. If it has been searched,
            continue                                # we'll pass this group.

        htySta.append(nextSta)                      # And if this ststus group hasn't been searched,
                                                    # we add it to "htySta" variable for recording.

        if(isDone(nextSta)):                        # If we fing one set of solutions, print it.
            sltCnt += 1
            print("Solution" + str(sltCnt) + ":")
            prtHtySta(htySta)
        else:
            solution(htySta)                        # If we haven't found a solution, keep searching.

        htySta.pop()

# To see if we have a solution
def isDone(sta):
    return sta[0] and sta[1] and sta[2] and sta[3]  # Because when an object reaches the opposite shore, 
                                                    # we set its value to true. 
                                                    # Therefore, if we want to know whether the search is over, 
                                                    # just use AND gate to connect statuses of all objects.
# Beautify the performance of the output.
def prtHtySta(htySta):
    prtStr = ""
    for sta in htySta:
        prtStr += "\t"
        for i in range(0, 4):
            prtStr += str(obj[i]) + " " + str(sta[i]) + " "
        prtStr += "\n"
    print(prtStr + "\n")

# main
solution(htySta)
print("Success!!! Find " + str(sltCnt) + " solutions.")
```

## 結果
```
PS C:\Users\ldhsi\Desktop\人工智慧\ai108b\homework\HWSV_pbm> py .\HWSV_pbm.py
Solution1:
        Human False Wolf False Sheep False Kale False 
        Human True Wolf False Sheep True Kale False   
        Human False Wolf False Sheep True Kale False
        Human True Wolf True Sheep True Kale False
        Human False Wolf True Sheep False Kale False
        Human True Wolf True Sheep False Kale True
        Human False Wolf True Sheep False Kale True
        Human True Wolf True Sheep True Kale True


Solution2:
        Human False Wolf False Sheep False Kale False
        Human True Wolf False Sheep True Kale False
        Human False Wolf False Sheep True Kale False
        Human True Wolf False Sheep True Kale True
        Human False Wolf False Sheep False Kale True
        Human True Wolf True Sheep False Kale True
        Human False Wolf True Sheep False Kale True
        Human True Wolf True Sheep True Kale True


Success!!! Find 2 solutions.
```