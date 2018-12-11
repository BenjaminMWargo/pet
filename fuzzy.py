#=========Fuzzy Logic========
def mFuzzyAnd(a,b):
    return min(a,b)
def mFuzzyOr(a,b):
    return max(a,b)
def mFuzzyNot(a):
    return 1-a
def mFuzzyCheck(x):
    return (True if x>=.5 else False)
#=======Slope Functuions===========
def downSlope(x,left,right):
    slope = ((-1)/(right-left))
    b = -((slope*right))
    return (slope*x) + b
def upSlope(x,left,right):
    slope = ((1)/(right-left))
    b = -((slope*left))
    return (slope*x) + b
#========Fuzzy HP=========
def mIsCritical(x):
    #Downward Line
    leftBound = 20
    rightBound = 50
    y = x.stats.hp
    if (y <= leftBound):
        return 1
    elif (y>=rightBound):
        return 0
    else:
        return downSlope(y,leftBound,rightBound)                 #(((-1/25)*y)+(9/5))
def mIsHurt(x):
    #peaking line
    leftBound = 20
    rightBound = 80
    peak = 50
    y = x.stats.hp
    if ((y <= leftBound) or (y>=rightBound)):
        return 0
    else:
        if (y<=peak):
            #upslope
            return upSlope(y,leftBound,peak)
        else:
            #downslope
            return downSlope(y,peak,rightBound)
def mIsHealthy(x):
    #upward Line
    leftBound = 50
    rightBound = 80
    y = x.stats.hp
    if (y <= leftBound):
        return 0
    elif (y>=rightBound):
        return 1
    else:
        return upSlope(y,leftBound,rightBound)
#==========Happpy Fuzzy =====================
def mIsSad(x):
    #Downward Line
    leftBound = 20
    rightBound = 50
    y = x.stats.happiness
    if (y <= leftBound):
        return 1
    elif (y>=rightBound):
        return 0
    else:
        return downSlope(y,leftBound,rightBound)                 #(((-1/25)*y)+(9/5))
def mIsIndifferent(x):
    #peaking line
    leftBound = 20
    rightBound = 80
    peak = 50
    y = x.stats.happiness
    if ((y <= leftBound) or (y>=rightBound)):
        return 0
    else:
        if (y<=peak):
            #upslope
            return upSlope(y,leftBound,peak)
        else:
            #downslope
            return downSlope(y,peak,rightBound)
def mIsHappy(x):
    #upward Line
    leftBound = 50
    rightBound = 80
    y = x.stats.happiness
    if (y <= leftBound):
        return 0
    elif (y>=rightBound):
        return 1
    else:
        return upSlope(y,leftBound,rightBound)
#======Hunger Check============
def mIsVeryHungry(x):
    #Downward Line
    leftBound = -75
    rightBound = -40
    y = x.stats.hunger
    if (y <= leftBound):
        return 1
    elif (y>=rightBound):
        return 0
    else:
        return downSlope(y,leftBound,rightBound)
def mIsHungry(x):
    #peaking line
    leftBound = -75
    rightBound = 0
    peak = -40
    y = x.stats.hunger
    if ((y <= leftBound) or (y>=rightBound)):
        return 0
    else:
        if (y<=peak):
            #upslope
            return upSlope(y,leftBound,peak)
        else:
            #downslope
            return downSlope(y,peak,rightBound)
def mIsNormalHunger(x):
    #peaking line
    leftBound = -40
    rightBound = 40
    peak = 0
    y = x.stats.hunger
    if ((y <= leftBound) or (y>=rightBound)):
        return 0
    else:
        if (y<=peak):
            #upslope
            return upSlope(y,leftBound,peak)
        else:
            #downslope
            return downSlope(y,peak,rightBound)
def mIsFull(x):
    #peaking line
    leftBound = 0
    rightBound = 75
    peak = 40
    y = x.stats.hunger
    if ((y <= leftBound) or (y>=rightBound)):
        return 0
    else:
        if (y<=peak):
            #upslope
            return upSlope(y,leftBound,peak)
        else:
            #downslope
            return downSlope(y,peak,rightBound)
def mIsVeryFull(x):
    #upward Line
    leftBound = 40
    rightBound = 75
    y = x.stats.hunger
    if (y <= leftBound):
        return 0
    elif (y>=rightBound):
        return 1
    else:
        return upSlope(y,leftBound,rightBound)