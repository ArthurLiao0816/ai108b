# initial data
obj = ["Human", "Sheep", "Wolf", "Kale"]    # Kale : 甘藍菜
sta = [False, False, False, False]


# successful condition : all members are alive
def alive(sta):
    if(sta[1] == sta[2] & sta[1] != sta[0]):    # Sheep's dead.
        return False
    if(sta[1] == sta[3] & sta[1] != sta[0]):    # Kale's eaten.
        return False
    return True                                 # They're all alive.

# generate the next status
def dfs(s):
    returnSta = []                      # returning variable 
    
    for i in range(0, 4):
        if(sta[0] != sta[i]):           # If there's anyone who's at the opposite of Human,
            continue                    # keep generating the next status.

        nextSta = sta[:]                # copy of current status
        nextSta[0] = not nextSta[0]     # Human goes across the river.
        nextSta[i] = nextSta[0]         # Appointed animal goes accompany with Human.

        if(alive(nextSta)):             # If next status we about to move in fits successful condition, 
            returnSta.append(nextSta)   # upgrade returning status.
        
    return returnSta                    # end of "dfs()"

# 
        